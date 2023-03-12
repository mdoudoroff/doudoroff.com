#!python
# encoding: utf-8

import json, os, sys, markdown, unidecode, shortuuid, time

f = open('keywords.json','r')
KEYWORDS = json.load(f)
f.close()
KEYWORD_LUT = KEYWORDS['categories']
KEYWORD_LUT.update(KEYWORDS['functions'])

class Recipe(object):

	def __init__(self, d):
		self._rawdict = d

		self._rID = d['rID']
		self._title = d['title']
		self._sortKey = d.get('sortKey',self._title.lower())
		self._attribution = d.get('attribution','')
		self._principle = d.get('principle','')
		self._mdBody = d['mdBody']
		self._categories = d.get('categories',[])
		self._functions = d.get('functions',[])
		self._modules = d.get('modules',[])

	def fnForSelf(self):
		words = ' '.join(self._title.split(' ')[:4])
		norm = unidecode.unidecode(words).lower().replace(' ','_')
		for c in '''!@#$%^&*(){}[]'"…“‘’”<>?,./''':
			norm = norm.replace(c,'')
		return f'{self._rID}-{norm}.html'

	def kwCategories(self):
		return [f'cat_{kw}' for kw in self._categories]

	def kwFunctions(self):
		return [f'fn_{kw}' for kw in self._functions]

	def kwModules(self):
		# @@ this is probably wrong
		return [f'mod_{kw}' for kw in self._modules]

	def allKw(self):
		# print(self.kwCategories() + self.kwFunctions() + self.kwModules()) 
		return self.kwCategories() + self.kwFunctions() + self.kwModules()

	def hKeywordClasses(self):
		klasses = []
		for kw in self._categories:
			klasses.append(f'cat_{kw}')
		for kw in self._functions:
			klasses.append(f'fn_{kw}')
		for kw in self._modules:
			klasses.append(f'mod_{kw}')
		return ' '.join(klasses)

	def hSummary(self):
		return self._mdBody[:150] + ' ...'

	def hBody(self):
		return markdown.markdown(self._mdBody)

	def hKeywordSummary(self):
		klasses = []
		for kw in self._categories:
			if kw in KEYWORD_LUT:
				klasses.append( f'<a href="index.html?tag=cat_{kw}"><span class="kw_cat category">{KEYWORD_LUT[kw]}</span></a>' )
			else:
				print(f'ERROR: unrecognized keyword {kw}')
		for kw in self._functions:
			if kw in KEYWORD_LUT:
				klasses.append( f'<a href="index.html?tag=fn_{kw}"><span class="kw_fn function">{KEYWORD_LUT[kw]}</span></a>' )
			else:
				print(f'ERROR: unrecognized keyword {kw}')
		return ' '.join(klasses)


class Recipes(object):

	def __init__(self):
		self._recipes = self.loadRecipes()

	def loadRecipes(self):
		recipes = []
		rIDs = []

		candidates = [x for x in os.listdir('./_recipes') if x.split('.')[-1]=='json']

		for c in candidates:
			f = open(os.path.join('./_recipes',c),'r')
			try:
				j = json.load(f)
			except:
				print('ERROR: could not load JSON for file',c)
				sys.exit(1)
			f.close()

			# process rID and timestamp for new entries
			if not j.get('rID'):
				j['rID'] = shortuuid.uuid()[:8]
				j['createtime'] = time.time()
				f = open(os.path.join('./_recipes',c),'w')
				json.dump(j,f,indent=4)
				f.close()

			# pull in the markdown sidecar, if available
			mdfn = '.'.join(c.split('.')[:-1]) + '.md'
			if mdfn in os.listdir('./_recipes'):
				f = open(os.path.join('./_recipes',mdfn),'r')
				t = f.read()
				f.close()
				j['mdBody'] = t
			else:
				j['mdBody'] = ''

			r = Recipe(j)

			if r._rID in rIDs:
				print('Error: caught repeat rID ', r._rID)
				sys.exit(1)
			else:
				rIDs.append(r._rID)

			recipes.append(r)

		return recipes

recipes = Recipes()

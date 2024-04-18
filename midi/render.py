#!/usr/bin/env python3
# encoding: utf-8

import json, csv, sys

if sys.version_info[0] != 3:
    sys.exit("This script requires Python version 3")

html_top = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>MIDI Eurorack</title>
	<style>

		:root {
			--TRSA-color: red;
			--TRSB-color: blue;
			--TRSX-color: green;
			--TRSTBD-color: gray
		}

		body {
			max-width: 1600px;
			font-family: Georgia, serif;
			font-size: 16px;
			margin: 0;
			padding: 0;
		}
		p, li {
			max-width: 40rem;
			line-height: 1.4;
		}
		.updates {
			font-size: 85%;
			font-family: monospace;
		}
		a {text-decoration:none;}
		a:hover {color:red;text-decoration:underline;}
		a:visited {color:blue;}
		img {
			width: 100%;
			margin: 0.5em 0;
		}
		.main {	padding: 1em; }
		.red {color:red;}
		.green {color:green;}
		.gray {color:gray;}
		table {border-collapse: collapse;font-size: 85%;height: auto;}

		.tablesection { text-align: left; padding-top: 1em; }
		td, th {text-align:center;padding:0.25em 1em;border-bottom:1px solid #eee;}
		td.left, th.left {text-align:left;}
		td.notes {text-align: left;}
		td ul { padding-left: 20px; -webkit-padding-start: 20px; }
		th { 
			color: #666; position: sticky; top: 0px; 

			background-color: rgba(200,200,200,0.9);
		}
		.notes { min-width: 15em; }
		.collapsed {display: none; }
		td.left { 
			height: auto;
			position: sticky; 
			left: 0px; 
			z-index: 1;

			background-color: rgba(225,225,225,0.9);
		}
		th.left {
			height: auto;
			position: sticky; 
			left: 0px; 
			z-index: 2;
		}

		nav {
			background: #eef; 
			padding: 0.5em 1em;
			font-family: Helvetica, sans-serif;
			border-bottom: 2px solid #666;
			}
		nav div.navrail { display: flex; }
		nav ul { margin: 0.5em 0.5em 0.5em 0; padding: 0; font-size: 80%; }
		nav ul li { list-style: none; margin-right: 1em; line-height: 1; margin-bottom: 1em;}

		@media (max-width: 450px) {
			.main { padding: 1em 0.5em; }
			nav { padding: 0.25 0.5em; }
		}

		#comparisonSwitcher {
			font-size: 80%;
			display: flex;
			column-gap: 18px;
			align-items: center;
			justify-content: space-evenly;
		}

		@media (min-width: 400px) {
			#comparisonSwitcher {
				font-size: 100%;
			}
		}
		@media (min-width: 960px) {
			#comparisonSwitcher {
				justify-content: flex-start;
				column-gap: 24px;
			}
		}


		.TRSA { color: var(--TRSA-color); font-weight: bold; text-wrap: nowrap;}
		.TRSB { color: var(--TRSB-color); font-weight: bold; text-wrap: nowrap;}
		.TRSX { color: var(--TRSX-color); font-weight: bold; text-wrap: nowrap; }
		.TRSTBD { color: var(--TRSTBD-color); }


		.graph .labels.x-labels {
		  text-anchor: middle;
		}

		.graph .labels.y-labels {
		  text-anchor: end;
		}

		.graph {
		  height: 500px;
		  width: auto;
		}

		.graph .grid {
		  stroke: #ccc;
		  stroke-dasharray: 0;
		  stroke-width: 1;
		}

		.labels {
		  font-size: 13px;
		}

		.label-title {
		  font-weight: bold;
		  text-transform: uppercase;
		  font-size: 12px;
		  fill: black;
		}
	</style>
</head>
<body>

<nav id="comparisonSwitcher">
<a href="/mixers/">Stereo Mixers</a>
<a href="/sequencers/">Pitch+Gate Sequencers</a>
<a href="/samplers/">Samplers</a>
<a href="/quantizers/">Quantizers</a>
<strong>MIDI Eurorack</strong>
</nav>


<div class="main">

<h1>MIDI Eurorack</h1>

<p>Martin Doudoroff<br>
<script><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>


<p>This is a study of the rise of MIDI as a supplemental patching system to conventional audio and CV patching. Here, we are mainly concerned with 3.5mm TRS MIDI connectivity, although USB and DIN-based MIDI are acknowledged (and of course, DIN can be adapted to TRS via readily available cables).</p>
<p>TRS patching of MIDI in Eurorack is already supported by over 80 modules and it is clearly here to stay. Unfortunately, TRS MIDI has been hobbled right out of the gate by two de facto standards: Type A (Korg) and Type B (Arturia). There’s nothing more than a single wire tranposition between these two standards, but this complication remains a fact of life. (For the time being, I have disregarded another, rare variant that uses TR cables, as it seems to be neither here nor there.)</p>
<p>Scope-wise, this study largely disregards MIDI-to-CV converters, but includes CV-to-MIDI converters. Some of the modules below can perform MIDI-to-CV, but that is not why they are included. MIDI-to-CV converters are still relevant, of course, but that is well-established topic area.</p>
<p>Moreover, this study is exclusive to Eurorack modules. There are, of course, gobs of standalone devices out there that support MIDI over 3.5mm TRS cables or adapter cable.</p>
<p>Acknowledgements: this work began with <a href="https://modwiggler.com/forum/viewtopic.php?t=186808">this ModWiggler thread</a> by user <strong>kay_k</strong> in 2017, and many contributions by other ModWiggler users. ModWiggler user <strong>audionerd</strong> created the <a href="https://minimidi.world"><strong>minimidi.world</strong></a> project in 2019, which includes its own database (including many non-Eurorack entries) and an excellent presentation on cabling. I got some of the information in this study from both these sources, and collected the rest, myself, via ModularGrid and module documentation.</p>
<p>I plan to update this study with new modules (and corrections) for as long as it seems relevant to do so.</p>


<h4>Latest</h4>
<p class="updates">
2024-04-18 errata and a few stragglers<br>
2024-04-17 first draft<br>
<!--<span id="additionalUpdates" class="collapsed">
</span>
<a id="updatesToggle" onclick="toggleAdditionalUpdates();" href="javascript:void(0);">Show full revision history</a>-->
</p>

<script>
var status = "less";
function toggleAdditionalUpdates()
{  
    if (status == "less") {
        document.getElementById("additionalUpdates").className = "";
        document.getElementById("updatesToggle").innerText = "Hide full revision history";
        status = "more";
    } else if (status == "more") {
	    document.getElementById("additionalUpdates").className = "collapsed";
        document.getElementById("updatesToggle").innerText = "Show full revision history";
        status = "less"
    }
}
</script>


'''

html_bottom = '''



<p style="text-align:center;">• • •</p>

</div><!-- end div.main -->

<footer>
<nav>
<div class="navrail">
<ul>
	<li style="border-bottom: 2px solid gray;">Comparison guides</li>
	<li><a href="//doudoroff.com/mixers/">Stereo Mixer Modules</a></li>
	<li><a href="//doudoroff.com/sequencers/">Pitch &amp; Gate Sequencers</a></li>
	<li><a href="//doudoroff.com/samplers/">Sampler Modules</a></li>
	<li><a href="//doudoroff.com/quantizers/">Quantizer Modules</a></li>
	<li><strong>MIDI Eurorack</strong></li>
</ul>
<ul>
	<li style="border-bottom: 2px solid gray;">Martin’s other articles</li>
	<li><a href="//doudoroff.com/cold-mac/">Patching Cold Mac</a></li>
	<li><a href="//doudoroff.com/multitracking/">How to Multitrack Your Eurorack</a></li>
	<li><a href="//doudoroff.com/logic/">A Logic Cookbook for Synthesis</a></li>
	<li><a href="https://mdoudoroff.s3.amazonaws.com/sport-modulator-2+patch+book+draft+28-03-22.pdf">Sport Modulator 2 Patch Book</a></li>
	<li><a href="https://www.youtube.com/user/MartinDoudoroffLLC/videos">Martin’s YouTube videos</a></li>
</ul>
</div>
</nav>

</footer>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-11161564-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-11161564-1');
</script>


</body>
</html>
'''

rows = []
columnDisplayNames = {}

def logStat(year,type):
	if year not in TRS_year_stats:
		TRS_year_stats[year] = {'A':0,'B':0,'X':0}
	if type=='A':
		TRS_year_stats[year]['A']+=1
	if type=='B':
		TRS_year_stats[year]['B']+=1
	if type=='X':
		TRS_year_stats[year]['X']+=1


modules = []
class Module(object):
	def __init__(self, d):
		self._product = d['product']
		self._role = d['role']
		self._mg = d['_mgurl']
		self._year = d['year']

		self._mAin = d['mAin']
		self._mBin = d['mBin']
		self._mXin = d['mXin']
		self._mTBDin = d['mTBDin']
		self._mAout = d['mAout']
		self._mBout = d['mBout']
		self._mXout = d['mXout']
		self._mTBDout = d['mTBDout']
		self._musb = d['musb']
		self._mdin = d['mdin']

		self._notes = d['notes']

	def roles(self):
		return [x.strip() for x in self._role.split(';')]

	def hProduct(self):
		s = f'<strong>{self._product}</strong><br>{self._year}<br><small>'
		if self._mg:
			s += '<a href="{self._mg}" target="_blank">Modular Grid &gt;</a></small>'
		return s

	def hMIDI_in(self):
		if self._mAin.strip():
			if int(self._mAin) > 1:
				return f'<span class="TRSA">A × {self._mAin}</span>'
			else:
				return '<span class="TRSA">A</span>'
		if self._mBin.strip():
			if int(self._mBin) > 1:
				return f'<span class="TRSB">B × {self._mBin}</span>'
			else:
				return '<span class="TRSB">B</span>'
		if self._mXin.strip():
			if int(self._mXin) > 1:
				return f'<span class="TRSX">A/B × {self._mXin}</span>'
			else:
				return '<span class="TRSX">A/B</span>'
		if self._mTBDin.strip():
			if int(self._mTBDin) > 1:
				return f'<span class="TRSTBD">??? × {self._mTBDin}</span>'
			else:
				return '<span class="TRSTBD">???</span>'
		return ''

	def hMIDI_out(self):
		if self._mAout.strip():
			if int(self._mAout) > 1:
				return f'<span class="TRSA">A × {self._mAout}</span>'
			else:
				return '<span class="TRSA">A</span>'
		if self._mBout.strip():
			if int(self._mBout) > 1:
				return f'<span class="TRSB">B × {self._mBout}</span>'
			else:
				return '<span class="TRSB">B</span>'
		if self._mXout.strip():
			if int(self._mXout) > 1:
				return f'<span class="TRSX">A/B × {self._mXout}</span>'
			else:
				return '<span class="TRSX">A/B</span>'
		if self._mTBDout.strip():
			if int(self._mTBDout) > 1:
				return f'<span class="TRSTBD">??? × {self._mTBDout}</span>'
			else:
				return '<span class="TRSTBD">???</span>'
		return ''

	def hMIDI_other(self):
		bits = []
		if self._musb and 'a' in self._musb.lower():
			bits.append('USB-A')
		if self._musb and 'b' in self._musb.lower():
			bits.append('USB-B')
		if self._musb and 'c' in self._musb.lower():
			bits.append('USB-C')
		if self._mdin:
			bits.append('DIN')
		return ' '.join(bits)

	def hNotes(self):
		if not self._notes:
			return ''
		lines = self._notes.split(';')
		h = '<ul>'
		for line in lines:
			h += f'<li>{line}</li>'
		h += '</ul>'
		return h



with open('midi-modules.csv',encoding='utf-8') as csvfile:

	reader = csv.DictReader(csvfile)

	for row in reader:

		# first row is special-contains our column display titles
		if row['product'] == 'Product':
			columnDisplayNames = row

		else:

			modules.append(Module(row))

print(f'Loaded {len(modules)} module entries')


# roles (deliberately ordered)
roles = ['utility', 'sequencer', 'voice', 'filter', 'effects', 'video']
rolesFound = set([])
for m in modules:
	for r in m.roles():
		rolesFound.add(r)
for r in rolesFound:
	if r not in roles:
		print(f'WARNING: role {r} missing from the sorted roles list—add or correct')

# compile stats
TRS_year_stats = {}
for m in modules:
	if m._mAin.strip() or m._mAout.strip() and m._year:
		logStat(m._year,'A')
	elif m._mBin.strip() or m._mBout.strip() and m._year:
		logStat(m._year,'B')
	elif m._mXin.strip() or m._mXout.strip() and m._year:
		logStat(m._year,'X')

TRS_growth = {
	'y':[],
	'A':[],
	'B':[],
	'X':[],
	't':[],
}
a = b = x = 0
for y in sorted(TRS_year_stats.keys()):
	d = TRS_year_stats[y]
	a += d['A']
	b += d['B']
	x += d['X']
	TRS_growth['y'].append(y)
	TRS_growth['A'].append(a)
	TRS_growth['B'].append(b)
	TRS_growth['X'].append(x)
	TRS_growth['t'].append(a + b + x)
	# s += f'''{y}: {d['A']} - {d['B']} - {d['X']}<br>'''


################ START GRAPH ################
xgrid = 60
ygrid = 5
xoffset = 40
yoffset = 40
totYears = len(TRS_growth['y'])
graphWidth = totYears * xgrid + xoffset
maxModules = TRS_growth['t'][-1]
graphHeight = maxModules * ygrid + yoffset + (ygrid * 5)
hsvg = f'''<svg viewBox="0 0 {graphWidth} {graphHeight}" class="graph">'''

# == Type A
coords = []
for i in range(totYears):
	coords.append(f'''{xoffset + i*xgrid},{graphHeight - yoffset-TRS_growth['A'][i]*ygrid}''')
hsvg += f'''
  <polyline
     fill="none"
     stroke="var(--TRSA-color)"
     stroke-width="2"
     points="{' '.join(coords)}"/>'''

# == Type B
coords = []
for i in range(totYears):
	coords.append(f'''{xoffset + i*xgrid},{graphHeight - yoffset-TRS_growth['B'][i]*ygrid}''')
hsvg += f'''
  <polyline
     fill="none"
     stroke="var(--TRSB-color)"
     stroke-width="2"
     points="{' '.join(coords)}"/>'''

# == Type X
coords = []
for i in range(totYears):
	coords.append(f'''{xoffset + i*xgrid},{graphHeight - yoffset-TRS_growth['X'][i]*ygrid}''')
hsvg += f'''
  <polyline
     fill="none"
     stroke="var(--TRSX-color)"
     stroke-width="2"
     points="{' '.join(coords)}"/>'''

# == TOTAL
coords = []
for i in range(totYears):
	coords.append(f'''{xoffset + i*xgrid},{graphHeight - yoffset-TRS_growth['t'][i]*ygrid}''')
hsvg += f'''
  <polyline
     fill="none"
     stroke="black"
     stroke-width="2"
     points="{' '.join(coords)}"/>'''


hsvg += f'''<g class="grid y-grid"><line x1="{xoffset}" x2="{xoffset}" y1="{graphHeight - yoffset}" y2="0"></line></g>'''
hsvg += f'''<g class="grid x-grid"><line x1="{xoffset}" x2="{graphWidth}" y1="{graphHeight - yoffset}" y2="{graphHeight - yoffset}"></line></g>'''
hsvg += f'''<g class="labels x-labels">'''
for i in range(totYears):
	hsvg += f'''<text x="{xoffset + i*xgrid}" y="{graphHeight - yoffset + 20}">{TRS_growth['y'][i]}</text>'''
hsvg += '</g>'
hsvg += f'''<g class="labels y-labels">'''
for i in range(5, maxModules + 10, 5):
	hsvg += f'''<text x="{xoffset - 10}" y="{graphHeight - yoffset - i * ygrid}">{i}</text>'''
hsvg += '</g>'

hsvg += '''</svg>'''
################ END GRAPH ################

s = html_top

s += '<h2>Growth of MIDI Eurorack</h2>'
s += '<p>The graph below summarizes the number of modules with TRS MIDI support (black line), and the numbers specifically for <strong style="color: var(--TRSA-color);">TRS-A</strong>, <strong style="color: var(--TRSB-color);">TRS-B</strong> and modules designed to accommodate <strong style="color: var(--TRSX-color);">both TRS-A and TRS-B (automatically or manually)</strong>. The graph omits modules of (as yet) unknown TRS type, and modules that only offer DIN or USB MIDI.</p>'
s += hsvg

s += '<h2>Modules</h2>'
s += '<table>'
for role in roles:

	s += f'<tr><td colspan="4" class="tablesection"><h3>{role.capitalize()}</h3></td></tr>'


	s += '<tr><th>Product</th><th>TRS In</th><th>TRS Out</th><th>Other MIDI</th><th>Notes</th></tr>'
	for p in [x for x in modules if role in x.roles()]:
		s += '<tr>'
		s += f'<td class="left">{p.hProduct()}</td>'
		s += f'<td>{p.hMIDI_in()}</td>'
		s += f'<td>{p.hMIDI_out()}</td>'
		s += f'<td>{p.hMIDI_other()}</td>'
		s += f'<td class="left">{p.hNotes()}</td>'
		s += '</tr>'
s += '</table>'

s += html_bottom



f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


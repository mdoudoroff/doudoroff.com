#!/usr/bin/env python
# encoding: utf-8

import json, csv


html_top = u'''
<html>
<head>
	<meta charset="utf-8">
	<title>Eurorack Pitch + Gate Sequencer Module Comparison</title>
</head>
<style>
body {
	max-width: 1600px;
	margin: 1em;
}
a {text-decoration:none;}
a:hover {color:red;text-decoration:underline;}
a:visited {color:blue;}
img {
	width: 100%;
	margin: 1em 0;
}
.red {color:red;}
.green {color:green;}
.gray {color:gray;}
table {border-collapse: collapse;}
td, th {text-align:center;padding:0.25em 1em;border-bottom:1px solid #eee;}
td.left, th.left {text-align:left;}
td ul { padding-left: 20px; -webkit-padding-start: 20px; }
</style>
<body>

<h1>Eurorack Pitch + Gate Sequencer Module Comparison</h1>

<p>Martin Doudoroff<br />
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<!--<p>Related discussion thread: <a href="https://muffwiggler.com/forum/viewtopic.php?t=154186"><em>stereo mixer module comparison</em> (MuffWiggler forum)</a></p>-->

<p>2017-06-18 Rough draft</p>
<p>2017-06-19 Various tweaks and additions</p>

<h2>Introduction</h2>

<p>There are many sequencer-related modules for Eurorack. This comparison is rather picky, <strong>focusing on heavier-duty melodic-oriented designs with fairly complete gate sequencing ability</strong>.
This comparison can never be more than a starting place for further research—most of the modules are amongst the most complex in Eurorack and they are extremely hard to compare fairly and accurately—their design
bias toward different priorities and “process”. Most of these modules have tons of features that I cannot even begin to describe here. Do your homework. <strong>Sequencer are intensely personal tools.</strong></p>

<p>The UI Style column is an attempt to broadly categorize the operational styles of these different designs:</p>

<ul>
	<li><strong>Classic</strong> means you have dedicated, separate pots/sliders for each step, yielding an operational style comparable to the vintage analog sequencers of yore</li>
	<li><strong>x0x</strong> generally implies a row of light-up buttons for choosing a step and a row of buttons similar to an octave of a piano keyboard for choosing notes</li>
	<li><strong>Cirklon-ish</strong> is a more modal push-button UI, often with lots of menus/remapping of the buttons</li>
	<li><strong>hybrid</strong> means there are pots/sliders for each step, but they get used for different modes and often are not accurately representing state</li>
	<li><strong>per-step window</strong> means a form-like interface that focuses on step parameters with no overall reperesentation of the sequence available</li>
	<li><strong>GUI</strong> means an interface focused on a computer-type display, generally with lots of menus</li>
	<li><strong>Tracker</strong> means a spreadsheet-like interface</li>
</ul>

<p>The <strong>Steps (UI basis/max pattern length)</strong> column describes the number of steps the interface facilitates for editing at one time versus the (max) number of steps in a pattern. 
This provides a clue about how “playable” or how much “windowing” is going on while navigating the sequence.</p>

<h2>Comparison</h2>

'''

html_bottom = u'''

<h2>External and partially-external alternatives with direct Eurorack integration</h2>
<p>There are, of course, a zillion MIDI solutions available for Eurorack and related ways to control one’s rack. 
These are a selection of alternatives to either a heavy-duty sequencer module as per above, or a straight-up MIDI-style approach:</p>
<ul>
<li><a href="https://www.arturia.com/beatstep-pro/overview">Arturia Beatstep Pro</a> (direct patch)</li>
<li><a href="https://www.arturia.com/products/keystep/overview">Arturia Keystep</a> (direct patch)</li>
<li><a href="http://www.monome.org/docs/modular/ansible/">Monome Ansible w/Grid or Arc</a></li>
<li><a href="http://www.monome.org/docs/modular/teletype/">Monome Teletype</a></li>
<li><a href="https://koma-elektronik.com/?product=komplex-sequencer">Koma Komplex</a></li>
<li><a href="http://www.korg.com/us/products/dj/sq_1/">Korg SQ-1</a> (direct patch)</li>
<li><a href="http://polyend.com/seq-sequencer/">Polyend SEQ</a> (w/Poly MIDI-to-CV interface module)</li>
<li><a href="https://www.sequentix.com">Sequentix Cirklon</a> (w/CV output module)</li>
<li><a href="https://www.socialentropy.com/engine/?page_id=346">Social Entropy Engine</a> (w/CV expander)</li>
</ul>

<h2>Further alternatives</h2>
<p>In addition, these modules don’t quite belong in the above comparison but have been pointed out as being of potential interest:</p>
<ul>
<li><a href="https://www.modulargrid.net/e/bastl-instruments-popcorn-">Bastl Popcorn</a> (clever eight step sequencer)</li>
<li><a href="https://www.modulargrid.net/e/catalyst-audio-time-s-arrow">Catalyst Audio Time’s Arrow</a> (random melody-focused 16-step sequencer)</li>
<li><a href="https://www.modulargrid.net/e/division-6-mattson-sq816-sequencer">Division6 Mattson SQ816</a> (classic 8-step design)</li>
<!--<li><a href="https://www.modulargrid.net/e/doepfer-a-155v">Doepfer A-155v</a> (classic sequencer design, but without full gate features)</li>-->
<li><a href="https://www.modulargrid.net/e/make-noise-rene">Make Noise René</a> (1 track, 16 step quantizable with gate processing, but not full gate features)</li>
<li><a href="https://www.modulargrid.net/e/malekko-heavy-industry-voltage-block">Malekko Heavy Industries Voltage Block</a> (8 independent tracks of quantizable 16-step CV sequencing, but no gates)</li>
<li><a href="https://www.modulargrid.net/e/other-unknown-ornament-crime-simple-msw-panel">Ornament & Crime</a> (teensy-based module with various sequencer programs)</li>
<!--<li><a href="https://www.modulargrid.net/e/rossum-electro-music-control-forge">Rossum Electro-Music Control Forge</a> (arbitrary function generator with extensive step transition features that can be operated as an 8-step sequencer)</li>-->
<li><a href="https://www.modulargrid.net/e/other-unknown-electro-music-klee-sequencer">San Pedro Labs Klee Sequencer</a> (teensy-based module with various sequencer programs)</li>
<li><a href="https://www.modulargrid.net/e/twisted-electrons-cells">Twisted Electron Cells</a> (compact grid-like, dual sequencer)</li>
<li><a href="https://www.modulargrid.net/e/tiptop-audio-z8000-mk2">Tiptop Z8000 Mk2</a> (novel cv-only grid-based sequencer with many outputs)</li>
</ul>

<p style="text-align:center;">• • •</p>

</body>
</html>
'''

def klassForAny(val):
	klasses = []
	if val.lower() in ('0','tbd'):
		klasses.append('gray')
	return ' '.join(klasses)

def valueForproduct(row):
	h = u'<strong>%s</strong>' % row['product']
	h += '<br /><small>'
	if row['_mgurl'].strip():
		h += u'<br /><a href="%s" target="_blank">Modular Grid &gt;</a>' % row['_mgurl']
	if row['_website'].strip():
		h += u'<br /><a href="%s" target="_blank">Web site &gt;</a>' % row['_website']
	h += '</small>'
	return h

def klassForproduct(val):
	return 'left'

def klassFornotes(val):
	return 'left'

def klassForheadphone(val):
	if val.lower().find('yes') > -1:
		return 'green'
	elif val.lower().find('no') > -1:
		return 'red'
	else:
		return ''

def klassForshippingstatus(val):
	if val.lower().find('yes') > -1:
		return 'green'
	elif val.lower().find('no') > -1:
		return 'red'
	else:
		return ''

def klassForpic(val):
	return 'pic'

def valueForpic(row):
	if row['pic'].strip():
		width = 0
		try:
			width = int(row['hp']) * 5
			height = 26.2 * 5
		except:
			pass
		return '''<a href="gfx/%s"><img src="gfx/%s" style="width:%spx;height:%spx;cursor:zoom-in;" /></a>''' % (row['pic'],row['pic'],width,height)
	else:
		return '(need photo)'

def valueFornotes(row):
	vals = row['notes'].split(';')
	bits = ['<ul>']
	for val in vals:
		if val.strip():
			bits.append('<li>%s</li>' % val)
	bits.append('</ul>')
	return '\n\t'.join(bits)

def valueFortrack_outs(row):
	vals = row['track_outs'].split(',')
	return u'<br />'.join(vals)

rows = []
columnDisplayNames = {}

with open('sequencers-data.csv') as csvfile:

	reader = csv.DictReader(csvfile)

	for row in reader:

		# first row is special-contains our column display titles
		if row['product'] == 'Product':
			columnDisplayNames = row
		else:
			columns = []
			for fieldname in reader.fieldnames:
				if not fieldname.find('_')==0:
					v = row[fieldname].decode('utf-8')
					try:
						v = locals()["valueFor%s" % fieldname](row)
					except:
						pass
					klass = ''
					try:
						klass = locals()["klassFor%s" % fieldname](row[fieldname])
					except:
						klass = klassForAny(row[fieldname])
					columns.append('<td class="%s">%s</td>' % (klass,v))


			rows.append(columns)

s = html_top


s += '<table>' 

s += '<tr>'
for fieldname in reader.fieldnames:
	if not fieldname.find('_')==0:
		klass = ''
		try:
			klass = locals()["klassFor%s" % fieldname](fieldname)
		except:
			klass = klassForAny(fieldname)

		s += '<th class="%s">%s</th>' % (klass,columnDisplayNames[fieldname])
s += '</tr>'

for row in rows:
	s += u'\n<tr>'
	s += u'\n\t'.join(row)
	s += u'\n</tr>'
s += u'\n</table>'

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


#!/usr/bin/env python
# encoding: utf-8

import json, csv, sys


html_top = u'''
<html>
<head>
	<meta charset="utf-8">
	<title>Eurorack Sampler Module Comparison</title>
</head>
<style>
body {
	max-width: 1600px;
	margin: 1em;
	font-family: Georgia, serif;
	font-size: 16px;
}
p, li {
	max-width: 50rem;
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
	margin: 1em 0;
}
.red {color:red;}
.green {color:green;}
.gray {color:gray;}
.nope {background-color:#eee;}
table {border-collapse: collapse;font-size: 85%;}
td, th {text-align:center;padding:0.25em 1em;border-bottom:1px solid #eee;}
td.left, th.left {text-align:left;}
td ul { padding-left: 20px; -webkit-padding-start: 20px; }
th { background-color: #eee; color: #666; }

.notes { min-width: 15em; }

.collapsed {display: none;}

nav { 
	background: #eee; 
	padding: 0.25em;
	font-family: Helvetica, sans-serif;
	border-bottom: 2px solid #666;
	}

nav ul {  }
nav ul li { list-style: none; display: inline-block; margin-right: 1em; }

</style>
<body>

<nav>
<ul>
	<li>Eurorack Comparisons:</li>
	<li><a href="//doudoroff.com/mixers/">Stereo Mixer Modules</a></li>
	<li><a href="//doudoroff.com/sequencers/">Pitch &amp; Gate Sequencers</a></li>
	<li><strong>Sampler Modules</strong></li>
</ul>
</nav>

<h1>Eurorack Sampler Module Comparison</h1>

<p>Martin Doudoroff<br />
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>Related discussion thread: <a href="https://www.muffwiggler.com/forum/viewtopic.php?p=3120088"><em>Eurorack sampler comparison</em></a> (MuffWiggler forum)</p>

<h4>Latest</h4>
<p class="updates">2019-09-19 added (tentatively) Modcan CV Record, Supercell, Microcell and ISD, plus more edits<br />
2019-09-17 added (tentatively) Clouds, more edits/augmentations<br />
2019-09-16 added (nascent) latency column, corrections<br />
2019-09-15 added 4ms DLD; many corrections and details<br />
2019-09-14 added VPME, Doepfer and Ladik modules, ongoing basic corrections<br />
2019-09-13 added Mungo g0, filled in more cells<br />
2019-08-26 super rough first draft<br />
<span id="additionalUpdates" class="collapsed">
</span>
<a id="updatesToggle" onclick="toggleAdditionalUpdates();" href="javascript:void(0);">Show full revision history</a>
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

<h2>Introduction</h2>

<p>This is an exhaustive comparison grid for Eurorack sampler options. The goal is to provide enough information to identify and narrow the options that interest you.</p>

<p>Not all modules that employ “sampling techniques” are included here; for example, digital delays also sample audio, but this is not a digital delay comparison. Only some of these modules can record/capture audio, but they can all replay audio on demand.</p>

<p>Eurorack samplers generally fall into—or overlap—five main types:</p>

<ul>
	<li><strong>file player</strong>: these play audio data files, typically by triggers or gate, typically with an emphasis on 1v/o pitch control and enveloping; they may or may not have recording functionality</li>
	<li><strong>audio buffer</strong>: these devices focus on capturing (recording) and manipulating audio (snippets) in rudimentary ways, such as modulating sample rates, to produce delay or wavetable-like effects; <em>these are more electronic than algorithmic</em></li>
	<li><strong>virtual tape</strong>: these use DSP techniques to play (typically longer) segments of audio in the style of a tape recorder, with an emphasis on variable speed, direction and edits (splices)</li>
	<li><strong>looper</strong>: these focus on simultaneously recording and playing (typically longer) ephemeral loops of audio, much like a guitar pedal looper</li>
	<li><strong>granular</strong>: these capture (typically ephemeral) audio and use DSP techniques to derive new audio through granular techniques</li>
</ul>

<p>Many modules do some or all of the above, but there’s nearly always some sort of bias built into the user interface.</p>

<h2>Comparison</h2>

'''

html_bottom = u'''

<h2>Other modules of interest</h2>
<p>These don’t really fit in the above comparison, but are probably worth being aware of.</p>
<ul>
<!--<li><a href="https://www.modulargrid.net/e/noise-reap-isd-sampler">Noise Reap ISD Sampler</a> (teensy-based DIY hackable platform by mxmxmx)</li>-->
<li><a href="https://www.modulargrid.net/e/other-unknown-eurotrash-mkii">Eurotrash Mk II dual mono WAV player</a> (teensy-based DIY hackable platform by mxmxmx)</li>
<li><a href="https://www.modulargrid.net/e/analogue-systems-rs-290">Analogue Systems RS-290 Sampler/Delay</a> (venerable, nominally-Eurorack-compatible delay/sample/effect unit of the “audio buffer” sort)</a></li>
<!--<li><a href="https://www.modulargrid.net/e/4ms-company-dual-looping-delay">4ms Dual Looping Delay</a> (delay with some sampler-esque capabilities)</li>-->
<li><a href="https://www.modulargrid.net/e/4ms-company-wav-recorder">4ms WAV Recorder</a></li>
<!--<li><a href="https://www.modulargrid.net/e/grayscale-supercell-aluminum-panel">Grayscale Supercell</a> (granular processor)</li>-->
<!--<li><a href="https://www.modulargrid.net/e/mutable-instruments-clouds">Mutable Instruments Clouds</a> (granular processor)</a></li>-->
<li><a href="https://www.modulargrid.net/e/instruo-arbhar">Instruo Arbhar</a> (granular)</a> (granular processor)</li>
</ul>

<h2>Non-modular alternatives</h2>
<ul>
<li><a href="https://1010music.com/blackbox-a-compact-sampling-studio-press-release">1010 Music Blackbox</a></li>
<li><a href="https://www.elektron.se/products/digitakt/">Elektron Digitakt</a></li>
<li><a href="https://www.elektron.se/products/octatrack-mkii/">Elektron Octatrack MKII</a></li>
<li><a href="https://synthstrom.com/product/deluge/">Synthstrom Deluge</a></li>
<li><a href="https://teenage.engineering/products/op-1">Teenage Engineering OP-1</a></li>
<li><a href="https://teenage.engineering/products/op-z">Teenage Engineering OP-Z</a></li>
<li><a href="https://teenage.engineering/products/po">Teenage Engineering PO-33</a></li>
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
	h = u'<strong>%s</strong>' % row['product'].decode('utf-8')
	if row['_year'].strip():
		h += u'<br />%s' % row['_year']
	h += u'<br /><small>'
	if row['_hp'].strip():
		h += u'<br />%s HP' % row['_hp']
	if row['_mgurl'].strip():
		h += u'<br /><a href="%s" target="_blank">Modular Grid &gt;</a>' % row['_mgurl'].decode('utf-8')
	if row['_website'].strip():
		h += u'<br /><a href="%s" target="_blank">Web site &gt;</a>' % row['_website']
	h += u'</small>'
	return h

def klassForproduct(val):
	return 'left'

def klassFornotes(val):
	return 'left notes'

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
			width = int(row['_hp']) * 5
			height = 26.2 * 5
		except:
			pass
		return '''<a href="gfx/%s"><img src="gfx/%s" style="width:%spx;height:%spx;cursor:zoom-in;" /></a>''' % (row['pic'],row['pic'],width,height)
	else:
		return '(need photo)'

def valueFornotes(row):
	vals = row['notes'].decode('utf-8').split(';')
	bits = ['<ul>']
	for val in vals:
		if val.strip():
			bits.append('<li>%s</li>' % val)
	bits.append('</ul>')
	return '\n\t'.join(bits)

def valueForrecording(row):
	v = row['recording'].decode('utf-8')
	if not v.strip():
		return u' '
	return v

def valueFormaxlength(row):
	v = row['recording'].decode('utf-8')
	if not v.strip():
		return u''
	return row['maxlength'].decode('utf-8')

def valueForclockedrec(row):
	v = row['recording'].decode('utf-8')
	if not v.strip():
		return u' '
	return row['clockedrec'].decode('utf-8')


def klassForrecording(val):
	if not val:
		return 'nope'
	return ''

def klassFormaxlength(val):
	if not val:
		return 'nope'
	return ''

def klassForclockedrec(val):
	if not val:
		return 'nope'
	return ''

rows = []
columnDisplayNames = {}

with open('samplers.csv') as csvfile:

	reader = csv.DictReader(csvfile)

	for row in reader:

		# first row is special-contains our column display titles
		if row['product'] == 'Product':
			columnDisplayNames = row
		else:
			columns = []
			for fieldname in reader.fieldnames:
				if not fieldname.find('_')==0:
					try:
						v = locals()["valueFor%s" % fieldname](row)
					except:
						v = row[fieldname].decode('utf-8')
					klass = ''
					try:
						klass = locals()["klassFor%s" % fieldname](row[fieldname])
					except:
						klass = klassForAny(row[fieldname])
					columns.append('<td class="%s">%s</td>' % (klass,v))


			rows.append(columns)

# print rows

# build th row
s = u''
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
table_header_row = s


s = html_top


s += '<table>' 

# s += '<tr>'
# for fieldname in reader.fieldnames:
# 	if not fieldname.find('_')==0:
# 		klass = ''
# 		try:
# 			klass = locals()["klassFor%s" % fieldname](fieldname)
# 		except:
# 			klass = klassForAny(fieldname)

# 		s += '<th class="%s">%s</th>' % (klass,columnDisplayNames[fieldname])
# s += '</tr>'

for row in rows:

	if rows.index(row)%4==0:
		s += table_header_row

	s += u'\n<tr>'
	try:
		s += u'\n\t'.join(row)
	except:
		print row
		sys.exit(1)
	s += u'\n</tr>'
s += u'\n</table>'

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()

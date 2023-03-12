#!/usr/bin/env python3
# encoding: utf-8

import json, csv, sys

if sys.version_info[0] != 3:
    sys.exit("This script requires Python version 3")

html_top = '''
<html>
<head>
	<meta charset="utf-8">
	<title>Eurorack Sampler Module Comparison</title>
</head>
<style>
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
	margin: 1em 0;
}
.main {	padding: 1em; }
.red {color:red;}
.green {color:green;}
.gray {color:gray;}
table {border-collapse: collapse;font-size: 85%;}
td, th {text-align:center;padding:0.25em 1em;border-bottom:1px solid #eee;}
td.left, th.left {text-align:left;}
td.notes {text-align: left;}
td ul { padding-left: 20px; -webkit-padding-start: 20px; }
th { 
	color: #666; position: sticky; top: 0px; 

	background-color: rgba(200,200,200,0.9);
	@supports ((-webkit-backdrop-filter: none) or (backdrop-filter: none)) {
		background-color: rgba(200, 200, 200, .5);
		-webkit-backdrop-filter: blur(5px);
		backdrop-filter: blur(5px);
	}

}
.notes { min-width: 15em; }
.collapsed {display: none;}
td.left { 
	position: sticky; 
	left: 0px; 
	z-index: 1;

	background-color: rgba(225,225,225,0.9);
	@supports ((-webkit-backdrop-filter: none) or (backdrop-filter: none)) {
		background-color: rgba(255, 255, 255, .5);
		-webkit-backdrop-filter: blur(5px);
		backdrop-filter: blur(5px);
	}
}
th.left {
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

table.players .nope { display: none; }

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


</style>
<body>

<nav id="comparisonSwitcher">
<a href="/mixers/">Stereo Mixers</a>
<a href="/sequencers/">Pitch+Gate Sequencers</a>
<strong>Samplers</strong>
<a href="/quantizers/">Quantizers</a>
</nav>

<div class="main">

<h1>Eurorack Sampler Module Comparison</h1>

<p>Martin Doudoroff<br />
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>Related discussion thread: <a href="https://www.modwiggler.com/forum/viewtopic.php?p=3120088"><em>Eurorack sampler comparison</em></a> (ModWiggler forum)</p>

<h4>Latest</h4>
<p class="updates">
2022-07-16 added Mutable Instruments Beads<br />
2022-05-31 minor updates<br />
2022-05-29 added ADDAC112 and Miso Cornflakes<br />
2021-07-28 added Endorphin.es Two of Cups<br />
2020-06-04 added 2hp Loop; additional updates<br />
2020-04-25 added Bitbox Mk2 and Bitbox Micro<br />
2020-04-24 added Disting EX<br />
<span id="additionalUpdates" class="collapsed">
2020-04-16 errata & updates<br />
2020-02-28 added Squarp Rample<br />
2019-09-27 errata<br />
2019-09-25 clarified some wording<br />
2019-09-24 kicked the DLD back down to the bottom of the page; other corrections<br />
2019-09-22 by request, broke table in two: one for those that capture audio, and one for those that just play<br />
2019-09-19 added (tentatively) Modcan CV Record, Supercell, Microcell and ISD, plus more edits<br />
2019-09-17 added (tentatively) Clouds, more edits/augmentations<br />
2019-09-16 added (nascent) latency column, corrections<br />
2019-09-15 added 4ms DLD; many corrections and details<br />
2019-09-14 added VPME, Doepfer and Ladik modules, ongoing basic corrections<br />
2019-09-13 added Mungo g0, filled in more cells<br />
2019-08-26 super rough first draft<br />

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

'''

html_bottom = '''

<h2>Other modules of interest</h2>
<p>These don’t really fit in the above comparison, but are probably worth being aware of.</p>
<ul>
<li><a href="https://www.modulargrid.net/e/other-unknown-eurotrash-mkii">Eurotrash Mk II dual mono WAV player</a> (teensy-based DIY hackable platform by mxmxmx)</li>
<li><a href="https://www.modulargrid.net/e/analogue-systems-rs-290">Analogue Systems RS-290 Sampler/Delay</a> (venerable, nominally-Eurorack-compatible delay/sample/effect unit of the “audio buffer” sort)</a></li>
<li><a href="https://www.modulargrid.net/e/4ms-company-dual-looping-delay">4ms Dual Looping Delay</a> (delay with some sampler-esque capabilities)</li>
<li><a href="https://www.modulargrid.net/e/4ms-company-wav-recorder">4ms WAV Recorder</a></li>
<li><a href="https://www.modulargrid.net/e/alyseum-record">Alyseum Record</a></li>
<li><a href="https://www.modulargrid.net/e/patching-panda-ephemere-silver-panel">Patching Panda Ephemere (cv recorder)</a></li>
</ul>

<h2>Non-modular alternatives</h2>
<ul>
<li><a href="https://1010music.com/blackbox-a-compact-sampling-studio-press-release">1010 Music Blackbox</a></li>
<li><a href="https://www.elektron.se/products/digitakt/">Elektron Digitakt</a></li>
<li><a href="https://www.elektron.se/products/octatrack-mkii/">Elektron Octatrack MKII</a></li>
<li><a href="https://synthstrom.com/product/deluge/">Synthstrom Deluge</a></li>
<li><a href="https://www.tastychips.nl/product/gr-1-granular-synthesizer/">Tasty Chips GR-1</a></li>
<li><a href="https://teenage.engineering/products/op-1">Teenage Engineering OP-1</a></li>
<li><a href="https://teenage.engineering/products/op-z">Teenage Engineering OP-Z</a></li>
<li><a href="https://teenage.engineering/products/po">Teenage Engineering PO-33</a></li>
</ul>


<p style="text-align:center;">• • •</p>

</div><!-- end div.main -->

<footer>
<nav>
<div class="navrail">
<ul>
	<li style="border-bottom: 2px solid gray;">Comparison guides</li>
	<li><a href="//doudoroff.com/mixers/">Stereo Mixer Modules</a></li>
	<li><a href="//doudoroff.com/sequencers/">Pitch &amp; Gate Sequencers</a></li>
	<li><strong>Sampler Modules</strong></li>
	<li><a href="//doudoroff.com/quantizers/">Quantizer Modules</a></li>
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

def klassForAny(val):
	klasses = []
	if val.lower() in ('0','tbd'):
		klasses.append('gray')
	return ' '.join(klasses)

def valueForproduct(row):
	h = '<strong>%s</strong>' % row['product']
	if row['_year'].strip():
		h += '<br />%s' % row['_year']
	h += '<br /><small>'
	if row['_hp'].strip():
		h += '<br />%s HP' % row['_hp']
	if row['_mgurl'].strip():
		h += '<br /><a href="%s" target="_blank">Modular Grid &gt;</a>' % row['_mgurl']
	if row['_website'].strip():
		h += '<br /><a href="%s" target="_blank">Web site &gt;</a>' % row['_website']
	h += '</small>'
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
	vals = row['notes'].split(';')
	bits = ['<ul>']
	for val in vals:
		if val.strip():
			bits.append('<li>%s</li>' % val)
	bits.append('</ul>')
	return '\n\t'.join(bits)

def valueForrecording(row):
	v = row['recording']
	if not v.strip():
		return ' '
	return v

def valueFormaxlength(row):
	v = row['recording']
	if not v.strip():
		return ''
	return row['maxlength']

def valueForclockedrec(row):
	v = row['recording']
	if not v.strip():
		return ' '
	return row['clockedrec']


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
rows_players = []
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
						v = row[fieldname]
					klass = ''
					try:
						klass = locals()["klassFor%s" % fieldname](row[fieldname])
					except:
						klass = klassForAny(row[fieldname])
					columns.append('<td class="%s">%s</td>' % (klass,v))


			if row['recording'].strip():
				rows.append(columns)
			else:
				rows_players.append(columns)

# print rows

# build th row
s = []

for fieldname in reader.fieldnames:
	if not fieldname.find('_')==0:
		klass = ''
		try:
			klass = locals()["klassFor%s" % fieldname](fieldname)
		except:
			klass = klassForAny(fieldname)

		s.append('<th class="%s">%s</th>' % (klass,columnDisplayNames[fieldname]))

table_header_row = ''.join(['<tr>'] + s + ['</tr>'])
table_player_header_row = ''.join(['<tr>'] + s[:3]+ s[6:] + ['</tr>'])

s = html_top

s += '<h2>Samplers (with recording/capture)</h2>'
s += '<table>' 

for row in rows:

	# if rows.index(row)%4==0:
	if rows.index(row)==0:
		s += table_header_row

	s += '\n<tr>'
	try:
		s += '\n\t'.join(row)
	except:
		print(row)
		sys.exit(1)
	s += '\n</tr>'
s += '\n</table>'

s += '<h2>Sample Players (no recording/capture)</h2>'
s += '<table class="players">' 

for row in rows_players:

	# if rows_players.index(row)%4==0:
	if rows_players.index(row)==0:
		s += table_player_header_row

	s += '\n<tr>'
	try:
		s += '\n\t'.join(row)
	except:
		print(row)
		sys.exit(1)
	s += '\n</tr>'
s += '\n</table>'

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


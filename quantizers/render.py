#!/usr/bin/env python3
# encoding: utf-8

import json, csv, decimal, sys

if sys.version_info[0] != 3:
    sys.exit("This script requires Python version 3")

html_top = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>Eurorack Quantizer Comparison</title>
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
		}
		.notes { min-width: 15em; }
		.collapsed {display: none;}
		td.left { 
			position: sticky; 
			left: 0px; 
			z-index: 1;

			background-color: rgba(225,225,225,0.9);
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
</head>
<body>

<nav id="comparisonSwitcher">
<a href="/mixers/">Stereo Mixers</a>
<a href="/sequencers/">Pitch+Gate Sequencers</a>

<strong>Quantizers</strong>
<a href="/midi/">MIDI Eurorack</a>
</nav>


<div class="main">


<h1>Eurorack Pitch Quantizer Module Comparison</h1>

<p>Martin Doudoroff<br>
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>This is a pretty exhaustive and up-to-date basic comparison of all your pitch quantizer module options for Eurorack. Some additional tools of potential interest are listed at the bottom.</p>

<p>Related discussion thread: <a href="https://www.modwiggler.com/forum/viewtopic.php?t=222110"><em>Eurorack pitch quantizer comparison</em> (ModWiggler forum)</a></p>


<h4>Latest</h4>
<p class="updates">
2024-05-15 added Instruo Dail<br>
2024-04-09 added dnipro qTone<br>
2023-06-30 added Tenderfoot QQ2<br>
2023-05-01 updates and corrections<br>
2022-04-09 added Ladik Q-040 and Blue Lantern Quad Mk2<br>
2022-01-20 added Flame Tame Machine (historical)<br>
2022-01-19 added Bastl 1983<br>
<span id="additionalUpdates" class="collapsed">
2020-10-31 added Monome Crow and Der Mann mit der Maschine DROID<br>
2020-02-19 added Shakmat Bard Quartet<br>
2020-02-19 added Tenderfoot Quad Quantizer<br>
2019-10-22 added Kassutronics Quantizer<br>
2019-09-29 errata<br>
2019-09-29 added Mungo w0<br>
2019-09-26 added more performance data from producers<br>
2019-09-25 errata<br>
2019-09-24 reworked transposition column, errata, first stab at accuracy column<br>
2019-09-23 rough draft<br>
</span>
<a id="updatesToggle" onclick="toggleAdditionalUpdates();" href="javascript:void(0);">Show full revision history</a>
</p>

<h4>Notes</h4>

<p>The <strong>Channels</strong> column is the number of input voltages the unit will quantize for you. The <strong>Derived Parts</strong> describes the <em>additional</em> outputs that some units will create for you (intervals, chords, arpeggios, etc.)</p>

<p>The <strong>Nominal accuracy</strong> column is a simple calculation of the resolution of the DAC against the output range of the quantizer. There are many other factors that may relate to the accuracy of a quantizer, but this is a baseline. Note that a cent is 0.83 millivolts, so quantizers above that value lack the resolution to be accurate within a cent.</p>

<p>As with all sophisticated modules, the devil is in the details. In particular, <em>how</em> each of these work is beyond the scope of this comparison, but critical for your workflow. All this comparison can do is help you survey the options and identify the modules you need to research more carefully. (You may find that some of these modules are pretty whacky.)</p>

<p>If you’re looking for microtonal quantization, use your browser’s search feature (usually command+f/ctrl+f) to find “micro” on this page.</p>


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

<p>In addition, these modules don’t really belong in the above comparison but have been pointed out as being of potential interest:</p>
<ul>
<li><a href="https://www.modulargrid.net/e/cycle-instruments-tetrachords">Cycle Instruments Tetrachord</a> (four part arp/chord melody mill with sophisticated macro and cv control)</li>
<li><a href="https://www.modulargrid.net/e/elektrofon-klang">Elektrofon Klang</a> (four part chord generator)</li>
<li><a href="https://www.modulargrid.net/e/qu-bit-electronix-chord">Qu-bit Chord</a> (chord-generating quad-oscillator with parametric front-end)</li>
<li><a href="https://www.modulargrid.net/e/qu-bit-electronix-chord-v2">Qu-bit Chord 2</a> (chord-generating quad-oscillator with parametric front-end)</li>
<li><a href="https://www.modulargrid.net/e/flame-4vox">Flame 4VOX</a> (chord-generating quad sequencer)</li>
<li><a href="https://www.modulargrid.net/e/mutable-instruments-plaits">Mutable Instrument Plaits</a> (oscillator with chord generator)</li>
<li><a href="https://www.modulargrid.net/e/mutable-instruments-braids-2015">Mutable Instrument Braids</a> (oscillator with chord generator)</li>
<li><a href="https://www.modulargrid.net/e/bastl-instruments-popcorn-">Bastl Instruments Popcorn</a> (sequencer that can be used as a quantizer)</li>
<li><a href="https://www.modulargrid.net/e/mutable-instruments-marbles">Mutable Instruments Marbles</a> (random source that can be quantized to a user-supplied voltage table)</li>
<li><a href="https://www.modulargrid.net/e/2hp-arp-black-panel">2hp Arp</a> (arpeggio generator)</li>
<li><a href="https://www.modulargrid.net/e/klavis-caltrans-">Klavis Caltrans</a> (pitch manager)</li>
<li><a href="https://www.modulargrid.net/e/alyseum-q-linear">Alyseium Q-Linear</a> (pitch manager)</li>
<li><a href="https://www.modulargrid.net/e/bastl-instruments-1983">Bastl Instruments 1983</a> (pitch manager/MIDI interface)</li>
<li><a href="https://www.modulargrid.net/e/mazzatron-keys-1-keyboard-quantizer">Mazzatron KEYS-1 Keyboard Quantizer</a> (transposer)</li>
<li><a href="https://www.modulargrid.net/e/doepfer-a-173-1">Doepfer A-173-1 and -2</a> (transposer)</li>
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
	
	<li><strong>Quantizer Modules</strong></li>
	<li><a href="//doudoroff.com/midi/">MIDI Eurorack</a></li>
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
		h += '<br>%s' % row['_year']
	h += '<br><small>'
	if row['_hp'].strip():
		h += '<br>%s HP' % row['_hp']
	if row['_mgurl'].strip():
		h += '<br><a href="%s" target="_blank">Modular Grid &gt;</a>' % row['_mgurl']
	if row['_website'].strip():
		h += '<br><a href="%s" target="_blank">Web site &gt;</a>' % row['_website']
	h += '</small>'
	return h

def klassForproduct(val):
	return 'left'

def klassFornotes(val):
	return 'notes'

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

def valueForaccuracy(row):
	v = row['accuracy'].strip()

	if not v:
		return '???'
	else:

		bitdepth = row['_dacresolution']
		if decimal.Decimal(v) < decimal.Decimal('0.83'):
			note = '(less than one cent)'
		elif decimal.Decimal(v) < decimal.Decimal('2.52'):
			note = '(within a few cents)'
		else:
			note = '(beware)'

		return '%s-bit:<br>within %s millivolts<br>%s' % (bitdepth,v,note)

def klassForaccuracy(val):
	if not val.strip():
		return 'red'

	if val.strip():
		try:
			d = decimal.Decimal(val)
		except:
			pass
		else:
			if d > decimal.Decimal('2.5'):
				return 'red'

	return ''

rows = []
columnDisplayNames = {}

with open('quantizers.csv') as csvfile:

	reader = csv.DictReader(csvfile)

	for row in reader:

		# first row is special-contains our column display titles
		if row['product'] == 'Product':
			columnDisplayNames = row
		else:
			columns = []
			for fieldname in reader.fieldnames:
				if not fieldname.find('_')==0:
					v = row[fieldname]
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


# build th row
s = ''
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

# build table
s = html_top
s += '<table>' 


for row in rows:

	# if rows.index(row)%5==0:
	# 	s += table_header_row
	if rows.index(row)==0:
		s += table_header_row

	s += '\n<tr>'
	s += '\n\t'.join(row)
	s += '\n</tr>'
s += '\n</table>'

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


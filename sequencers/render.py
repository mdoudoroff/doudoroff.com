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
	<title>Eurorack Pitch + Gate Sequencer Module Comparison</title>
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
<strong>Pitch+Gate Sequencers</strong>

<a href="/quantizers/">Quantizers</a>
<a href="/midi/">MIDI Eurorack</a>
</nav>

<div class="main">

<h1>Eurorack Pitch + Gate Sequencer Module Comparison</h1>

<p>Martin Doudoroff<br>
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>Related discussion thread: <a href="https://www.modwiggler.com/forum/viewtopic.php?p=2581692"><em>heavy duty pitch + gate sequencer module comparison</em></a> (ModWiggler forum)</p>

<h4>Latest</h4>
<p class="updates">
2025-05-28 added TipTop 248t, Koma Monoplex, Qu-bit Bloom v2<br>
2024-10-09 added Tobinski Sequencer<br>
2024-06-01 added CubuSynth ConseQuencer<br>
2024-05-24 added DMMDM Droid Moto Kit, Doboz T12, and Tubbutec Brainstep<br>
2024-05-20 added Five12 Vector II and Rides in the Storm QSQ<br>
2024-04-10 added Glasgow Synth Guild Oct Tone<br>
2024-02-02 added 4ms Catalyst Sequencer and NONO Major Tom<br>
2023-12-12 added Floating Knobs Cuisine<br>
2023-09-24 various updates<br>
2023-09-10 added Tesseract Step Fader II<br>
2023-06-20 added Squarp Hermod+<br>
2023-02-22 added ALM ASQ-1<br>
2022-03-23 added various new sequencers to lists at bottom<br>
2021-06-01 added XAOC Moskwa II<br>
<span id="additionalUpdates" class="collapsed">
2021-05-15 errata<br>
2021-05-14 misc updates, added videos column<br>
2021-04-08 errata<br>
2021-02-15 added Intellijel Metropolix<br>
2021-01-23 minor updates<br>
2021-01-03 added Intellijel Tete+Tetrapad<br>
2020-12-19 added D&D Modules Heaven 16<br>
2020-12-12 added Extralife Super Sixteen, other updates<br>
2020-10-25 added Ladik S-280<br>
2020-08-01 added SDS Digital Sequarallel<br>
2020-07-21 added (with misgivings) Behringer 960 and 182<br>
2020-04-29 added the RYK M185<br>
2020-03-30 reworked the Gate Handling column<br>
2019-12-30 minor updates<br>
2019-10-28 added Befaco Muxlicer<br>
2019-10-27 added Qu-bit Bloom to the comparison, updates<br>
2019-10-15 removed Pittsburgh Sequence Designer<br>
2019-10-13 minor updates<br>
2019-09-30 added Tesseract Sequencer<br>
2019-09-30 added Oakley Sequencer<br>
2019-09-06 added Octone, other updates<br>
2019-09-05 added WMD Metron+Voltera<br>
2019-05-13 added Erica Black Sequencer, Livestock Shepard<br>
2019-05-08 added Endorphin.es Ground Control<br>
2019-05-03 added USTA, release years<br>
2019-02-13 added CFM1<br>
2019-02-10 stubbed out Per|Former (DIY)<br>
2018-09-19 added René 2<br>
2018-07-30 added Pittsburgh and Random Source sequencers, misc updates<br>
2018-04-26 misc updates, added Red Light District, Varigate 4+, and Lifeforms Micro Sequence<br>
2017-11-01 updates to FLXS1, added Squarp and 1010Music Toolbox<br>
2017-08-15 NerdSeq updates<br>
2017-07-03 Corrections<br>
2017-06-29 Added column on gate sequencing features; added Rene, Popcorn and Mattson sq816<br>
2017-06-19 Various tweaks and additions<br>
2017-06-18 Rough draft<br>
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

<p>It is important to understand that this comparison is quite picky, <strong>focusing on complex, all-in-one (“battleship”), melodic-oriented sequencers with fairly complete gate sequencing ability</strong>. It includes pretty much everything at the “high end” and excludes pretty much all simpler “utility sequencers”.</p>

<p style="border: 3px solid red; padding: 0.5em;">The Eurorack market offers a huge number (dozens, even hundreds) of comparatively simple “utility sequencers” that vary wildly in design and features. <strong>None of them are included in this comparison.</strong> Some of these “utility sequencers” store or generate variable CV levels, while others specialize in gate generation (gate sequencers). <strong>Any “simpler” sequencers can be patched together with each other and in combination with virtually any other Eurorack utility modules to create a custom pitch and gate sequence</strong>, often with interesting and idiosyncratic characteristics that cannot be achieved by relying on the all-in-one tools listed here. This <em>modular</em>, patching-centric approach to creating sequences can be more hands-on, immediate, and rewarding. So, please do not assume that you need any of the products listed on this page in order to make melodic music with your synthesizer.</p>

<p>This comparison can never be more than a starting place for further research—these modules are amongst the most complex in Eurorack and they are extremely hard to compare fairly and accurately—they each have design
biases reflecting different priorities and ideas about “process” (how you work with them). Most of these modules have tons of features that I cannot even begin to describe here. Do your homework. <strong>Sequencers are intensely personal tools.</strong></p>

<p>The <strong>Steps (UI basis/max pattern length)</strong> column describes the number of steps the interface facilitates for editing at one time versus the (max) number of steps in a pattern. 
This provides a clue about how “playable” or how much “windowing” is going on working with and navigating your sequence.</p>

<p>The <strong>UI Style</strong> column is an attempt to broadly categorize the operational styles of these different designs:</p>

<ul>
	<li><strong>classic</strong> means you have dedicated, separate pots/sliders for each step, yielding an operational style comparable to the vintage analog sequencers of yore</li>
	<li><strong>hybrid</strong> means there are pots/sliders for each step, but they get used for different modes and often are not accurately reflecting the current state of what you’re looking at</li>
	<li><strong>x0x</strong> generally implies a row of light-up buttons for choosing a step and a row of buttons similar to an octave of a piano keyboard for choosing notes—the working style popularized by the Roland 303 etc. in the 1980s</li>
	<li><strong>Cirklon-ish</strong> is a more modal push-button UI, often with lots of menus that remap the meaning of the buttons</li>
	<li><strong>per-step window</strong> means a form-like interface that focuses on the parameters of a single step, with no overall reperesentation of the sequence available</li>
	<li><strong>GUI</strong> means an interface focused on a computer-type display, generally with lots of menus and modes</li>
	<li><strong>Tracker</strong> is a specific GUI interface similar to a spreadsheet</li>
</ul>

<p>The <strong>Gate handling</strong> column is an attempt to characterize how the sequencer treats gates. All these sequencers emit (or at least pass through) gates of some sort, but they vary wildly in capabilities and style. Perhaps most critically, many attempt to provide per-step control over gate length. Per-step gate length can be critical for use with ADSR- and ASR-envelopes, but this capability often implies a more complex, programmatic user interface for the sequencer.</p>
<p>A few sequencers even provide for variable step length, meaning each step can have a duration of variable length, and within that duration, a gate of variable length. This approach, while more complex, makes more sophisticated phrasing (or “groove”) possible. Some of these designs will use the term “stage” in place of “step”.</p>

<p>Below the comparison is a directory of additional tools of potential interest that do not fit in the comparison.</p>

<h2>Comparison</h2>

'''

html_bottom = '''

<h2>External and partially-external alternatives with direct Eurorack integration</h2>
<p>There are, of course, a zillion MIDI solutions available for Eurorack and related ways to control one’s rack. 
These are a selection of alternatives to either a heavy-duty sequencer module (per above) or a straight-up MIDI-style approach (i.e., these can all produce CV):</p>
<ul>
<li><a href="http://www.analoguesolutions.com/generator/">Analogue Solutions Generator</a> (<strong>direct patch</strong>)</li>
<li><a href="https://www.arturia.com/beatstep-pro/overview">Arturia Beatstep Pro</a> (<strong>direct patch</strong>)</li>
<li><a href="https://www.arturia.com/products/keystep/overview">Arturia Keystep</a> (<strong>direct patch</strong>)</li>
<li><a href="https://www.arturia.com/products/hybrid-synths/keystep-pro/overview">Arturia Keystep Pro</a> (<strong>direct patch</strong>)</li>
<li><a href="http://www.grpsynthesizer.it/index.php/en/products/grp-synthesizer-r24-en.html">Grp Synthesizer R24</a> (<strong>direct patch</strong>)</li>
<li><a href="https://www.kilpatrickaudio.com/?p=carbon">Kilpatrick Audio Carbon</a> (<strong>direct patch</strong>)</li>
<li><a href="https://koma-elektronik.com/?product=komplex-sequencer">Koma Komplex</a> (<strong>direct patch</strong>)</li>
<li><a href="http://www.korg.com/us/products/dj/sq_1/">Korg SQ-1</a> (<strong>direct patch</strong>)</li>
<li><a href="http://makenoisemusic.com/synthesizers/ohctrl">Make Noise Music 0-Control</a> (<strong>direct patch</strong>)</li>
<li><a href="http://www.monome.org/docs/modular/ansible/">Monome Ansible w/Grid or Arc</a> (<strong>direct patch</strong>)</li>
<li><a href="https://novationmusic.com/keys/sl-mkiii">Novation SL MkIII</a> (<strong>direct patch</strong>)</li>
<li><a href="https://www.indiegogo.com/projects/noodlebox-a-serendipity-sequencer/x/23407414">Sixty Four Pixels Serendipity</a> (<strong>direct patch</strong>)</li>
<li><a href="https://oxiinstruments.com/product/oxi-one/">OXI One</a> (<strong>direct patch</strong>)</li>
<li><a href="http://polyend.com/seq-sequencer/">Polyend SEQ</a> (w/Poly MIDI-to-CV interface module)</li>
<li><a href="https://squarp.net/pyramid">Squarp Pyramid</a> (<strong>direct patch</strong>)</li>
<li><a href="https://squarp.net/hapax">Squarp Hapax</a> (<strong>direct patch</strong>)</li>
<li><a href="https://teenage.engineering/guides/po-modular/16">Teenage Engineering Pocket Operator Modular 16</a> (<strong>direct patch</strong>)</li>
<li><a href="https://www.sequentix.com">Sequentix Cirklon</a> (w/CV output module)</li>
<li><a href="http://www.signalarts.ca/sattetra.html">Signal Arts TetraMAPS</a> (Lemur/TouchOSC eurorack hardware + iPad solution)</li>
<li><a href="https://www.socialentropy.com/engine/?page_id=346">Social Entropy Engine</a> (w/CV expander)</li>
<li><a href="http://www.ucapps.de">uCApps MIDIbox SEQ</a> (DIY MIDI sequencer with extensive analog CV bus)</li>
</ul>

<h2>Additional Eurorack modules</h2>
<p>Finally, the modules below don’t quite belong in the above comparison but have been pointed out as being of potential interest:</p>
<ul>
<li><a href="https://modulargrid.net/e/arc-serge-tkb">Analogue Research (ARC) Serge TKB</a> (touch activated keyboard sequencer)</li>
<li><a href="https://www.antikulture.com">Antikulture Desruptor</a> (probability-focused sequencer)</li>
<li><a href="https://modulargrid.net/e/catalyst-audio-time-s-arrow">Catalyst Audio Time’s Arrow</a> (random melody-focused 16-step sequencer)</li>
<li><a href="https://modulargrid.net/e/cycle-instruments-tetrachords">Cycle Instruments Tetrachord</a> (four part arp/chord melody mill with sophisticated macro and cv control)</li>
<li><a href="https://modulargrid.net/e/divergent-waves-sycamore">Divergent Waves Sycamore</a> (two part melody mill)</li>
<li><a href="https://modulargrid.net/e/frequency-central-cryptograf">Frequency Central Polygraf</a> (16 step CV sequencer with novel addressing scheme)</li>
<li><a href="https://modulargrid.net/e/kaona-zazou">Kaona Zazou</a> (four part pitch generator/melody mill--see also Kaona Skippy gate generator)</li>
<li><a href="https://modulargrid.net/e/malekko-heavy-industry-voltage-block">Malekko Heavy Industries Voltage Block</a> (8 independent tracks of quantizable 16-step CV sequencing, but no gates)</li>
<li><a href="https://modulargrid.net/e/noise-engineering-mimetic-digitalis-">Noise Engineering Mimetic Digitalis</a> (novel compact cv-only grid-based sequencer with four outputs)</li>
<li><a href="https://modulargrid.net/e/other-unknown-degree-vco-controller">OK200 Degree</a> (novel quantized performance controller &amp; sequencer)</li>
<li><a href="https://modulargrid.net/e/percussa-super-signal-processor">Percussa SSP</a> (multi-function device that, amongst other things, can run a flexible number of 64-step cv+gate sequencers)</li>
<li><a href="https://rabidelephant.com/products/nexus-seq">Nexus Seq</a> (novel interactive CV sequencer with many unconventional ideas to make sequencing more immediate and performative)</li>
<li><a href="https://modulargrid.net/e/other-unknown-electro-music-klee-sequencer">San Pedro Labs Klee Sequencer</a> (teensy-based module with various sequencer programs)</li>
<li><a href="https://modulargrid.net/e/tinrs-tuesday">TiNRS Tuesday</a> (algorithmic melody-focused sequencer)</li>
<li><a href="https://modulargrid.net/e/tiptop-audio-z8000-mk2">Tiptop Z8000 Mk2</a> (novel cv-only grid-based sequencer with many outputs)</li>
<li><a href="https://modulargrid.net/e/twisted-electrons-cells">Twisted Electron Cells</a> (compact grid-like, dual sequencer)</li>
<li><a href="https://modulargrid.net/e/vermona-melodicer">Vermona meloDICER</a> (probability-focused musical phrase generator)</li>
</ul>

<p style="text-align:center;">• • •</p>

</div><!-- end div.main -->

<footer>
<nav>
<div class="navrail">
<ul>
	<li style="border-bottom: 2px solid gray;">Comparison guides</li>
	<li><a href="//doudoroff.com/mixers/">Stereo Mixer Modules</a></li>
	<li><strong>Pitch &amp; Gate Sequencers</strong></li>
	
	<li><a href="//doudoroff.com/quantizers/">Quantizer Modules</a></li>
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
	if row['_mgurl'].strip():
		h += '<br><a href="%s" target="_blank">Modular Grid &gt;</a>' % row['_mgurl']
	if row['_website'].strip():
		h += '<br><a href="%s" target="_blank">Web site &gt;</a>' % row['_website']
	h += '</small>'
	return h

def klassForproduct(val):
	return 'left'

def valueForvideos(row):
	bits = []
	links = row['videos'].split(';')
	for l in links:
		(text, url) = l.split('|')
		bits.append(f'<a href="{url.strip()}" target="_blank">{text.strip()}</a>')
	return '<br><br>'.join(bits)

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
	return '<br>'.join(vals)

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
					# v = locals()["valueFor%s" % fieldname](row)
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


			rows.append(columns)

# print rows

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

	# if rows.index(row)%5==0:
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

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


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
	<title>Eurorack Stereo Mixer Module Comparison</title>
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
			margin: 0.5em 0;
		}
		.main {	padding: 1em; }
		.red {color:red;}
		.green {color:green;}
		.gray {color:gray;}
		table {border-collapse: collapse;font-size: 85%;height: auto;}
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
	</style>
</head>
<body>

<nav id="comparisonSwitcher">
<strong>Stereo Mixers</strong>
<a href="/sequencers/">Pitch+Gate Sequencers</a>
<a href="/samplers/">Samplers</a>
<a href="/quantizers/">Quantizers</a>
<a href="/midi/">MIDI Eurorack</a>
</nav>


<div class="main">

<h1>Eurorack Stereo Mixer Module Comparison</h1>

<p>Martin Doudoroff<br>
<script><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>This is a pretty exhaustive and up-to-date basic comparison of all your stereo mixer module options for Eurorack, with an implicit focus on your output stage, although some of these modules are suitable for submixing. Some additional tools of potential interest are listed at the bottom. Related discussion thread: <a href="https://modwiggler.com/forum/viewtopic.php?t=154186"><em>stereo mixer module comparison</em> (ModWiggler forum)</a></p>

<h4>Latest</h4>
<p class="updates">
2024-04-17 added Weston m3s and Alyseum Q-MIXI<br>
2024-04-15 added Clank Endline<br>
2024-01-19 added blaknblu Alpha Pro<br>
2024-01-09 added Frequency Central Strips<br>
2023-12-12 added After Later Audio Bartender<br>
2023-11-30 added NANO Modules Performance Mixer<br>
2023-11-08 added AI Synthesis AI018 and BearModules MATRIX<br>
2023-10-02 added DPW M1 Mix<br>
2023-09-10 added XAOC Ostrawa, NANO ST MAR and Worng Soundstage II<br>
2023-09-09 added 1010music Bluebox Eurorack Edition and Boredbrain Xcelon<br>
2023-08-26 added Noise Engineering Xer Mixa<br>
2023-07-03 added Eowave Supamix<br>
2023-06-01 added Dreadbox Psychosis<br>
2023-05-28 added Sebsongs ST MIXER XL and ST Modular MIX & PAN<br>
2023-05-06 added Jolin Tutto & Sempre<br>
<span id="additionalUpdates" class="collapsed">
2023-02-13 added Animal Factory Tannhauser Gates<br>
2022-11-30 added ALM Mega Tang and G-Storm Electro Influx<br>
2022-11-23 added Instruo cárn and Uraltone Tube Sounding Micro Mixer<br>
2022-11-11 added Cosmotronic Cosmix Pro, Noise Engineering Xer Dualis, and Feedback Mix Mix<br>
2022-08-27 added Sebsongs ST Mixer<br>
2022-08-27 added D&D Wire Station<br>
2022-08-14 added NoisyFruitsLab 8CHAN<br>
2022-08-12 added added ADDAC713<br>
2022-06-17 added Modbap Transit; misc updates<br>
2021-12-01 added EMW 8-channel and updated Frap CGM<br>
2021-08-19 added Toppobrillo MiniMix<br>
2021-07-10 added Happy Nerding 4x Stereo Mixer<br>
2021-06-05 added Modulaire Maritime Victor Alpha 2 &amp; Feedback Mix BX<br>
2020-03-20 added Blood Cells Audio D.O.Mixx<br>
2020-01-11 small updates<br>
2020-11-24 added Frap Tools QSC<br>
2020-11-09 added SSF Vortices<br>
2020-10-30 added Endorphin.es Cockpit 2<br>
2020-08-02 added Make Noise XOH<br>
2020-08-01 added Ladik M-610<br>
2020-07-03 added Cosmotronic Cosmix<br>
2020-06-04 added 6IXMXM.SET and ST-Modular SUM CHANNEL + MAIN<br>
2020-06-01 minor updates<br>
2020-05-18 added ACL Pan Mix<br>
2020-02-17 added Doepfer A-135-3<br>
2020-02-17 added SynEssentials SE2026<br>
2020-02-16 added Modulaire Maritime Victor Alpha<br>
2019-11-20 added Arcaico Caronte MS-4<br>
2019-11-04 added Catoff Mix<br>
2019-11-03 added Paratek РИТМИКС<br>
2019-09-26 added Alyseum Q-Mix<br>
2019-09-26 added L-1 Discrete VC Stereo Mixer, other updates<br>
2019-09-26 removed Cwejman MX-4AS and Escalation Dominance<br>
2019-09-26 added Toppobrillo Stereomix 2<br>
2019-09-22 added Happy Nerding 2xSAM<br>
2019-08-06 added ph Mixer++<br>
2019-06-28 added new column about individual outs (for multitracking), other updates<br>
2019-05-08 added OIII Quad Mixer<br>
2019-04-30 added Make Noise X-Pan and the AGO Summingfacility; varoius other updates<br>
2019-03-27 added Befaco STMIX<br>
2019-02-10 added JPSynth Stereo Mixer<br>
2019-01-20 added Tesseract Tex Mix<br>
2018-11-16 added Takaab Nearness and stubbed out Worng Sound Stage<br>
2018-10-14 added ST-Modular SUM<br>
2018-09-07 Added SSI M-4 and Happy Nerding 3X<br>
2018-05-02 Added Happy Nerding PanMix Jr.<br>
2018-05-01 Added Roland 531, updates<br>
2018-03-15 Added Hyrlo, minor updates<br>
2018-02-07 Stubbed out 4ms Listen modules<br>
2017-12-21 Added Intellijel Mixup<br>
2017-11-13 Stubbed out Random*Source Stereo Mixer<br>
2017-08-14 Doepfer shipping update<br>
2017-07-04 Stubbed out the Befaco HEXA<br>
2017-06-29 XAOC Praga shipping update<br>
2017-06-05 Rebel Technologies Mix 02, Eric Stereo Mixer V2<br>
2017-06-01 ADDAC Stereo Summing Mixer<br>
2017-05-02 GRP Stereo Out Module<br>
2017-04-13 Doepfer A-138s<br>
2017-04-06 Qu-bit Mixology update<br>
2017-02-21 L-1 2 Channel Mixer &amp; Unity Stereo Mixer<br>
2017-02-01 Rebel Technologies Mix 01<br>
2017-01-31 Cwejman MX-4AS<br>
2017-01-30 Doepfer A-135<br>
2017-01-19 Qu-bit Mixology update<br>
2017-01-17 Pittsburgh Lifeforms System Interface<br>
2016-09-19 Ladik M-175 (and related)<br>
2016-09-15 WMD &amp; Erica updates<br>
2016-08-21 Toppobrillo &amp; Frap Tools update<br>
2016-07-06 Topporillo update<br>
2016-07-05 Endorphin.es Cockpit<br>
2016-06-29 Blue Lantern Stereo Sir Mix Alot + new related modules<br>
2016-06-01 Additonal PanMix details<br>
2016-05-19 Added Happy Nerding PanMix &amp; Hinton references<br>
2016-05-18 Added Arrel ER-100<br>
2016-03-24 Added initial info on Doepfer A-138p/o<br>
2016-03-23 Added initial info on Frap CGM<br>
2016-03-15 Added headphone column; updated data on Koma mixer<br>
2016-02-01 Updated WMD photo<br>
2016-01-27 Updated Toppobrillo info, new photos<br>
2016-01-26 More additions and corrections<br>
2016-01-25 Added more placeholder photos, missing modules, errata<br>
2016-01-24 Errata and many additions from Mod Wiggler members<br>
2016-01-23 Rough draft<br>
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


'''

html_bottom = '''

<p>In addition, these modules don’t really belong in the above comparison but have been pointed out as being of potential interest:</p>
<ul>
<li><a href="https://www.modulargrid.net/e/make-noise-rxmx">Make Noise RxMx</a> (can be employed in a stereo manner)</li>
<li><a href="https://www.modulargrid.net/e/other-unknown-sponde">IO Instruments Sponde</a> (can be employed in a stereo manner)</li>
<li><a href="https://www.modulargrid.net/e/intellijel-mutamix">Intellijel Mutamix</a> (can be employed in a stereo manner)</li>
<li><a href="https://www.modulargrid.net/e/intellijel-azimuth-ii">Intellijel Azimuth II</a> (single channel of mono to stereo with panning and spread, amongst other features)</li>
<li><a href="https://www.modulargrid.net/e/4ms-company-vca-matrix">4ms VCA Matrix</a> (multi-channel mixing and routing vca that can be employed in a stereo manner)</li>
<li><a href="https://www.modulargrid.net/e/addac-system-addac802-quintet-mixing-console">ADDAC 802 Quintet Mixing Console</a> (multi-cahnnel mixing and routing vca that can be employed in a stereo manner)</li>
<li><a href="https://www.modulargrid.net/e/low-gain-electronics-submix">Low-Gain Submix</a> (multi-channel mixing and routing vca that can be employed in a stereo manner)</li>
<li><a href="https://www.modulargrid.net/e/mfb-drum-99">MFB Drum-99</a>  (multi-channel stereo submixer)</li>
<li><a href="https://www.modulargrid.net/e/hinton-instruments-modmixii">Hinton Instruments ModMix II</a> (dual four input mixer with added sauce; also note other Hinton products relevant to stereo mixing)</li>
<li><a href="https://www.modulargrid.net/e/other-unknown-worng-lrmsmslr">Worng LRMSMSLR Mid-Side (MS) Matrix</a> (mid side stereo processor for Eurorack)</li>
<li><a href="https://www.modulargrid.net/e/ladik-m-160-6ch-mono-stereo-aux-mixer">Ladik M-160</a> (configurable mixer)</li>
<li><a href="https://www.modulargrid.net/e/blue-lantern-modules-stereoscopic-duo-vca--">Blue Lantern Stereoscopic Duo VCA</a></li>
<li><a href="https://www.modulargrid.net/e/hikari-instruments-atten-mixer">Hikari Atten/Mixer</a></li>
<li><a href="http://omsonic.co.uk/product/omsonic-universal-panning-expander-upe-and-mixer/">omsonic Universal Panning Expander and Mixer</a></li>
<li><a href="https://github.com/sarnesjo/nearness">Nearness</a> (clever space-efficient DIY design)</li>
<li><a href="https://www.modulargrid.net/e/qu-bit-electronix-synapse">Qu-bit Synapse</a> (can be employed in a stereo manner)</li>
</ul>

<p style="text-align:center;">• • •</p>

</div><!-- end div.main -->

<footer>
<nav>
<div class="navrail">
<ul>
	<li style="border-bottom: 2px solid gray;">Comparison guides</li>
	<li><strong>Stereo Mixer Modules</strong></li>
	<li><a href="//doudoroff.com/sequencers/">Pitch &amp; Gate Sequencers</a></li>
	<li><a href="//doudoroff.com/samplers/">Sampler Modules</a></li>
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

def valueForindiv_outs(row):
	if row['indiv_outs']:
		return row['indiv_outs']
	return '–'

rows = []
columnDisplayNames = {}

with open('mixers-data.csv',encoding='utf-8') as csvfile:

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
	if rows.index(row)==0:
		s += table_header_row

	s += '\n<tr>'
	for bit in row:
		try:
			s += '\n\t' + bit
		except Exception as reason:
			print("FAILED (%s) on bit:" % reason)
			print(bit)
			sys.exit(1)
	s += '\n</tr>'
s += '\n</table>'

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


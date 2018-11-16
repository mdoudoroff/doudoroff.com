#!/usr/bin/env python
# encoding: utf-8

import json, csv


html_top = u'''
<html>
<head>
	<meta charset="utf-8">
	<title>Eurorack Stereo Mixer Module Comparison</title>
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
table {border-collapse: collapse;font-size: 85%;}
td, th {text-align:center;padding:0.25em 1em;border-bottom:1px solid #eee;}
td.left, th.left {text-align:left;}
td.notes {text-align: left;}
td ul { padding-left: 20px; -webkit-padding-start: 20px; }
th { background-color: #eee; color: #666; }
</style>
<body>

<h1>Eurorack Stereo Mixer Module Comparison</h1>

<p>Martin Doudoroff<br />
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>Related discussion thread: <a href="https://muffwiggler.com/forum/viewtopic.php?t=154186"><em>stereo mixer module comparison</em> (MuffWiggler forum)</a></p>

<p class="updates">
2018-11-16 added Takaab Nearness and stubbed out Worng Sound Stage<br />
2018-10-14 added ST-Modular SUM<br />
2018-09-07 Added SSI M-4 and Happy Nerding 3X<br />
2018-05-02 Added Happy Nerding PanMix Jr.<br />
2018-05-01 Added Roland 531, updates<br />
2018-03-15 Added Hyrlo, minor updates<br />
2018-02-07 Stubbed out 4ms Listen modules<br />
2017-12-21 Added Intellijel Mixup<br />
2017-11-13 Stubbed out Random*Source Stereo Mixer<br />
2017-08-14 Doepfer shipping update<br />
2017-07-04 Stubbed out the Befaco HEXA<br />
2017-06-29 XAOC Praga shipping update<br />
2017-06-05 Rebel Technologies Mix 02, Eric Stereo Mixer V2<br />
2017-06-01 ADDAC Stereo Summing Mixer<br />
2017-05-02 GRP Stereo Out Module<br />
2017-04-13 Doepfer A-138s<br />
2017-04-06 Qu-bit Mixology update<br />
2017-02-21 L-1 2 Channel Mixer &amp; Unity Stereo Mixer<br />
2017-02-01 Rebel Technologies Mix 01<br />
2017-01-31 Cwejman MX-4AS<br />
2017-01-30 Doepfer A-135<br />
2017-01-19 Qu-bit Mixology update<br />
2017-01-17 Pittsburgh Lifeforms System Interface<br />
2016-09-19 Ladik M-175 (and related)<br />
2016-09-15 WMD &amp; Erica updates<br />
2016-08-21 Toppobrillo &amp; Frap Tools update<br />
2016-07-06 Topporillo update<br />
2016-07-05 Endorphin.es Cockpit<br />
2016-06-29 Blue Lantern Stereo Sir Mix Alot + new related modules<br />
2016-06-01 Additonal PanMix details<br />
2016-05-19 Added Happy Nerding PanMix &amp; Hinton references<br />
2016-05-18 Added Arrel ER-100<br />
2016-03-24 Added initial info on Doepfer A-138p/o<br />
2016-03-23 Added initial info on Frap CGM<br />
2016-03-15 Added headphone column; updated data on Koma mixer<br />
2016-02-01 Updated WMD photo<br />
2016-01-27 Updated Toppobrillo info, new photos<br />
2016-01-26 More additions and corrections<br />
2016-01-25 Added more placeholder photos, missing modules, errata<br />
2016-01-24 Errata and many additions from Muffwiggler members<br />
2016-01-23 Rough draft</p>


'''

html_bottom = u'''

<p>In addition, these modules don’t really belong in the above comparison but have been pointed out as being of potential interest:</p>
<ul>
<li><a href="https://www.modulargrid.net/e/make-noise-rxmx">Make Noise RxMx</a> (can be employed in a stereo manner)</li>
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


rows = []
columnDisplayNames = {}

with open('mixers-data.csv') as csvfile:

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

# build table
s = html_top
s += '<table>' 


for row in rows:

	if rows.index(row)%5==0:
		s += table_header_row

	s += u'\n<tr>'
	s += u'\n\t'.join(row)
	s += u'\n</tr>'
s += u'\n</table>'

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


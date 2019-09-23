#!/usr/bin/env python
# encoding: utf-8

import json, csv


html_top = u'''
<html>
<head>
	<meta charset="utf-8">
	<title>Eurorack Quantizer Comparison</title>
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
.collapsed {display: none;}

nav { 
	background: #eef; 
	padding: 0.25em 1em;
	font-family: Helvetica, sans-serif;
	border-bottom: 2px solid #666;
	}
nav p { margin: 0.5em 0; }
nav ul { margin: 0 0 0.5em 0; padding: 0; }
nav ul li { list-style: none; display: inline-block; margin-right: 1em; }
</style>
<body>

<nav>
<p><em>Martin’s Eurorack Module Comparisons:</em></p>
<ul>
	<li><a href="//doudoroff.com/mixers/">Stereo Mixer Modules</a></li>
	<li><a href="//doudoroff.com/sequencers/">Pitch &amp; Gate Sequencers</a></li>
	<li><a href="//doudoroff.com/samplers/">Sampler Modules</a></li>
	<li><strong>Quantizer Modules</strong></li>
</ul>
</nav>

<h1>Eurorack Pitch Quantizer Module Comparison</h1>

<p>Martin Doudoroff<br />
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>Note: I’m still adding the rows to this comparison—if your favorite quantizer is missing, don’t worry (yet).</p>

<!--<p>This is a pretty exhaustive and up-to-date basic comparison of all your pitch quantizer module options for Eurorack. 
Some additional tools of potential interest are listed at the bottom.--> 

<p>Related discussion thread: <a href="https://www.muffwiggler.com/forum/viewtopic.php?t=222110"><em>Eurorack pitch quantizer comparison</em> (MuffWiggler forum)</a></p>


<h4>Latest</h4>
<p class="updates">
2019-09-23 rough draft<br />
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


'''

html_bottom = u'''

<p>In addition, these modules don’t really belong in the above comparison but have been pointed out as being of potential interest:</p>
<ul>
<li><a href="https://www.modulargrid.net/e/qu-bit-electronix-chord">Qu-bit Chord</a> (chord-generating quad-oscillator with parametric front-end)</li>
<li><a href="https://www.modulargrid.net/e/qu-bit-electronix-chord-v2">Qu-bit Chord 2</a> (chord-generating quad-oscillator with parametric front-end)</li>
<li><a href="https://www.modulargrid.net/e/2hp-arp-black-panel">2hp Arp</a> (arpeggio generator)</li>
<li><a href="https://www.modulargrid.net/e/klavis-caltrans-">Klavis Caltrans</a> (pitch manager)</li>
<li><a href="https://www.modulargrid.net/e/bastl-instruments-1983">Bastl Instruments 1983</a> (pitch manager/MIDI interface)</li>
<li><a href="https://www.modulargrid.net/e/mazzatron-keys-1-keyboard-quantizer">Mazzatron KEYS-1 Keyboard Quantizer</a> (transposer)</li>
<li><a href="https://www.modulargrid.net/e/doepfer-a-173-1">Doepfer A-173-1 and -2</a> (transposer)</li>
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
	if row['_year'].strip():
		h += u'<br />%s' % row['_year']
	h += u'<br /><small>'
	if row['_hp'].strip():
		h += u'<br />%s HP' % row['_hp']
	if row['_mgurl'].strip():
		h += u'<br /><a href="%s" target="_blank">Modular Grid &gt;</a>' % row['_mgurl'].decode('utf-8')
	if row['_website'].strip():
		h += u'<br /><a href="%s" target="_blank">Web site &gt;</a>' % row['_website'].decode('utf-8')
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


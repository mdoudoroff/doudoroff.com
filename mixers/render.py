#!/usr/bin/env python3
# encoding: utf-8

import csv
import json
import sys

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

<p>Welcome to the <em>revised</em> comparison launched in 2025, featuring a narrowed, stronger focus.</p>
<p>When I began the comparison in 2016, there only only a few options—less than ten. Today, depending how you count,
there are well over a hundred, and potentially more than 150 (if you cast the widest net).</p>
<p>However, the vast majority of these mixers are poorly-differentiated variations on simple, compact (or at least relatively compact) designs
with little to no actual modular functionality (e.g., cv control) and no distinct vision. These relatively generic stereo utility mixers are
perfectly fine, and perfectly adequate for many people’s modest needs. On the other hand, they are not interesting in and of themselves,
few are around for long (most are boutique limited runs or are quickly superseded by slightly tweaked newer designs), and they’re damned tedious to track,
and damned tedious to wade through. The old comparison, which <a href="index-pre-purge.html">you can still view</a>, had some of these, but far from all.</p>
<p>The new comparison focuses only on major mixer modules, generally those with at least some CV control, generally those with six or more channels.
As of this writing, I’m leaving in the “nearness”-related mixers because they employ a form of patch programmability (if you squint a bit). No small
utility mixers (you can find those on modulargrid), no matrix mixers (I love them, but they are not what this is designed for), and fewer dark, dusty corners.</p>

<p>Related discussion
thread:
<a href="https://modwiggler.com/forum/viewtopic.php?t=154186"
    ><em>stereo mixer module comparison</em> (ModWiggler
    forum)</a
></p>

<h4>Latest</h4>
<p class="updates">
2025-11-29 major purge and refocusing of the comparison<br>
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

html_bottom = '''


<p style="text-align:center;">• • •</p>

</div><!-- end div.main -->

<footer>
<nav>
<div class="navrail">
<ul>
	<li style="border-bottom: 2px solid gray;">Comparison guides</li>
	<li><strong>Stereo Mixer Modules</strong></li>
	<li><a href="//doudoroff.com/sequencers/">Pitch &amp; Gate Sequencers</a></li>

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
    if val.lower() in ('0', 'tbd'):
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
        return (
            '''<a href="gfx/%s"><img src="gfx/%s" style="width:%spx;height:%spx;cursor:zoom-in;" /></a>'''
            % (row['pic'], row['pic'], width, height)
        )
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

with open('mixers-data.csv', encoding='utf-8') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        # first row is special-contains our column display titles
        if row['product'] == 'Product':
            columnDisplayNames = row
        else:
            columns = []
            for fieldname in reader.fieldnames:
                if not fieldname.find('_') == 0:
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
                    columns.append('<td class="%s">%s</td>' % (klass, v))

            rows.append(columns)


# build th row
s = ''
s += '<tr>'
for fieldname in reader.fieldnames:
    if not fieldname.find('_') == 0:
        klass = ''
        try:
            klass = locals()["klassFor%s" % fieldname](fieldname)
        except:
            klass = klassForAny(fieldname)

        s += '<th class="%s">%s</th>' % (klass, columnDisplayNames[fieldname])
s += '</tr>'
table_header_row = s

# build table
s = html_top
s += '<table>'


for row in rows:

    # if rows.index(row)%5==0:
    if rows.index(row) == 0:
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

f = open('index.html', 'wb')
f.write(s.encode('utf-8'))
f.close()

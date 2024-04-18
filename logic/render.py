#!python
# encoding: utf-8

import json, os, random

from recipes import recipes

f = open('keywords.json','r')
KEYWORDS = json.load(f)
f.close()

#BDDCFF   #459DFF    blue (light, dark)
#FFCEC9   #FF5F52    red
#B0FFFF   #38FDFE    light blue
#FFD996   #FFAE1F    orange
#AEFCD0   #38FC8D    light green


latest = '''

<div id="about">

<p>This cookbook is by no means exhaustive, but will hopefully be helpful to a few folks. If you think you find an error or wish to submit a recipe for inclusion, get in touch!</p>

<p>Martin Doudoroff<br />
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<p>Related discussion thread: <a href="https://www.modwiggler.com/forum/viewtopic.php?t=271848"><em>A Logic Cookbook for Synthesis</em></a> (ModWiggler forum)</p>

<h4>Latest</h4>
<p class="updates">
2024-04-10 updated the PWM recipe<br>
2023-03-16 added recipes for PWM and sub-octave generation<br />
2023-03-12 added recipes for toggle, gate-to-trigger, and trigger-to-gate<br />
2023-03-11 first draft
<span id="additionalUpdates" class="collapsed">
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

</div>
'''

html_top = '''
<html>
<head>
	<meta charset="utf-8">
	<title>A Logic Cookbook for Synthesis</title>
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

span.kw_cat, span.kw_fn {
	display: inline-block;
	font-family: sans-serif;
	font-size: 12px;
	background-color: #ddf;
	padding: 2px 0.5em;
	border-radius: 12px;
	cursor: pointer;
	text-decoration: none;
}

a span.kw_cat:hover, a span.kw_fn:hover {
	color: red;
	background-color: #fdd;
}

div.entry {
	border-bottom: 1px solid #eee;
	padding: 0.5em 0;
	max-width: 640px;
}

p.principle {
	font-style: italic;
	color: #FF5F52;
}

@media (max-width: 450px) {
	.main { padding: 1em 0.5em; }
	nav { padding: 0.25 0.5em; }
}

#recipefilters {
	display: flex;
}

fieldset {
	border: none;
	border-radius: 12px;
}



.category { background-color: #AEFCD0; }
span.category { background-color: #AEFCD0; }
.category.cv {}
.category.audio {}
.function { background-color: #FFD996; }
span.function { background-color: #FFD996; }


#about {
  margin-top: 2em;
	padding: 1em;
	background: #eee;
	border-radius: 12px;
	max-width: 960px;
}

</style>
<body>

<div class="main">
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
	<li><a href="//doudoroff.com/midi/">MIDI Eurorack</a></li>
</ul>
<ul>
	<li style="border-bottom: 2px solid gray;">Martin’s other articles</li>
	<li><a href="//doudoroff.com/cold-mac/">Patching Cold Mac</a></li>
	<li><a href="//doudoroff.com/multitracking/">How to Multitrack Your Eurorack</a></li>
	<li><strong>A Logic Cookbook for Synthesis</strong></li>
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

def recipeKwCount(kw):
	# print(kw)
	# print([x for x in recipes._recipes if kw in x.allKw()])
	return len([x for x in recipes._recipes if kw in x.allKw()])

def render():

	# ============= index page =============

	hbits = []

	hbits.append('<h1>A Logic Cookbook for Synthesis</h1>')



	# --- filter UI ---
	groupCounter = 0
	h = '\n<div id="recipefilters">'

	groupCounter += 1
	h += '\n\t<fieldset id="filtergroup%s" style="display:none;">' % groupCounter
	h += '<strong>Choose a module (optional)</strong><br />'
	h += '\n\t<select id="ingredientChooser" style="width:250px;">'
	h += '\n\t\t<optgroup><option value="">(all)</option></optgroup>'
	currentOptionGroup = None
	for p in []:
		h += '<optgroup>'
		currentOptionGroup = 'foo'
		h += '\n\t\t<option value="iid%s">%s</option>' % ('[iid]','[name]')
	h += '\n\t</optgroup>'
	h += '\n\t</select>'
	h += '\n\t</fieldset>'

	groupCounter += 1
	h += '\n\t<fieldset id="filtergroup%s" class="category">' % groupCounter
	h += '<strong>Categories</strong><br />'
	for kw in KEYWORDS['categories']:
		if recipeKwCount('cat_'+kw):
			h += '\n\t\t<label><input type="checkbox" name="cat_%s" value="cat_%s" /> %s (%s)</label><br />' % (
				kw,
				kw,
				KEYWORDS['categories'][kw],
				recipeKwCount('cat_'+kw)
				)
	h += '\n\t</fieldset>'

	groupCounter += 1
	h += '\n\t<fieldset id="filtergroup%s" class="function">' % groupCounter
	h += '<strong>Functions</strong><br />'
	for kw in KEYWORDS['functions']:
		if recipeKwCount('fn_'+kw):
			h += '\n\t\t<label><input type="checkbox" name="fn_%s" value="fn_%s" /> %s (%s)</label><br />' % (
				kw,
				kw,
				KEYWORDS['functions'][kw],
				recipeKwCount('fn_'+kw)
				)
	h += '\n\t</fieldset>'
	h += '\n</div><!--end #recipefilters -->'

	hbits.append(h)
	# ---

	hbits.append('<p id="matchesAnnotation"></p>')

	for r in sorted(recipes._recipes,key=lambda x: x._sortKey):
		hbits.append(f'<div class="entry {r.hKeywordClasses()}">')
		hbits.append(f'<strong><a href="{r.fnForSelf()}">{r._title}</a></strong><br />')
		hbits.append(f'{r.hSummary()}<br />')
		hbits.append(f'{r.hKeywordSummary()}')
		hbits.append('</div>')

	bust = random.randint(10000,99999)
	hbits.append('<script type="text/javascript" src="jquery.min.js?b={bust}"></script>')
	hbits.append('<script type="text/javascript" src="recipeindex.js?b={bust}"></script>')

	hbits.append(latest)

	f = open('index.html','w')
	f.write(html_top + '\n'.join(hbits) + html_bottom)
	f.close()


	# ============= detail pages =============

	for r in recipes._recipes:

		hbits = []

		hbits.append(f'<p><strong><a href="index.html">A Logic Cookbook for Synthesis</a></strong></p>')

		hbits.append(f'<article class="{r.hKeywordClasses()}">')
		hbits.append(f'<h1>{r._title}</h1>')
		hbits.append(f'<small>Attibution: {r._attribution}</small>')
		if r._principle:
			hbits.append(f'<p class="principle">{r._principle}</p>')
		hbits.append(f'{r.hBody()}')

		hbits.append('<p><a href="index.html">&lt; Back</a></p>')

		hbits.append('</div>')

		f = open( r.fnForSelf(),'w' )
		f.write( html_top + '\n'.join(hbits) + html_bottom )
		f.close()


if __name__=='__main__':
	render()

#!/usr/bin/env python
# encoding: utf-8

import json, csv, decimal, sys

if sys.version_info[0] != 3:
    sys.exit("This script requires Python version 3")

html_top = '''
<html>
<head>
	<meta charset="utf-8">
	<title>How to Multitrack Your Eurorack</title>
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
th { background-color: #eee; color: #666; }
.notes { min-width: 15em; }
.collapsed {display: none;}

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





img.diagram {
	height: 450px;
	width: auto;
}

h2, h3 {
	margin-top: 1.5em;
	margin-bottom: 0.5em;
}

@media (max-width: 450px) {
	img.diagram { width: 100%; height: auto; }
}


</style>
<body>

<nav>
<div class="navrail">
<ul>
	<li style="border-bottom: 2px solid gray;">Comparison guides</li>
	<li><a href="//doudoroff.com/mixers/">Stereo Mixer Modules</a></li>
	<li><a href="//doudoroff.com/sequencers/">Pitch &amp; Gate Sequencers</a></li>
	<li><a href="//doudoroff.com/samplers/">Sampler Modules</a></li>
	<li><a href="//doudoroff.com/quantizers/">Quantizer Modules</a></li>
</ul>
<ul>
	<li style="border-bottom: 2px solid gray;">Martin’s other articles</li>
	<li><a href="//doudoroff.com/cold-mac/">Patching Cold Mac</a></li>
	<li><strong>How to Multitrack Your Eurorack</strong></li>
	<li><a href="https://www.youtube.com/user/MartinDoudoroffLLC/videos">Martin’s YouTube videos</a></li>
</ul>
</div>
</nav>

<div class="main">


<h1>How to Multitrack Your Eurorack</h1>



<p>Martin Doudoroff<br />
<script type="text/javascript"><!--
var vtnrkjn = ['f','i','o','f','a','=','a','<','a','>','n','l','f','a','<','r',':','a','f','i','"','o','o','@','o','m','.','m','h','>','r','e','=','d','i','@','r','c','"','a','o','u','s','t','/','l','d','o','m','o','m','d','t','"','s','c','.',' ','d',' ','o','m','m','a','"','u','r','f','e','c','n','o','r','i','t','l'];var tbigqfr = [67,48,70,66,47,43,40,72,53,75,21,12,31,74,0,54,15,1,30,11,50,60,27,58,65,16,68,52,3,51,28,45,7,26,56,22,4,38,8,10,14,61,41,13,73,39,62,29,71,34,9,59,19,44,42,33,32,37,23,2,63,46,35,17,36,25,64,6,5,69,57,24,18,20,55,49];var bnsubaz= new Array();for(var i=0;i<tbigqfr.length;i++){bnsubaz[tbigqfr[i]] = vtnrkjn[i]; }for(var i=0;i<bnsubaz.length;i++){document.write(bnsubaz[i]);}
// --></script>
<noscript>Please enable Javascript to see the email address</noscript></p>

<small>Thanks to flo, Cromatica45, desolationjones, and simka for their input.</small>

<p>This guide attempts to summarize and demystify the options and considerations for those making the move from stereo recording to multitrack recording of their Eurorack modular system. </p>





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

<h2>Contents</h2>

<p>Your options will largely depend on how many tracks you wish to record concurrently from your modular, and, of course, the rest of your “studio setup”. Some of your options are most suitable for 4-6 simultaneous tracks, some sit around 8 tracks, others support even more.</p>

<p>The first three options I describe are related and—depending how you look at it—overlap, but have distinct practical implications. They are the analog solutions. The digital solutions are outlined thereafter.</p>

<p>Your options:</p>
<ol>
	<li><a href="#directpatch">Directly patch each voice into your studio</a> (analog, any number of channels)</li>
	<li><a href="#snake">Use a DB25/snake adapter module</a> (analog, 8-channels, 16-channels)</li>
	<li><a href="#mixermodule">Use a stereo mixer module with individual channel output jacks</a> (analog, 4-8 channels)</li>
	<li><a href="#interfacemodule">Put a computer audio interface in your modular</a> (digital, 4-14 channels)</li>
	<li><a href="#adatmodule">Put an ADAT interface in your modular</a> (digital, 6-8 channels)</li>
	<li><a href="#recordermodule">Self-contained multitrack recording within the modular itself</a> (digital, 4-16 channels)</li>
</ol>
<p>Additional considerations:</p>
<ol>
	<li><a href="#interfaces">Computer Audio Interfaces and alternatives</a></li>
	<li><a href="#coupling">DC-coupling</a></li>
	<li><a href="#postfader">Pre-fader/Post-fader recording</a></li>
</ol>
<p>Case studies:</p>
<ol>
	<li><a href="#studypragaportastudio">Two Pragas and a portastudio</a></li>
	<li><a href="#study4848">Small studio integration with a WMD Performance Mixer+DB25, PreSonus 4848, and a little ADAT</a></li>
</ol>


<h3 id="directpatch">Option 1: Directly patch each voice into your studio</h3>

<p>This option is common with folks whose modular is part of a larger, mature studio context, and it is straightforward and direct: you simply run a cable from each audio signal you wish to record out of your modular to some destination where recording can happen. That might be straight into an computer audio interface, into a mixing console, into a portastudio, or into an audio recorder, possibly passing through a patch bay, effects and other equipment along the way! Typically that patch is simply accomplished with an 1/8" TR to 1/4" TR cable or a 1/8" to 1/4" adapter.</p>

<img src="gfx/option-direct.png" class="diagram" />

<p>This approach can scale from just a single mono signal up to any number of mono and stereo channels, depending on what the rest of your studio setup can handle.</p>

<p>The main issue with this approach is that Eurorack modular voltage levels are pretty hot (±10V range). Most mixing consoles have no trouble handling Eurorack voltages, but depending on the headroom of the destination to which you are patching, you may wish to run the signal through an attenuator first. Any attenuator could work, but there are modules specifically designed to ease output attenuation. One simple, inexpensive example is the passive <a href="https://www.modulargrid.net/e/ladik-p-520-4ch-out-line">Ladik P-520</a>. Numerous “output modules” also exist that provide balanced audio outputs, although they’re typically stereo, and for multitracking you’d need multiples of those, which could get quite expensive and consume a lot of hp.</p>




<h3 id="snake">Option 2: Use a DB25/snake adapter module</h3>

<p>This option centers around a Eurorack module that takes your various Eurorack voices, attenuates them to line level, and passes them out a DB25 connector, to which you attach a “snake” that carries the signals to your computer audio interface, patch bay, or other studio gear. The DB25 approach is implemented in blocks of eight channels, typically of balanced audio. The best known such solution is probably the <a href="https://www.modulargrid.net/e/nw2s-nw2s-io-balanced">nw2s::io</a> module.</p>

<img src="gfx/option-db25.png" class="diagram" />

<p>The advantage to this approach is that you can tidily deliver up to eight channels of properly attenuated (line level), balanced audio for processing and recording, without a lot of repatching between your module and the rest of your studio. It’s also relatively space-efficient compared to some alternatives, and depending on your other studio equipment, it may be relatively cost-effective.</p>

<p>In fact, there are other high density snake connector systems around, such as EDAC, and high end alternatives for managing multiple outputs from your modular, such as Hinton Instrument’s <a href="http://www.hinton-instruments.co.uk/paprod/modular/trimmer/">Trimmer</a>. Some modular synthesists use these, instead. If you’re reading this guide in the first place, then these sorts of heavy duty options are most likely out of scope, but it’s good to know they exist.</p>

<p>A related approach is the <a href="https://www.modulargrid.net/e/wmd-pm-db25">PM DB25 expander</a> for the popular <a href="https://www.modulargrid.net/e/wmd-performance-mixer-black">WMD Performance Mixer</a>. The latter is a stereo mixer module that—fully expanded—can handle up up to six mono channels and four stereo channels. The PM DB25 expander delivers all those channels, plus the stereo mix, out through two DB25 ports—a total of sixteen line level signals of balanced audio. The PM DB25 only works with the WMD Performance mixer, so you’re unlikely to consider this option unless you want the Performance Mixer in your rack, but it’s a tidy solution and offers the convenience that any and every channel you’re working with in the mixer can be recorded at any time with no extra patching.</p>





<h3 id="mixermodule">Option 3: Use a stereo mixer module with individual channel output jacks</h3>

<p>People have various reasons for wanting a stereo mixer in their modular synthesizer to begin with, so multitrack recording will be only one of the factors why you would choose to purchase and employ any of these Eurorack stereo mixers. A few Eurorack stereo mixer modules offer <strong>individual channel outputs</strong>, which enable you to multitrack record your modular while still using the stereo mixer module in your patch. </p>

<p>We already mentioned the WMD Performance Mixer, above, which delivers individual channels (pre-fader—more on this below) over line level DB25. A few other stereo mixers offer individual 1/8" output jacks per track:

<ul>
	<li><a href="https://www.modulargrid.net/e/xaoc-devices-praga">Xaoc Devices Praga</a> is a four channel stereo mixer; each channel has an individual “VCA output” which is “post-fader” (see considerations, below); you can direct patch from this jack (Eurorack signal levels) to the studio recording solution of your choice; multiple Praga modules can be connected to add additional channels</li>
	<li>similarly, <a href="https://www.modulargrid.net/e/befaco-hexmix">Befaco Hexmix</a> + <a href="https://www.modulargrid.net/e/befaco-hexpander">Hexpander</a> is a six track stereo mixer with individual channel outputs (post-fader, post-eq) for each of the six channels</li>
	<li><a href="https://frap.tools/products/mixer/">Frap Tools CGM</a> is a modular Eurorack stereo mixer system, with separate modules for mono channels and stereo channels; each has a direct output (pre- or post-fader, configurable) useful for multitrack recording; pretty much any number of mono or stereo channels can be configured with enough pieces of this system</li>
</ul>

<img src="gfx/option-stereo-mixer.png" class="diagram" />






<h3 id="interfacemodule">Option 4: Put a computer audio interface in your modular</h3>

<p>Expert Sleepers offers two modules—the <a href="https://www.modulargrid.net/e/expert-sleepers-es-8">ES-8</a> and the <a href="https://www.modulargrid.net/e/expert-sleepers-es-9">ES-9</a>—each of which embed a USB class-compliant audio interface in a Eurorack module. These modules connect to your computer over USB, and pass bidirectional digital audio between your modular and your computer. The modules themselves handle the analog-to-digital and digital-to-analog conversions.</p>

<ul>
	<li>Expert Sleepers ES-8 will send up to four audio tracks to your computer, and return eight. You can add various expansion modules to the ES-8 to send up to twelve audio tracks to your computer, and return up to 16.</li>
	<li>Expert Sleepers ES-9 will send up to fourteen audio channels to your computer and return 8. Headphone and balanced outputs are also provided.</li>
</ul>

<img src="gfx/option-es8-es9.png" class="diagram" />

<p>For multitrack recording purposes, this approach is tidy (one USB cable does it all), and appealing for those who don’t already have a suitable computer audio interface. An additional point of interest is that these modules are DC-coupled, meaning that they can pass control voltage bi-directionally in addition to audio. Some DAWs (Ableton and Bitwig, in particular) and other software (Virtual Rack, Silent Way, etc.) can employ this feature to further integrate your modular with your computer, and it is one of the most accurate ways to clock your modular from your DAW (or, perhaps, clock your DAW from your modular—your mileage may vary).</p> 

<p>If you do already have a computer audio interface, then running an ES-8 or ES-9 at the same time as a second interface may not be what you want to do. A personal computer only wants to deal with a single audio interface, so if you have more than one interface, you need a software broker to make them appear as one to the rest of the computer. This sleight of hand is easy to do on a Mac, because of the Aggregate Device feature built into the operating system. On Windows, you’ll need a utility such as ASIO4LL.</p>




<h3 id="adatmodule">Option 5: Put an ADAT interface in your modular</h3>

<p>By “ADAT” we actually mean “ADAT Lightpipe”. It’s nothing new: a standard for transmitting eight channels of digital audio over a fiber optic cable. Many computer audio interfaces (and various other types of gear) offer ADAT interfaces because it’s an inexpensive, space-efficient way to handle additional channels of (digital) audio without having to also implement the ADCs, DACs and related hardware of translating those channels to and from the analog domain. Consequently, some audio equipment manufacturers (e.g., Behringer) sell rack mount units with eight mic inputs, preamps, and an ADAT output, as a solution to conveniently add analog inputs to a computer audio interface that has an ADAT input.</p>

<p>So, if you already have a computer audio interface, and that interface has at least one ADAT output port and one ADAT input port, then you probably have an additional mulittrack recording option: Expert Sleepers offers the <a href="https://www.modulargrid.net/e/expert-sleepers-es-3-mk4">ES-3</a> module, to which you connect an ADAT cable from the ADAT OUT jack of your interface. The ES-3 receives clocking (for the ADAT signals, not for your DAW or modular) from your interface and translates eight channels of audio from your interface to the eight mono Eurorack output jacks on the ES-3. If you then attach the <a href="https://www.modulargrid.net/e/expert-sleepers-es-6-mk2">ES-6 expander module</a> to your ES-3, and connect the ES-6 via ADAT cable to the ADAT IN jack on your interface, you can also send six audio channels to your computer through the six input jacks on the ES-6. In this respect, the ES-3/ES-6 combo will enable you to record up to six tracks simultaneously in your DAW. If you additionally add the ES-7 expander to the ES-6, you can add two more inputs for a total of eight simultaneous tracks.</p>

<img src="gfx/option-es3-es6.png" class="diagram" />

<p>As per the ES-8 and ES-9, above, the ES-3/ES-6 combo offers a relatively tidy solution (two ADAT cables do it all) <em>if you already have a suitable computer audio interface</em>. Also, like the ES-8 and ES-9, the ES-3/ES-6 combo is DC coupled, meaning it can also pass CV for various purposes.</p>




<h3 id="recordermodule">Option 6: Self-contained multitrack recording within the modular itself</h3>

<p>This is a relatively new option that depends on particular capabilities of specific modules on the market.</p>
<ul>
	<li>The <a href="https://www.modulargrid.net/e/percussa-super-signal-processor">Percussa SSP</a> can record up to sixteen (mono) tracks direct to disk</li>
	<li>The Expert Sleepers <a href="https://www.modulargrid.net/e/expert-sleepers-disting-ex">Disting EX</a> can record up to six (mono) tracks direct to disk</li>
	<li>The Orthogonal Devices <a href="https://www.modulargrid.net/e/orthogonal-devices-er-301-sound-computer">ER-301</a> can record 4 tracks of audio direct to disk (technicaly, it can record as many as twelve tracks to disk, but there are caveats)</li>
</ul>

<img src="gfx/option-recorder-module.png" class="diagram" />

<p>These are all Eurorack modules that you simply patch your voices into. The advantage is you keep the process within the rack. The disadvantages are that you’re monopolizing modules (and the HP they consume) for recording that would otherwise be put to some musical purpose, and this approach might not be the most cost-effective. On the other hand, this approach will appeal to people who have no other “studio setup” and don’t want one.</p>




<h2>Additional considerations</h2>




<h3 id="interfaces">Computer Audio Interfaces and alternatives</h3>

<p>There’s inevitably much handwringing over interfaces, exacerbated by the constant stream of new models. The market has wildly diverse options at wildly different price points. One fundamental variable that is only loosely related to price (and physical size) is the number of analog audio inputs the device offers. Number of inputs is (obviously) relevant to multitracking your modular. However, many of the other features of an interface (mic preamps, DSP, networking) may be of little or no relevance, yet add dramatically to the cost of the product.</p>

<p>Most interfaces are rackmount or tabletop boxes (MOTU, RME, Presonus, Focusrite, Universal Audio, Apollo, Apogee, Lynx, etc.). Many analog mixing consoles offer an integrated USB audio interface for recording, but most of these are just a single stereo pair. A handful of analog mixing consoles from Soundcraft, Presonus, TASCAM (and maybe a some others) offer a full multitrack recording interface.</p>

<p>Most interfaces offer an array of 1/4" TR input jacks (and/or combo jacks) designed to accommodate a variety of instrument and microphone sources. These are what you would patch your modular to, directly or indirectly, using 1/8" to 1/4" adapters as necessary. A few interfaces have DB25 inputs—these are line level only and offer some advantages in terms of tidyness and density. In some cases (see Option 2, above), you can connect your modular directly to one of these interfaces over DB25. There are also many other ways of integrating a DB25 computer audio interface into an overall studio setup using patch bays or other gear.</p>

<p>As mentioned above, if your interface offers ADAT In <em>and</em> ADAT Out, it opens the opportunity to use modular ADAT interfaces such as the ES-3/ES-6 for multitrack recording and/or CV integration with your software. Note that ADAT tops out at 48kHz for sampling rate.</p>

<p>If you wish to completely avoid having to record to a DAW running on a personal computer, alternatives exist, mainly in the forms of “audio recorder” boxes (ZOOM, Sound Devices, JoeCo, etc.) and certain “portastudio”-type digital mixing consoles (TASCAM, ZOOM, etc.). These devices will record whatever you’re sending them directly to disk—typically to an SD Card—with no personal computer attached.</p>





<h3 id="coupling">DC-coupling</h3>

<p>In this context, DC-coupling is mainly about the ability to share low frequency CV between the modular and a computer, and not have it stripped out by capacitors in an analog circuit. DC voltage (offset) is generally undesirable with audio because it can gobble headroom and even damage circuitry that isn’t designed to handle it. However, the ability to record and play back CV signals by a DAW, transmit clock and other CV signals to/from a DAW, or otherwise integrate hardware synths with software synths based on control voltage instead of MIDI is growing in popularity. Quite a few computer audio interfaces</a> are now DC-coupled for input, output or both. (This probably-not-quite-exhaustive <a href="https://www.sweetwater.com/sweetcare/articles/which-audio-interfaces-are-dc-coupled">list from Sweetwater</a> unfortunately does not specify whether it is the input, the output, or both that is DC-coupled.) Due diligence is required. Note that all bets are off if you’re not patching your modular more or less directly to the interface.</p>

<p>If you are using an interface with DC-coupled inputs to record audio, you may also need to be thoughtful about not introducing DC offset to the audio you produce in your modular (or about countering it), if some of your modules tends to introduce offset. Some interfaces, such as the aforementioned ES-9, have optional DC-blocking filters that can be enabled/disabled for particular channels.</p>




<h3 id="postfader">Pre-fader/Post-fader recording</h3>

<p>The terms “pre-fader” and “post-fader” are a little problematic, here, but we (ab)use them for lack of a better name. Canonically, when you do multitrack recording, you’re trying to properly capture the individual “raw” elements (voices, instruments) of a performance distreetly, and you don’t worry about manipulating and mixing them until later. This is why, for example, the WMD Performance Mixer+DB25 combo passes all the channels out raw and untouched except for the gain adjustments. For the sake of this discussion, that would be “pre-fader” because the faders and panners on the WMD Performance Mixer do not influence the channels you’re recording in parallel.</p>

<p>However, some modular synthesists adamantly want to capture their performance “post-fader”, because <em>they are playing their mixer as part of the performance</em> and don’t want to have to reconstruct (re-mix) what they did later on. Basically, they want capture and bake-in some of their on-the-fly mixing decisions, while still retaining separate tracks.</p>

<p>In most of the multitrack recording options, above, this boils down to what you do in terms of patching—you patch for the result you want. Stereo mixer modules are one “bottleneck” where the design of the module can limit your options in this regard.</p>



<h2>Case studies</h2>

<p>Below are a few brief case studies to provide food for thought.</p>


<h3 id="studypragaportastudio">Two Pragas and a portastudio</h3>

<p>In this setup, two Pragas provide eight channels of signal control in the rack. Eight longish 1/8"-to-1/4" TR patch cables stretch from the individual channel outputs on the Pragas to the inputs on the TASCAM DP-24SD. These Praga outputs are post-fader, so the level knobs and mutes on the Praga are part of the recorded performance (but not the panning). The TASCAM records up to eight channels simultaneously to an SD card. No computer required.</p>

<img src="gfx/study-praga-portastudio.png" class="diagram" />




<h3 id="study4848">Small studio integration with a WMD Performance Mixer+DB25, PreSonus 4848, and a little ADAT</h3>

<p>This Eurorack system began with the WMD Performance Mixer, which was first used to live mix a stereo signal for recording. When it was time to “upgrade” to multitrack recording, the Performance Mixer was retained and the WMD DB25 expander added. A new computer audio interface was needed, and the PreSonus 4848 was selected because of its extensive DB25 support, the implication being the two DB25 snakes from the WMD DB25 Expander could be connected directly to the 4848. After doing so, the 4848 still had available 16 channels of line level input, 32 channels of line level output, and another 16 channels in and out of ADAT. A couple of DB25-to-1/4" TRS snakes is all that was required to integrate a small mixing console, which in turn handled the monitors. Eventually, an Expert Sleepers ES-3 is added to carry clock and reset from the DAW to the modular over ADAT, and later, and ES-6 could be added to that.</p>

<img src="gfx/study-pm-db25-4848.png" class="diagram" />






'''

html_bottom = '''



<p style="text-align:center;">• • •</p>

<h4>Revision History</h4>
<p class="updates">
2020-05-26 minor additions, clarifications<br />
2020-05-25 tweaks<br />
2020-05-24 rough draft<br />
</p>

</div><!-- end div.main -->

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



# build table
s = html_top

s += html_bottom

f = open('index.html','wb')
f.write(s.encode('utf-8'))
f.close()


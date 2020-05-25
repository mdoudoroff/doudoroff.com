#!/usr/bin/env python
# encoding: utf-8

import json, csv, decimal, sys

if sys.version_info[0] != 3:
    sys.exit("This script requires Python version 3")

html_top = '''
<html>
<head>
	<meta charset="utf-8">
	<title>Multitrack Recording Your Eurorack Modular Synthesizer</title>
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

img.diagram {
	height: 450px;
	width: auto;
}
</style>
<body>


<h1>Multitrack Recording Your Eurorack Modular Synthesizer</h1>


<h4>Latest</h4>
<p class="updates">
2020-05-24 rough draft<br />
<!--<span id="additionalUpdates" class="collapsed">
</span>
<a id="updatesToggle" onclick="toggleAdditionalUpdates();" href="javascript:void(0);">Show full revision history</a>-->
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

<p>This guide attempts to summarize the options and considerations for those making the move from stereo recording to multitrack recording of their Eurorack modular system. </p>

<h2>An array of options</h2>

<p>Your options will largely depend on how many tracks you wish to record concurrently from your modular, and, of course, the rest of your “studio setup”. Some of your options are most suitable for 4-6 simultaneous tracks, some sit around 8 tracks, others support even more.</p>



<h3>Option 1: directly patch the last output of each voice with a cable into your studio for recording</h3>

<p>This option is common with folks whose modular is part of a larger, mature studio context, and it is straightforward and direct: you simply run a cable from each audio signal you wish to record out of your modular to some destination where recording can happen. That might be straight into an computer audio interface, into a mixing console, into a portastudio, or into an audio recorder, possibly passing through a patch bay, effects and other equipment along the way! Typically that patch is simply accomplished with an 1/8" TR to 1/4" TR cable or a 1/8" to 1/4" adapter.</p>

<img src="gfx/option-direct.png" class="diagram" />

<p>This approach can scale from just a single mono single up to any number of mono and stereo channels, depending on what the rest of your studio setup can handle.</p>

<p>The main issue with this approach is that the Eurorack modular voltage levels are pretty hot (±10V range). Most mixing consoles have no trouble handling Eurorack voltages, but depending on the headroom of the destination to which you are patching, you may wish to run the signal through an attenuator first.</p>




<h3>Option 2: use a DB25 adapter module</h3>

<p>This option centers around some sort of Eurorack module that you patch into that takes your Eurorack signal, attenuates it to line level, and passes it out a DB25 connector, to which you attach a “snake” that carries the signals to your computer audio interface, patch bay, or other studio gear. The DB25 approach is implemented in blocks of eight channels, typically of balanced audio. The best known such solution is probably the nw2s::io module.</p>

<img src="gfx/option-db25.png" class="diagram" />

<p>The advantage to this approach is that you can deliver up eight channels of modular audio for processing and recording in the rest of your studio in a relatively tidy manner.</p>

<p>A related approach is the PM DB25 expander for the popular WMD Performance Mixer. The latter is a stereo mixer module that—fully expanded—can handle up six mono channels and four stereo channels. The PM DB25 expander delivers all those channels, plus the stereo mix out two DB25 ports—a total of sixteen line level signals of balanced audio. The PM DB25 only works with the WMD Performance mixer.</p>

<p>The advantage to the WMD Performance Mixer + DB25 approach is that you retain all the functionality of the Performance Mixer within your modular while also being able to pass all of its channels (post-gain, pre-fader, more on this below) to your studio in a relatively tidy manner.</p>





<h3>Option 3: use a stereo mixer module that provides individual channel output jacks</h3>

<p>People have various reasons for wanting a stereo mixer in their modular synthesizer to begin with, so multitrack recording will be only one of the factors why you would choose to purchase and employ any of these Eurorack stereo mixers. A few Eurorack stereo mixer modules offer <strong>individual channel outputs</strong>, which enable you to multitrack record your modular while still using the stereo mixer module in your patch. </p>

<p>We already mentioned the WMD Performance Mixer, above, which delivers individual channels (pre-fader) over line level DB25. A few other stereo mixers have individual 1/8" output jacks per track:

<ul>
	<li>Xaoc Devices Praga is a four channel stereo mixer; each channel has an individual “VCA output” which is “post-fader” (see considerations, below); you can direct patch from this jack (Eurorack signal levels) to the studio recording solution of your choice; multiple Praga modules can be connected to add additional channels</li>
	<li>similarly, Befaco Hexmix + Hexpander is a six track stereo mixer with individual channel outputs (post-fader, post-eq) for each of the six channels</li>
	<li>Frap Tools CGM is a modular Eurorack stereo mixer system, with separate modules for mono channels and stereo channels; each has a direct output (pre- or post-fader, configurable) useful for multitrack recording; pretty much any number of mono or stereo channels can be configured with enough pieces of this system</li>
</ul>

<img src="gfx/option-stereo-mixer.png" class="diagram" />






<h3>Option 4: put a computer audio interface in your modular</h3>

<p>Expert Sleepers offers two modules—the ES-8 and the ES-9—each of which embed a USB class-compliant audio interface in a Eurorack module. These modules connect to your computer over USB, and pass bidirectional digital audio between your modular and your computer. The modules themselves handle the analog-to-digital and digital-to-analog conversions.</p>

<ul>
	<li>Expert Sleepers ES-8 will send up to four audio tracks to your computer, and return eight. You can add various expansion modules to the ES-8 to send up to twelve audio tracks to your computer, and return up to 16.</li>
	<li>Expert Sleepers ES-9 will send up to fourteen audio channels to your computer and return 8. Headphone and balanced outputs are also provided.</li>
</ul>

<img src="gfx/option-es8-es9.png" class="diagram" />

<p>For multitrack recording purposes, this approach is tidy (one USB cable does it all), and appealing for those who don’t already have a suitable computer audio interface. An additional point of interest is that these modules are DC-coupled, meaning that they can pass control voltage bi-directionally in addition to audio. Some DAWs (Ableton and Bitwig, in particular) and other software (Virtual Rack, Silent Way, etc.) can employ this feature to further integrate your modular with your computer, and it is one of the most accurate ways to clock your modular from your DAW (or, perhaps, clock your DAW from your modular—your mileage may vary).</p> 

<p>If you do already have a computer audio interface, then running an ES-8 or ES-9 at the same time as a second interface may not be what you want to do. A personal computer only wants to deal with a single audio interface, so if you have more than one interface, you need a software broker to make them appear as one to the rest of the computer. This sleight of hand is easy to do on a Mac, because of the Aggregate Device feature built into the operating system. On Windows, you’ll need a utility such as ASIO4LL.</p>




<h3>Option 5: put an ADAT interface in your modular</h3>

<p>By “ADAT” we actually mean “ADAT Lightpipe”. It’s nothing new: a standard for transmitting eight channels of digital audio over a fiber optic cable. Many computer audio interfaces (and various other types of gear) offer ADAT interfaces because it’s an inexpensive, space-efficient way to handle additional channels of (digital) audio without having to also implement the ADCs, DACs and related hardware of translating those channels to and from the analog domain. Consequently, some audio equipment manufacturers (e.g., Behringer) sell rack mount units with eight mic inputs, preamps, and an ADAT output, as a solution to conveniently add analog inputs to a computer audio interface that has an ADAT input.</p>

<p>So, if you already have a computer audio interface, and that interface has at least one ADAT output port and one ADAT input port, then you probably have an additional mulittrack recording option: Expert Sleepers offers the ES-3 module, to which you connect an ADAT cable from the ADAT OUT jack of your interface. The ES-3 receives clocking (for the ADAT signals, not for your DAW or modular) from your interface and translates eight channels of audio from your interface to the eight mono Eurorack output jacks on the ES-3. If you then attach the ES-6 expander module to your ES-3, and connect the ES-6 via ADAT cable to the ADAT IN jack on your interface, you can also send six audio channels to your computer through the six input jacks on the ES-6. In this respect, the ES-3/ES-6 combo will enable you to record up to six tracks simultaneously in your DAW. If you additionally add the ES-7 expander to the ES-6, you can add two more inputs for a total of eight simultaneous tracks.</p>

<img src="gfx/option-es3-es6.png" class="diagram" />

<p>As per the ES-8 and ES-9, above, the ES-3/ES-6 combo offers a relatively tidy solution (two ADAT cables do it all) <em>if you already have a suitable computer audio interface</em>. Also, like the ES-8 and ES-9, the ES-3/ES-6 combo is DC coupled, meaning it can also pass CV for various purposes.</p>




<h3>Option 6: self-contained multitrack recording within the modular itself</h3>

<p>This is a relatively new option that depends on particular capabilities of specific modules on the market.</p>
<ul>
	<li>The Percussa SSP can record up to sixteen (mono) tracks direct to disk</li>
	<li>The Expert Sleepers Disting EX can record up to six (mono) tracks direct to disk</li>
	<li>The Orthogonal Devices ER-301 can record up to six (mono) tracks direct to disk</li>
	<li>There are a few stereo recording modules on the market, such as the Expert Sleepers Disting Mk4 and the 4MS WAV Recorder, multiples of which could theoretically be used in concert to record more channels concurrently, although they would be doing so to separate SD cards</li>
</ul>

<img src="gfx/option-recorder-module.png" class="diagram" />

<p>These are all Eurorack modules that you simply patch your voices into. The advantage is you keep the process within the rack. The disadvantages are that you’re monopolizing modules (and the HP they consume) for recording that would otherwise be put to some musical purpose, and this approach might not be the most cost-effective. On the other hand, this approach will appeal to people who have no other “studio setup” and don’t want one.</p>




<h2>Considerations</h2>




<h3>Computer Audio Interfaces and alternatives</h3>

<p>There’s inevitably much handwringing over interfaces, exacerbated by the constant stream of new models. The market has wildly diverse options at wildly different price points. One fundamental variable that is only loosely related to price (and physical size) is the number of analog audio inputs the device offers. Number of inputs is (obviously) relevant to multitracking your modular. However, many of the other features of an interface (mic preamps, DSP, networking) may be of little or no relevance, yet add dramatically to the cost of the product.</p>

<p>Most interfaces are rackmount or tabletop boxes (MOTU, RME, Presonus, Focusrite, Universal Audio, Apollo, Apogee, Lynx, etc.). Many analog mixing consoles offer an integrated USB audio interface for recording, but most of these are just a single stereo pair. A handful of analog mixing consoles from Soundcraft, Presonus, TASCAM (and maybe a some others) offer a full multitrack recording interface.</p>

<p>Most interfaces offer an array of 1/4" TR input jacks (and/or combo jacks) designed to accommodate a variety of instrument and microphone sources. These are what you would patch your modular to, directly or indirectly, using 1/8" to 1/4" adapters as necessary. A few interfaces have DB25 inputs—these are line level only and offer some advantages in terms of tidyness and density. In some cases (see Option 2, above), you can connect your modular directly to one of these interfaces over DB25. There are also many other ways of integrating a DB25 computer audio interface into an overall studio setup using patch bays or other gear.</p>

<p>As mentioned above, if your interface offers ADAT In <em>and</em> ADAT Out, it opens the opportunity to use modular ADAT interfaces such as the ES-3/ES-6 for multitrack recording and/or CV integration with your software. Note that ADAT tops out at 48kHz for sampling rate.</p>

<p>If you wish to completely avoid having to record to a DAW running on a personal computer, alternatives exist, mainly in the forms of “audio recorder” boxes (ZOOM, Sound Devices, JoeCo, etc.) and certain “portastudio”-type digital mixing consoles (TASCAM, ZOOM, etc.). These devices will record whatever you’re sending them directly to disk—typically to an SD Card—with no personal computer attached.</p>





<h3>DC-Coupling</h3>

<p>In this context, DC-Coupling is mainly about the ability to share low frequency CV between the modular and a computer, and not have it stripped out by capacitors in an analog circuit. DC voltage (offset) is generally undesirable with audio because it can gobble headroom and even damage circuitry that isn’t designed to handle it. However, the ability to record and play back CV signals by a DAW, transmit clock and other CV signals to/from a DAW, or otherwise integrate hardware synths with software synths based on control voltage instead of MIDI is growing in popularity. Quite a few computer audio interfaces</a> are now DC-coupled for input, output or both. (This probably-not-quite-exhaustive <a href="https://www.sweetwater.com/sweetcare/articles/which-audio-interfaces-are-dc-coupled">list from Sweetwater</a> unfortunately does not specify whether it is the input, the output, or both that is DC-coupled.) Due diligence is required. Note that all bets are off if you’re not patching your modular more or less directly to the interface.</p>

<p>If you are using an interface with DC-coupled inputs to record audio, you may also need to be thoughtful about not introducing DC offset to the audio you produce in your modular (or about countering it), if some of your modules tends to introduce offset. Some interfaces, such as the aforementioned ES-9, have optional DC-blocking filters that can be enabled/disabled for particular channels.</p>




<h3>Pre-fader/Post-fader recording</h3>

<p>The terms “pre-fader” and “post-fader” are a little problematic, here, but we (ab)use them for lack of a better name. Canonically, when you do multitrack recording, you’re trying to properly capture the individual “raw” elements (voices, instruments) of a performance distreetly, and you don’t worry about manipulating and mixing them until later. This is why, for example, the WMD Performance Mixer+DB25 combo passes all the channels out raw and untouched except for the gain adjustments. For the sake of this discussion, that would be “pre-fader” because the faders and panners on the WMD Performance Mixer do not influence the channels you’re recording in parallel.</p>

<p>However, some modular synthesists adamantly want to capture their performance “post-fader”, because <em>they are playing their mixer as part of the performance</em> and don’t want to have to reconstruct (re-mix) what they did later on. Basically, they want capture and bake-in some of their on-the-fly mixing decisions, while still retaining separate tracks.</p>

<p>In most of the multitrack recording options, above, this boils down to what you do in terms of patching—you patch for the result you want. Stereo mixer modules are one “bottleneck” where the design of the module can limit your options in this regard.</p>


'''

html_bottom = '''





<p style="text-align:center;">• • •</p>

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


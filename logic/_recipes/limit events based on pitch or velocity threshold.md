If you patch a variable voltage signal such as pitch or velocity to a comparator, you can use the resulting gate to trigger an event, open a VCA, or gate an envelope generator whenenever the input signal is high enough or low enough.

Example:

- create a “standard” keyboard- (or sequencer-based) voice with pitch —> VCO —> filter —> VCA voice, including an ADSR (or ASR) to shape the note through the filter and/or VCA
- mult the note gate or velocity value to a comparator
- patch the output of the comparator to the CV input on a second VCA
- mult the output of the voice, above, to the second VCA’s main input
- patch the second VCA’s output to a delay effect
- combine the output of the delay effect with the voice in a mixer
- adjust the comparator to taste

Result: when you play notes that are high enough in pitch (or fast enough in velocity) they will also be passed to the delay. Notes that are too low in pitch (or slow enough in velocity) will not be passed to the delay. 

Video example (begins at 15:36	):

<iframe width="560" height="315" src="https://www.youtube.com/embed/_wCqnEgUtmk?start=936" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



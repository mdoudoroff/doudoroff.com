If you patch the note gate from a keyboard or sequencer to a rise/fall detector, you can use the resulting trigger or gate to make something else happen (play a sample, strike a low-pass gate, fire off another envelope, etc.) upon note onset and/or releases.

Note: rise/fall detection is uncommon as a standalone, exposed utility feature.

Example:

- create a “standard” keyboard- (or sequencer-based) voice with pitch —> VCO —> filter —> VCA voice, including an ADSR (or ASR) to shape the note through the filter and/or VCA
- mult the keyboard/sequencer gate to the rise/fall detector
- patch the output of the detector to the strike input on an LPG
- patch a noise source to the LPG
- combine the output of the LPG and the voice in a mixer

Result: depending on whether you’re detecting rise, fall or both, a percussive element is added to the start and/or end of each note played

Video example (begins at 11:37):

<iframe width="560" height="315" src="https://www.youtube.com/embed/_wCqnEgUtmk?start=697" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



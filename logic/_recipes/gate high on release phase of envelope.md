If you patch a copy of the gate you send an ADSR (or ASR) envelope to the input on a NOR circuit, the NOR output will be low when your gate is high and high when your gate is low. This NOR output patched to, say, a VCA, allows you to do things to your voice that only manifest during note release.

Note: NOR is the inverse of OR; some logic modules don’t explicitly offer a NOR output, but they offer an INVERSE output, so if you use the OR circuit, taking the INVERSE output is the same as NOR.

Example:

- create a “standard” keyboard- (or sequencer-based) voice with pitch —> VCO —> filter —> VCA voice, including an ADSR (or ASR) to shape the note through the VCA
- mult the keyboard/sequencer gate to a NOR circuit and patch the NOR output to a second VCA
- patch a clocked sample & hold or other rapidly changing signal to the input on the second VCA
- patch the output of the second VCA to filter cutoff

Result: when you play a note, the filter cutoff is modulated only during the release phase of the envelope. (Technically, the filter cutoff is modulating constantly whenever the note is off, but you should not hear that unless the voice isn’t completely silenced by the first VCA after the note release.)

Video example (begins at 3:34):

<iframe width="560" height="315" src="https://www.youtube.com/embed/_wCqnEgUtmk?start=214" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



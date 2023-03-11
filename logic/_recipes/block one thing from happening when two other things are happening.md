You can mult gates for two or more event streams into a NAND circuit, and circuit will output a high signal except when two input gates happen to overlap. In this way, you can silence a third activity when two other activities are already happening coincidentally.

Example:

- patch copies of two distinct gate streams from two melodic sequences to a NAND circuit
- patch the output of the NAND circuit to control a VCA (or to the input of a separate AND circuit)
- patch a trigger rhythm destined for a percussion voice to the input of the VCA (or the other input on the separate AND circuit) and patch the output to the percussion voice

Result: the percussion will trigger normally whenever neither *or* one of two melodic sequences is playing a note, but will be silent when both sequences are playing notes simultaneously.


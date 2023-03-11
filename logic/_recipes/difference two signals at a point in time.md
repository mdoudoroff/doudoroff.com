You can patch two signals to a DIFF circuit and get a voltage at the output that reflects the magnitude of the difference between the two input voltages. Optionally, you can then use a sample and hold to capture the moment you’re interested in.

Aside: you can patch your own DIFF circuit with an inverter, mixer, and full wave rectifier. Pass one of the two signals you wish to DIFF through the inverter, combine the two signals in the mixer at unity gain, then patch the mix through the full wave rectifier.

Example:

- patch two unsync’d LFOs into a DIFF circuit
- patch the output to a sample & hold module’s signal input
- patch a clock to the sample & hold trigger input

Result: the sample & hold output will update at each clock pulse with a voltage representation of the difference between the two signals at the time

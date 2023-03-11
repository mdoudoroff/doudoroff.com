You can get the lower of two continuous voltage values by passing them through a MIN (analog AND) circuit. Optionally, you can employ a sample and hold to capture the moment you’re interested in.

Example:

- patch two unsync’d LFOs into a MIN (AND) circuit
- patch the output to a sample & hold module’s signal input
- patch a clock to the sample & hold trigger input

Result: the sample & hold output will update at each clock pulse with whichever input voltage was lower at the time

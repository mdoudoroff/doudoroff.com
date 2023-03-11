You can get the higher/larger of two continuous voltage values by passing them through a MAX (analog OR) circuit. Optionally, you can employ a sample and hold to capture the moment you’re interested in.

Note: with some MAX circuits, this procedure only works for positive voltages

Example:

- patch two unsync’d LFOs into a MAX (OR) circuit
- patch the output to a sample & hold module’s signal input
- patch a clock to the sample & hold trigger input

Result: the sample & hold output will update at each clock pulse with whichever input voltage was higher at the time

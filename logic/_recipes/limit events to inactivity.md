You can use a comparator to allow or disallow other events (such as advancing a sequencer) based on activity elsewhere in your patch.

The requirement is a comparator that can be set to output a high gate when the incoming voltage drops to 0V (or lower).

Example:

- mult the envelopes (or other dynamic signals) from one or more voices to a mixer
- patch the sum (or the logical OR/maximum, if your mixer has that feature) to the input on your comparator
- configure the comparator so that its output will be high when the input is 0V or lower
- patch the comparator output to the clock input on a sequencer (or patch it to control a VCA through which a trigger or clock stream is flowing)

Result: when the combined signal activity monitored by the comparator is at a lull, something else can happen/move forward



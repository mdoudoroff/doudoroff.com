Gate-to-trigger conversion is not a logic operation, per se, but it can be a necessary logic-adjacent step.

A few multi-utility modules include a gate-to-trigger function (e.g., Klavis Two Bits, Klavis Logica XT); with these, you can patch a gate stream to the module and receive a trigger stream at the output, although these triggers may really just be gates with a very short length that you set with a parameter.

Another approach is to use a voltage controlled slew with an EOR gate output. With these, you patch a gate stream to the slew input, set RISE to very fast, and retrieve your trigger stream from the EOR output.

Another approach is to use a Doepfer A-162 Dual Trigger Delay, with the delay set to minimum and the gate length set to a minimum.

There are probably many other approaches.

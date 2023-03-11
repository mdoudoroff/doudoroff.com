You can use a three-step validation function, such as the 1,2,3 features of Klavis Logica XT, to insure that something only happens when a particular order of triggers occurs.

This could be used, for example, to determine when a rhythmic “fill” is triggered from a burst generator, based on two other rhythmic parts.

Example:

- patch mults of the gates for the first and second things (kick and snare?) to the first and second inputs
- patch the gates for the third thing (clap?) to the third input
- patch the output to the destination of the third thing

Result: a (single) gate for the third thing will only pass when a rising edge at the first input is followed by a rising edge at the second input and then a rising edge at the third input.


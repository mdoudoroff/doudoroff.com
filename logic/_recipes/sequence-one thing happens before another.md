You can use a flipflop to track whether something has happened or not, and employ the output downstream (in another logic module or VCA) to prevent something else from happening prematurely.

Note: A plain flipflop may have only one effective input and be hard to work with except as a divide-by-two. Some flipflops, such as the Set/Reset feature of Klavis Logica XT, have separate set and reset inputs.

Example:

- patch the thing that must go first—perhaps the trigger for a kick drum—into the SET input
- patch the output to another logic module or VCA (this will gate whatever must go second)
- optionally, patch the a copy of the second thing (or something else entirely) to the reset input

Result: the output will not go high until a trigger at the SET input arrives. The output will remain high until another trigger either resets or toggles the flipflop.


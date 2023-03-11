If you feed a 50% duty cycle clock into the OR of a logic module, the NOR (or inverse of OR) will go high halfway through the clock cycle (when the clock goes low), providing a convenient trigger/gate for the offbeat. If your logic module offers a NOT feature, it can be use similarly.

Example:

- patch a square wave (50% duty cycle) clock to OR
- patch NOR to trigger a percussion module

Video example (begins at 9:54):

<iframe width="560" height="315" src="https://www.youtube.com/embed/3y6uRCM-fdE?start=594" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


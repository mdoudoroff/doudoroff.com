If you combine a rhythm and a slowish 50% duty cycle clock (sync’d or unsync’d) or other stream of long-ish gates in an OR circuit, the second stream will hold the OR output high part of the time. If you’re using the OR output to trigger percussion or envelopes, this technique has the effect of muting the triggers part of the time.

Example:

- patch a rhythm to an OR circuit (can be triggers or gates)
- patch a slow square wave (50% duty cycle) clock or other relatively slow gate stream to the other OR input (must be gates)
- patch OR output to trigger a percussion module

Result: the input rhythm is chopped up/muted on a rhythmic basis by the other gatestream.

Video example (begins at 9:54):

<iframe width="560" height="315" src="https://www.youtube.com/embed/3y6uRCM-fdE?start=594" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


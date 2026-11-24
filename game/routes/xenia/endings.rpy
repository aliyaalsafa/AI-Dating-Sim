## Xenia's three endings (CLAUDE.md §7), played at the Founders' Gala.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_good_xenia(ending):
    scene bg gala
    with fade
    show xenia neutral at center
    with dissolve

    # PLACEHOLDER: Xenia good ending
    "Xenia arrives late, in a black suit with silver star earrings and one electric-blue streak. She isn't holding her phone."
    xenia "Before you say anything: yes, I own formalwear. No, I will not be taking questions."
    xenia "I didn't post anything tonight. First night in two years. My thumbs feel weird."
    "When the music starts, she doesn't roast the band. She just takes your hand and pulls you out onto the floor."
    xenia "You know what the stars taught me? Everything's farther away than it looks, and closer than you think. I used to think that was sad."
    xenia "I don't anymore. ...Okay. That's enough sincerity. You look like a lukewarm glass of water, by the way. My favorite kind."
    call ending_card(ending)
    return


label ending_sweet_xenia(ending):
    scene bg gala
    with fade
    show xenia neutral at center
    with dissolve

    # PLACEHOLDER: Xenia sweet ending
    xenia "You asked {i}me{/i}? To the gala? In front of Grace? Bold move. Yes. Obviously yes. Don't get cocky."
    "She spends half the night roasting everyone's outfits under her breath, and the other half pretending she isn't having fun."
    xenia "This is... fine. Good. It's good. I'm still not great at the whole 'feelings out loud' thing."
    xenia "But come up to the roof sometime this summer. Bring noodles. Maybe I'll read you another note."
    call ending_card(ending)
    return


label ending_friends_xenia(ending):
    scene bg gala
    with fade
    show xenia neutral at center
    with dissolve

    # PLACEHOLDER: Xenia friends ending
    xenia "Oh. Oh no. You're asking me out? Like, properly? That's so sincere. I'm breaking out in hives."
    xenia "Okay, real talk, for one second. You're one of maybe three people on this campus I actually like. I don't want to mess that up by pretending I'm somewhere I'm not."
    xenia "So... no. But not a mean no. The nicest no I've ever said. Frame it."
    xenia "Friends? Real ones? The kind that roast each other at funerals?"
    "You spend the gala on the balcony together, ranking everyone's dance moves. She gives the dean a two. She gives you an eight. She says it's the highest score she's ever given."
    call ending_card(ending)
    return

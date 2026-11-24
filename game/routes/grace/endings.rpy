## Grace's three endings (CLAUDE.md §7), played at the Founders' Gala.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_good_grace(ending):
    scene bg gala
    with fade
    show grace neutral at center
    with dissolve

    # PLACEHOLDER: Grace good ending
    "Grace arrives in a sea-green dress. She isn't carrying her planner."
    grace "For the record, I have no plan for tonight. None. I left the whole evening blank."
    grace "It's the scariest thing I've ever done, and I've given a speech to the entire faculty with a fever."
    "When the music starts, she doesn't ask if you want to dance. She just takes your hand."
    grace "I used to think I had to be everything to everyone. Turns out I just wanted to be something to someone."
    grace "Want me to— no. I know what I want."
    call ending_card(ending)
    return


label ending_sweet_grace(ending):
    scene bg gala
    with fade
    show grace neutral at center
    with dissolve

    # PLACEHOLDER: Grace sweet ending
    grace "You asked me! Yes! Obviously yes. I prepared three possible itineraries for tonight. They're laminated."
    "You dance to option two. Then option one. Then, briefly, an option she clearly invents on the spot."
    grace "This is really nice. I mean it. I'm still figuring out what I want, but I know I wanted tonight."
    grace "Next semester, maybe I'll leave a whole day blank. With you in it."
    call ending_card(ending)
    return


label ending_friends_grace(ending):
    scene bg gala
    with fade
    show grace neutral at center
    with dissolve

    # PLACEHOLDER: Grace friends ending
    grace "Oh. You're asking me? That's so kind. I'd love to say yes. I say yes to everything."
    grace "That's kind of why I'm saying no."
    grace "I think I need to figure out what I want before I go to a gala with anyone. Does that make sense?"
    grace "Can we still be friends? Like, real ones? The kind that disagree with me?"
    "You spend the gala at the snack table together, arguing about which canapés are overrated. She disagrees with you three times. She seems proud of it."
    call ending_card(ending)
    return

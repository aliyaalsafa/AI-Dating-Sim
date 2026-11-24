## Gemma's three endings (CLAUDE.md §7), played at the Founders' Gala.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_good_gemma(ending):
    scene bg gala
    with fade
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER: Gemma good ending
    "Gemma arrives in a blue dress with four hair clips: red, yellow, green, blue. She hands her phone to the coat check."
    gemma "Don't give it back until midnight. Actually, until one. Actually, don't give it back at all, I'll pick it up tomorrow."
    gemma "I want to remember tonight without looking it up later."
    "She doesn't take a single photo all night. She dances badly and enthusiastically and corrects the DJ's song trivia exactly once."
    gemma "I used to think if I finished something, it'd turn out not good enough. This isn't finished. I hope it never is. And it's already good enough."
    call ending_card(ending)
    return


label ending_sweet_gemma(ending):
    scene bg gala
    with fade
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER: Gemma sweet ending
    gemma "You're asking me? Yes! Yes. Let me look up how to— no. I know how. Yes."
    gemma "Fun fact: the first Founders' Gala was in nineteen-oh-two. Actually, nineteen-oh-four. The wiki was wrong. I'll fix it later. Not now. Maybe a little now."
    "You dance while she live fact-checks the gala's welcome speech under her breath. Grace's speech gets three corrections. Grace looks delighted anyway."
    gemma "This is nice. This is really nice. Footnote: I mean it."
    call ending_card(ending)
    return


label ending_friends_gemma(ending):
    scene bg gala
    with fade
    show gemma neutral at center
    with dissolve

    # PLACEHOLDER: Gemma friends ending
    gemma "Oh! You're asking me? That's— thank you. Really."
    gemma "I don't think I can say yes, though. I looked it up, and then I actually thought about it, which is new for me."
    gemma "You're my favorite lab buddy. I don't want to start something I'm scared I'll leave on a shelf. You're too important for the shelf."
    gemma "Still lab partners on Monday? Shen says it's more efficient with three."
    "You spend the gala by the dessert table, rating every pastry on a four-color scale. She labels the best one blue."
    call ending_card(ending)
    return

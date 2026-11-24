## Shen's three endings (CLAUDE.md §7), played at the Founders' Gala.
## PLACEHOLDER: all dialogue in this file is placeholder for the owner to rewrite.

label ending_good_shen(ending):
    scene bg gala
    with fade
    show shen placeholder at center
    with dissolve

    # PLACEHOLDER: Shen good ending
    "Shen arrives in a deep-navy dress. It's thrifted. It cost six dollars. It looks like it was made for her."
    shen "Charity shop. Second rack. I altered the hem myself. Don't tell anyone it took two tries."
    "All night, people come up to congratulate her. Not one of them mentions Grace. You keep count. So does she."
    shen "Zero comparisons. I checked. Several times."
    shen "Wait. Let me reconsider. That's not why tonight is good. Tonight is good because you're here."
    "When the music starts, she pulls you onto the floor without a single wasted step."
    call ending_card(ending)
    return


label ending_sweet_shen(ending):
    scene bg gala
    with fade
    show shen placeholder at center
    with dissolve

    # PLACEHOLDER: Shen sweet ending
    shen "Yes."
    shen "That was too short. Let me expand. Yes, I'll go with you. I already budgeted for it. Just in case."
    "She dances like she studies: precisely, efficiently, and with a slight frown of concentration. She steps on your foot once and apologizes in exactly four words."
    shen "This is nice. I'm still figuring out how much time I'm allowed to spend not working."
    shen "Current estimate: more than this. Let's keep testing."
    call ending_card(ending)
    return


label ending_friends_shen(ending):
    scene bg gala
    with fade
    show shen placeholder at center
    with dissolve

    # PLACEHOLDER: Shen friends ending
    shen "Let me think about it properly. You deserve the full reasoning."
    shen "You're kind. You're good company. You helped me when you didn't have to."
    shen "But I don't feel that way. I checked. My answer is no. I'm sorry. I mean the sorry."
    shen "Friends, though. That's a yes. That one I'm sure of."
    "You spend the gala at the dessert table together. She rates every pastry on value for money, and wraps two in a napkin for later."
    call ending_card(ending)
    return

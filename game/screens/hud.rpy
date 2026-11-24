## Calendar HUD (CLAUDE.md §5): day, time slot, money, phone button.

screen hud():
    zorder 50

    frame:
        xpos 24
        ypos 20
        padding (28, 12)
        background Solid("#fff6fbe6")
        hbox:
            spacing 36
            text "Day [gs.day] / [RULES.semester_days]" size 30 color "#3a1640" bold True
            text slot_label() size 30 color "#b0306a"
            text "Cash: [gs.money]" size 30 color "#3a1640"

    # One row, so the buttons never overlap at large text sizes.
    hbox:
        xalign 1.0
        xoffset -24
        ypos 20
        spacing 12
        use playtest_button
        use phone_button


screen phone_button():
    textbutton "Phone":
        padding (28, 12)
        background Solid("#3a1640")
        hover_background Solid("#b0306a")
        text_color "#fff6fb"
        text_size 30
        action [Function(sfx, "phone"), Show("phone")]

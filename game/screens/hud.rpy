## Calendar HUD (CLAUDE.md §5): day, time slot, money, phone button.

define SLOT_ICONS = {"morning": "☀", "afternoon": "☁", "evening": "☾", "night": "✦"}

screen hud():
    zorder 50

    hbox:
        xpos 22
        ypos 18
        spacing 10

        frame:
            background ui_pill("plum")
            padding (30, 8, 30, 12)
            hbox:
                spacing 10
                text "DAY" size 24 color THEME_PINK_LIGHT yalign 0.6
                text "[gs.day]" size 40 color "#ffffff" outlines OUTLINE_SMALL
                text "/ [RULES.semester_days]" size 24 color THEME_PINK_LIGHT yalign 0.6

        frame:
            background ui_pill("white")
            padding (26, 10, 30, 14)
            hbox:
                spacing 10
                text SLOT_ICONS[SLOTS[gs.slot]] size 30 color THEME_HOT yalign 0.5
                text slot_label() size 28 color THEME_PLUM yalign 0.5

        frame:
            background ui_pill("gold")
            padding (26, 10, 30, 14)
            text "$ [gs.money]" size 28 color "#ffffff" outlines [(3, "#b77900", 0, 0)] yalign 0.5

    # One row, so the buttons never overlap at large text sizes.
    hbox:
        xalign 1.0
        xoffset -22
        ypos 18
        spacing 12
        use playtest_button
        use phone_button


screen phone_button():
    button at pop_hover:
        background ui_pill("pink")
        hover_background ui_pill("violet")
        padding (24, 8, 30, 12)
        action [Function(sfx, "phone"), Show("phone")]
        hbox:
            spacing 10
            add "gui/theme/heart_small.png" at heart_beat yalign 0.5
            text "Phone" size 30 color "#ffffff" outlines OUTLINE_SMALL yalign 0.5

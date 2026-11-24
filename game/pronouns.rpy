## Player pronouns (owner decision: the player chooses). Asked right after the
## name in the prologue; changeable later from Preferences while in a game.
##
## Writing lines about the player in the third person: use the attributes of
## `pn`, e.g. "[pn.They] [pn.are] new here." -> "They are new here." /
## "She is new here." Attributes: they them their theirs themself are were have
## do s (verb ending: "" for they, "s" for she/he: "[pn.they] walk[pn.s]"),
## plus capitalized They Them Their Theirs Themself.

init -4 python:

    class Pronouns(object):
        """Pickles with saves. Plural verb agreement follows the subject pronoun."""

        def __init__(self, they="they", them="them", their="their", theirs="theirs",
                     themself="themself", plural=True):
            self.they, self.them, self.their, self.theirs, self.themself = they, them, their, theirs, themself
            self.plural = plural

        @property
        def are(self): return "are" if self.plural else "is"
        @property
        def were(self): return "were" if self.plural else "was"
        @property
        def have(self): return "have" if self.plural else "has"
        @property
        def do(self): return "do" if self.plural else "does"
        @property
        def s(self): return "" if self.plural else "s"

        They = property(lambda self: self.they[:1].upper() + self.they[1:])
        Them = property(lambda self: self.them[:1].upper() + self.them[1:])
        Their = property(lambda self: self.their[:1].upper() + self.their[1:])
        Theirs = property(lambda self: self.theirs[:1].upper() + self.theirs[1:])
        Themself = property(lambda self: self.themself[:1].upper() + self.themself[1:])

        def label(self):
            return "%s/%s" % (self.they, self.them)

    PRONOUN_PRESETS = [
        Pronouns(),                                                   # they/them (default)
        Pronouns("she", "her", "her", "hers", "herself", plural=False),
        Pronouns("he", "him", "his", "his", "himself", plural=False),
    ]

    def custom_pronouns():
        """Ask for each form; blank answers keep the they/them form."""
        def ask(prompt, default):
            v = renpy.input(prompt, default=default, length=16).strip().lower()
            return v or default
        they = ask("Subject pronoun (e.g. they, xe):", "they")
        them = ask("Object pronoun (e.g. them, xem):", "them")
        their = ask("Possessive (e.g. their, xyr):", "their")
        theirs = ask("Possessive, standalone (e.g. theirs, xyrs):", "theirs")
        themself = ask("Reflexive (e.g. themself, xemself):", "themself")
        plural = renpy.display_menu([
            ("Verbs like \"%s are\"" % they, True),
            ("Verbs like \"%s is\"" % they, False),
        ])
        return Pronouns(they, them, their, theirs, themself, plural)

    def copy_pronouns(p):
        return Pronouns(p.they, p.them, p.their, p.theirs, p.themself, p.plural)

    def set_custom_pronouns():
        """From a menu screen: ask in a fresh context, then store the result."""
        store.pn = renpy.invoke_in_new_context(custom_pronouns)

default pn = Pronouns()


## in_menu=True: opened from Preferences; sets `pn` directly instead of returning.
screen pronoun_picker(in_menu=False):
    modal True
    zorder 200
    add Solid("#3a164077")
    frame at notify_pop:
        xalign 0.5
        yalign 0.45
        xsize 900
        padding (60, 46, 60, 50)
        background ui_panel("panel")
        vbox:
            spacing 18
            xfill True
            use heading("Your pronouns", 54)
            text "Used whenever someone talks about you. You can change them later in Preferences." size 26 color THEME_MUTED xalign 0.5 text_align 0.5
            null height 6
            for p in PRONOUN_PRESETS:
                hbox:
                    xalign 0.5
                    if in_menu:
                        use pill_button(p.label(), [SetVariable("pn", copy_pronouns(p)), Hide("pronoun_picker")], "pink", 34, True, 420)
                    else:
                        use pill_button(p.label(), Return(p), "pink", 34, True, 420)
            hbox:
                xalign 0.5
                if in_menu:
                    use pill_button("Custom…", [Function(set_custom_pronouns), Hide("pronoun_picker")], "white", 32, True, 420)
                else:
                    use pill_button("Custom…", Return("custom"), "white", 32, True, 420)


label choose_pronouns:
    call screen pronoun_picker
    if _return == "custom":
        $ pn = custom_pronouns()
    else:
        $ pn = copy_pronouns(_return)
    return

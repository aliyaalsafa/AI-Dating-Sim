"""Player pronouns (game/pronouns.rpy): verb agreement and capitalization."""

import os
import re
import textwrap

GAME = os.path.join(os.path.dirname(__file__), "..", "game")


def load_pronouns():
    src = open(os.path.join(GAME, "pronouns.rpy"), encoding="utf-8").read()
    block = re.search(r"^init -4 python:\n((?:[ \t]+[^\n]*\n|\n)+)", src, re.M).group(1)
    ns = {}
    exec(textwrap.dedent(block).split("    def custom_pronouns")[0].split("def custom_pronouns")[0], ns)
    return ns


def test_presets_and_agreement():
    ns = load_pronouns()
    they, she, he = ns["PRONOUN_PRESETS"]
    assert (they.label(), she.label(), he.label()) == ("they/them", "she/her", "he/him")
    assert (they.are, she.are, he.have, they.s, she.s) == ("are", "is", "has", "", "s")
    assert she.Their == "Her" and they.Themself == "Themself"


def test_custom_singular_neopronoun():
    ns = load_pronouns()
    xe = ns["Pronouns"]("xe", "xem", "xyr", "xyrs", "xemself", plural=False)
    assert "%s %s here" % (xe.They, xe.are) == "Xe is here"
    assert xe.label() == "xe/xem"

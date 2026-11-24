## Entry point. M0: a "hello world" scene proving the engine, placeholder art,
## the pure-Python sim package, and the web build all work.

init python:
    import sim

label start:

    scene bg quad
    with fade

    narrator "Welcome to [SCHOOL_NAME]."

    $ player_name = renpy.input("What's your name?", length=20).strip() or "You"

    show grace placeholder at center
    with dissolve

    # PLACEHOLDER: Grace's first line, rewrite in the owner's voice.
    grace "Great question — wait, you didn't ask one. Hi, [player_name]! I'm the student body president."

    # PLACEHOLDER: Grace's first line, rewrite in the owner's voice.
    grace "Want me to: 1) give you a tour, 2) give you a map, or 3) give you a tour {i}and{/i} a map?"

    narrator "(Hello world! Sim engine v[sim.SIM_VERSION] loaded.)"

    return

## Accessibility settings (CLAUDE.md §8 M5). The preferences screen exposes
## these alongside Ren'Py's built-ins (text speed, auto-forward, self-voicing,
## Shift+A accessibility menu). Font size and line spacing use Ren'Py's own
## accessibility scaling, so they apply to every piece of text.

define ACCESS_TEXT_SIZES = [1.0, 1.15, 1.3, 1.5]
define ACCESS_LINE_SPACINGS = [1.0, 1.2, 1.4]

default persistent.textbox_opacity = 1.0

init -1 python:

    def textbox_background(st, at):
        alpha = max(0.0, min(1.0, persistent.textbox_opacity))
        return Transform(Frame("gui/theme/textbox.png", 60, 60, 60, 60), alpha=alpha), 0.25

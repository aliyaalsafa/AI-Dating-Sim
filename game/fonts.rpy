## Font setup. DejaVu Sans (Ren'Py's default) has no CJK glyphs, so Chinese
## characters (Shen's name, 沈寻) fall back to WenQuanYi Micro Hei, which ships
## inside Ren'Py. See CREDITS.md.

init -100 python:

    def cjk_fallback(base):
        return (
            FontGroup()
            .add("_WenQuanYiMicroHei.woff2", 0x2E80, 0x9FFF)   # CJK radicals .. unified ideographs
            .add("_WenQuanYiMicroHei.woff2", 0x3000, 0x303F)   # CJK punctuation
            .add("_WenQuanYiMicroHei.woff2", 0xFF00, 0xFFEF)   # full-width forms
            .add(base, 0x0000, 0xFFFF)
        )

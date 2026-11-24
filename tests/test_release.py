"""Release safety checks (CLAUDE.md §8 M6, RELEASE.md)."""

import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).parent.parent
GAME = ROOT / "game"


def test_playtest_is_not_hard_coded_on():
    src = (GAME / "playtest.rpy").read_text(encoding="utf-8")
    m = re.search(r"^define PLAYTEST = (.+)$", src, re.M)
    assert m, "PLAYTEST define missing"
    assert m.group(1).strip() != "True"
    assert "config.developer" in m.group(1) and "playtest_enabled.txt" in m.group(1)


def test_playtest_flag_is_never_committed():
    assert "/game/playtest_enabled.txt" in (ROOT / ".gitignore").read_text(encoding="utf-8")
    tracked = subprocess.run(["git", "ls-files", "game/playtest_enabled.txt"], cwd=ROOT,
                             capture_output=True, text=True).stdout.strip()
    assert tracked == ""


def test_only_pages_build_enables_playtest():
    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    assert "playtest_enabled.txt" in pages
    assert "playtest_enabled.txt" not in release
    assert "playtest_enabled.txt" in (ROOT / "scripts/build_release.sh").read_text(encoding="utf-8")


def test_version_is_semver():
    src = (GAME / "options.rpy").read_text(encoding="utf-8")
    m = re.search(r'^define config.version = "([^"]+)"', src, re.M)
    assert m and re.fullmatch(r"\d+\.\d+\.\d+", m.group(1))


def test_repo_only_files_are_excluded_from_builds():
    src = (GAME / "options.rpy").read_text(encoding="utf-8")
    for pattern in ("tests/**", "scripts/**", "**.md", ".github/**", "web-build/**",
                    "dists/**", "*.zip", "game/**.rpy"):
        assert "build.classify('%s', None)" % pattern in src, pattern
    assert "build.classify('game/**.rpyc', 'scripts')" in src


def test_save_directory_is_pinned():
    """Changing it after release would orphan players' saves."""
    src = (GAME / "options.rpy").read_text(encoding="utf-8")
    assert 'define config.save_directory = "AIDatingSim-1795488577"' in src


def test_model_subtitle_switch_exists():
    assert re.search(r"^\s*SHOW_MODEL_SUBTITLES = (True|False)$",
                     (GAME / "config_names.rpy").read_text(encoding="utf-8"), re.M)
    assert "if SHOW_MODEL_SUBTITLES:" in (GAME / "screens/phone.rpy").read_text(encoding="utf-8")

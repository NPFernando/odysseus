"""Accessibility contract for the icon-only primary navigation rail."""

from pathlib import Path


_REPO = Path(__file__).resolve().parents[1]
_INDEX = (_REPO / "static" / "index.html").read_text(encoding="utf-8")


def test_icon_rail_buttons_have_programmatic_names():
    expected_labels = {
        "rail-search-btn": "Search conversations",
        "rail-new-session": "New chat",
        "rail-delete-session": "Delete current chat",
        "rail-chats": "Chat ready",
        "rail-documents": "Documents",
        "rail-calendar": "Calendar",
        "rail-compare": "Compare models",
        "rail-cookbook": "Cookbook",
        "rail-research": "Deep research",
        "rail-email": "Email",
        "rail-gallery": "Gallery",
        "rail-archive": "Library",
        "rail-memory": "Brain",
        "rail-notes": "Notes",
        "rail-tasks": "Tasks",
        "rail-theme": "Theme",
        "rail-settings": "Settings",
    }

    for button_id, label in expected_labels.items():
        assert f'id="{button_id}"' in _INDEX
        assert f'id="{button_id}" aria-label="{label}"' in _INDEX


def test_icon_rail_has_visible_keyboard_focus_treatment():
    """Icon-only controls need an explicit focus cue beyond hover styling."""
    style = (_REPO / "static" / "style.css").read_text(encoding="utf-8")

    assert ".icon-rail-btn:focus-visible" in style
    assert "outline: 2px solid var(--red, var(--color-error));" in style
    assert "outline-offset: 2px;" in style

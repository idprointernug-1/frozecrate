import json
from pathlib import Path

SETTINGS_FILE = Path("data/settings.json")

DEFAULT_SETTINGS = {
    "theme": "dark",
    "auto_update_check": True,
    "check_interval_minutes": 60
}

def load_settings():
    """Load settings from file or return defaults if not found."""
    if not SETTINGS_FILE.exists():
        return DEFAULT_SETTINGS.copy()
    
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return {**DEFAULT_SETTINGS, **data}
        except json.JSONDecodeError:
            return DEFAULT_SETTINGS.copy()

def save_settings(settings: dict):
    """Save settings to file."""
    SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)

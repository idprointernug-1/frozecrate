import json
from pathlib import Path

METADATA_FILE = Path("data/apps_metadata.json")

def load_metadata():
    """Load the full metadata JSON file."""
    if not METADATA_FILE.exists():
        return []
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_metadata(apps):
    """Save the metadata list back to the JSON file."""
    METADATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(apps, f, indent=2)

def get_app_metadata(app_id):
    """Get a single app's metadata by ID."""
    apps = load_metadata()
    for app in apps:
        if app["id"] == app_id:
            return app
    return None

def update_app_metadata(app_id, new_data: dict):
    """Update an app's metadata and save it."""
    apps = load_metadata()
    for i, app in enumerate(apps):
        if app["id"] == app_id:
            apps[i].update(new_data)
            save_metadata(apps)
            return True
    return False

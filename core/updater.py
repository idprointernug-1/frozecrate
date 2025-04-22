# Re-run after environment reset

from packaging import version
import requests
import subprocess

def get_latest_version_github(repo_url):
    """
    Fetches the latest release version from a GitHub repository.
    Expects a URL like: https://api.github.com/repos/OWNER/REPO/releases/latest
    """
    try:
        response = requests.get(repo_url)
        response.raise_for_status()
        data = response.json()
        return data.get("tag_name") or data.get("name")
    except Exception as e:
        print(f"Failed to fetch latest version: {e}")
        return None

def is_update_available(current_version, latest_version):
    """
    Compares two versions using PEP 440.
    """
    try:
        return version.parse(latest_version) > version.parse(current_version)
    except Exception as e:
        print(f"Version comparison failed: {e}")
        return False

def update_app(app):
    """
    Runs the update command for the app.
    Assumes the update method is the same as install (e.g., winget).
    """
    update_cmd = app.get("install_command")  # Using install command as update
    if update_cmd:
        try:
            subprocess.run(update_cmd, shell=True, check=True)
            print("Update complete.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Update failed: {e}")
            return False
    else:
        print("No update command found.")
        return False


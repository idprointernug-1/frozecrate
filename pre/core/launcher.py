# Re-executing after environment reset

import subprocess
import os

def launch_app(app):
    """
    Launches an installed application.
    The app dictionary should contain the path or launch command.
    """
    launch_cmd = app.get("launch_command")
    if not launch_cmd:
        print("No launch command provided.")
        return False

    try:
        subprocess.Popen(launch_cmd, shell=True)
        print(f"Launched: {app.get('name', 'Unknown App')}")
        return True
    except Exception as e:
        print(f"Failed to launch app: {e}")
        return False

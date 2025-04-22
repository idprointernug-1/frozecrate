from pathlib import Path
import requests
import subprocess
import os
import sys

def download_file_with_progress(url, dest_path):
    """Download a file from the given URL with a progress bar."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    bytes_downloaded = 0

    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    with open(dest_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                bytes_downloaded += len(chunk)
                done = int(50 * bytes_downloaded / total_size)
                sys.stdout.write(f"\r[{'█' * done}{'.' * (50 - done)}] {bytes_downloaded / 1024:.1f} KB")
                sys.stdout.flush()
    print("\nDownload complete.")
    return str(dest_path)

def install_app(app):
    """Install an app using the install command (for Windows)."""
    install_cmd = app.get("install_command")
    if install_cmd:
        try:
            subprocess.run(install_cmd, shell=True, check=True)
            print("Installation completed.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Installation failed: {e}")
            return False
    else:
        print("No install command provided.")
        return False

def uninstall_app(app):
    """Uninstall an app using the uninstall command (for Windows)."""
    uninstall_cmd = app.get("uninstall_command")
    if uninstall_cmd:
        try:
            subprocess.run(uninstall_cmd, shell=True, check=True)
            print("Uninstallation completed.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Uninstallation failed: {e}")
            return False
    else:
        print("No uninstall command provided.")
        return False


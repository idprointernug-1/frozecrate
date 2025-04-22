from core import metadata_handler, updater

def check_updates():
    """
    Checks all installed apps for updates.
    Returns a list of apps with available updates.
    """
    apps = metadata_handler.load_metadata()
    apps_with_updates = []

    for app in apps:
        if not app.get("installed") or not app.get("version_url"):
            continue

        current_version = app.get("version")
        latest_version = updater.get_latest_version_github(app["version_url"])

        if latest_version and updater.is_update_available(current_version, latest_version):
            app["latest_version"] = latest_version
            apps_with_updates.append(app)

    return apps_with_updates

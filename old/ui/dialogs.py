from PySide6.QtWidgets import QMessageBox

def confirm_install(parent, app_name):
    return _show_confirmation(parent, f"Install {app_name}?", "Do you want to install this app?")

def confirm_update(parent, app_name):
    return _show_confirmation(parent, f"Update {app_name}?", "A newer version is available. Proceed with update?")

def confirm_uninstall(parent, app_name):
    return _show_confirmation(parent, f"Uninstall {app_name}?", "Are you sure you want to uninstall this app?")

def _show_confirmation(parent, title, text):
    box = QMessageBox(parent)
    box.setWindowTitle(title)
    box.setText(text)
    box.setIcon(QMessageBox.Question)
    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return box.exec() == QMessageBox.Yes

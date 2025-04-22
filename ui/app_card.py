from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize

class AppCard(QWidget):
    def __init__(self, app_data, parent=None):
        super().__init__(parent)
        self.app_data = app_data
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("border: 1px solid #aaa; padding: 10px; margin: 5px;")
        layout = QHBoxLayout(self)

        # Icon
        icon_label = QLabel()
        icon_path = self.app_data.get("icon", "assets/default_icon.png")
        pixmap = QPixmap(icon_path).scaled(QSize(64, 64))
        icon_label.setPixmap(pixmap)
        layout.addWidget(icon_label)

        # App info
        info_layout = QVBoxLayout()
        name_label = QLabel(self.app_data.get("name", "Unknown App"))
        name_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        version_label = QLabel(f"Version: {self.app_data.get('version', 'N/A')}")

        info_layout.addWidget(name_label)
        info_layout.addWidget(version_label)
        layout.addLayout(info_layout)

        # Buttons
        btn_layout = QVBoxLayout()
        launch_btn = QPushButton("Launch")
        update_btn = QPushButton("Update")

        # Connect functionality later
        launch_btn.clicked.connect(lambda: print(f"Launching {self.app_data['name']}"))
        update_btn.clicked.connect(lambda: print(f"Updating {self.app_data['name']}"))

        btn_layout.addWidget(launch_btn)
        btn_layout.addWidget(update_btn)
        layout.addLayout(btn_layout)

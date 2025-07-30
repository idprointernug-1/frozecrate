from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QPushButton, QScrollArea
)
from PySide6.QtCore import Qt
import sys
from ui.app_card import AppCard
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Froze Crate")
        self.setMinimumSize(1000, 700)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignTop)

        self.title = QLabel("Froze Crate - Open Source Creative Suite")
        self.title.setObjectName("title")  # For styling in QSS
        self.layout.addWidget(self.title)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll.setWidget(self.scroll_content)

        self.layout.addWidget(self.scroll)

        self.load_apps()

    def load_apps(self):
        try:
            with open("data/apps_metadata.json", "r", encoding="utf-8") as f:
                apps = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            apps = []

        for app in apps:
            card = AppCard(app)
            self.scroll_layout.addWidget(card)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

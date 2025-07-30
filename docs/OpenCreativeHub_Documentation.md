# Open Creative Hub

A fullscreen PySide6-based desktop application designed as an open-source alternative to Adobe Creative Cloud. It serves as a unified launcher and updater for open-source creative tools such as GIMP, Blender, Krita, and more.

---

## 🌟 Overview

Open Creative Hub centralizes the installation, updating, launching, and status tracking of creative open-source applications in one modern, user-friendly interface.

---

## 🎯 Features

- App Cards with install/open/uninstall/update capabilities
- Download manager with real-time speed, progress, and size
- System specs checker to determine compatibility
- Searchable grid layout of apps by category
- Update checker comparing local and remote app metadata
- Scrollable UI with collapsible sections for detailed control
- Performance panel integration (like system monitor)
- Clean, dark-themed fullscreen UI

---

## 🧱 Project Structure

```
open_creative_hub/
├── main.py                  # App entry point
├── ui/                      # UI components and layout
│   ├── main_window.py
│   ├── top_bar.py
│   ├── sidebar.py
│   ├── main_panel.py
│   ├── status_panel.py
│   └── app_card.py
├── engine/                  # Core logic and background processing
│   ├── app_manager.py
│   ├── download_manager.py
│   ├── update_checker.py
│   └── spec_checker.py
├── data/                    # Databases and system info
│   ├── app.db               # Local metadata store
│   ├── server_app.db        # Downloaded metadata from server
│   └── specs.json           # Cached system specs
├── resources/               # Static assets
│   ├── images/
│   ├── icons/
│   └── styles.qss
├── utils/                   # Helper functions
│   ├── paths.py
│   ├── logger.py
│   └── ui_helpers.py
└── README.md
```

---

## 📁 Key Files and Their Roles

### main.py
Initializes QApplication and sets up the MainWindow with dark theme and fullscreen.

### ui/
Custom PySide6 widgets and containers:
- TopBar: app icon, title, buttons, search
- Sidebar: navigation links
- MainPanel: banner and scrollable app grid
- StatusPanel: update notes and progress
- AppCard: detailed app block (install/open/status)

### engine/
Handles:
- Installing/uninstalling apps
- Threaded downloading with progress feedback
- System info checks
- Version comparison for updates

### data/
- app.db: stores app metadata locally
- server_app.db: temporary server metadata for update checks
- specs.json: cache of hardware specs

### resources/
- Static assets: logos, icons, app banners
- QSS styles for theming

### utils/
- Cross-platform path helpers
- Logging system for downloads
- UI building tools (e.g., collapsible widgets)

---

## 📦 Requirements

See requirements.txt for full install list. Includes:
- PySide6
- psutil
- requests
- tqdm
- python-dotenv
- py7zr
- aiohttp (optional for async)

---

## 🚀 Future Ideas

- Plugin system
- Cloud syncing
- Built-in marketplace
- Cross-platform binary builder

---

## 🛠 Setup

1. Clone the repo
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python main.py
   ```

---

## 🧑‍💻 Contributing

Pull requests and issue reports are welcome. Feel free to fork and adapt!
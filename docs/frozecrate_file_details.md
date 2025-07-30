# Detailed File Explanations for Frozecrate

## Root Level Files

### `main.py`
**Purpose**: Application entry point and initialization
**Contains**:
- QApplication setup and configuration
- Dark theme application
- MainWindow instantiation and display
- Global exception handling
- Command line argument parsing
- Application shutdown cleanup

### `requirements.txt`
**Purpose**: Python dependencies specification
**Contains**:
- PySide6 (GUI framework)
- psutil (system information)
- requests (HTTP requests)
- tqdm (progress bars)
- python-dotenv (environment variables)
- py7zr (7zip extraction)
- aiohttp (async HTTP - optional)

### `setup.py`
**Purpose**: Package installation and distribution
**Contains**:
- Package metadata (name, version, author)
- Dependencies specification
- Entry points definition
- Package data inclusion rules
- Build configuration

### `README.md`
**Purpose**: Project documentation and introduction
**Contains**:
- Project description and features
- Installation instructions
- Usage examples
- Contributing guidelines
- License information

### `LICENSE`
**Purpose**: Legal license for open source distribution
**Contains**:
- Full license text (MIT, GPL, Apache, etc.)
- Copyright notice
- Usage permissions and restrictions

### `.gitignore`
**Purpose**: Git version control exclusions
**Contains**:
- Python cache files (`__pycache__/`, `*.pyc`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)
- User data and logs
- Temporary files

---

## UI Directory (`ui/`)

### `__init__.py`
**Purpose**: Python package initialization
**Contains**:
- Package imports and exports
- Version information
- Common UI constants

### `main_window.py`
**Purpose**: Main application window container
**Contains**:
- QMainWindow subclass
- Window geometry and state management
- Layout initialization (top bar, sidebar, main panel)
- Menu bar and toolbar setup
- Window close event handling
- Fullscreen toggle functionality

### `top_bar.py`
**Purpose**: Application header with controls
**Contains**:
- App logo and title display
- Search bar widget
- Settings button
- Minimize/maximize/close buttons
- User profile/account area (future)
- Notification indicators

### `sidebar.py`
**Purpose**: Navigation and category selection
**Contains**:
- Category list (Creative Tools, Video, Audio, etc.)
- Navigation menu items
- Active category highlighting
- Collapsible sections
- Filter options
- Quick access buttons

### `main_panel.py`
**Purpose**: Central content display area
**Contains**:
- Scrollable app grid layout
- Banner/featured content area
- App card container management
- Grid view/list view toggle
- Loading indicators
- Empty state handling

### `status_panel.py`
**Purpose**: Progress and notification display
**Contains**:
- Download progress bars
- Update notifications
- System status indicators
- Error message display
- Background task status
- Activity log viewer

### `app_card.py`
**Purpose**: Individual application display widget
**Contains**:
- App icon, name, and description
- Install/Uninstall/Update buttons
- Version information display
- Download progress indicator
- App status (installed/available/updating)
- Quick launch functionality
- Context menu (uninstall, settings, etc.)

### `dialogs/` Directory

#### `__init__.py`
**Purpose**: Dialog package initialization
**Contains**:
- Dialog base classes
- Common dialog utilities
- Standard button configurations

#### `settings_dialog.py`
**Purpose**: Application preferences window
**Contains**:
- User preferences form
- Installation path configuration
- Update frequency settings
- Theme selection
- Download behavior options
- System integration settings

#### `about_dialog.py`
**Purpose**: Application information dialog
**Contains**:
- Version information
- Developer credits
- License information
- System specifications
- Third-party acknowledgments

#### `confirm_dialog.py`
**Purpose**: User confirmation prompts
**Contains**:
- Generic confirmation dialog
- Uninstall confirmation
- Update confirmation
- Delete data confirmation
- Custom message support

### `widgets/` Directory

#### `__init__.py`
**Purpose**: Custom widget package initialization
**Contains**:
- Widget base classes
- Common widget utilities
- Style helpers

#### `progress_widget.py`
**Purpose**: Enhanced progress bar component
**Contains**:
- Progress bar with percentage
- Speed indicator (MB/s)
- Time remaining calculation
- Pause/resume controls
- Cancel functionality

#### `search_widget.py`
**Purpose**: Advanced search functionality
**Contains**:
- Search input field
- Auto-complete suggestions
- Search filters (category, status)
- Search history
- Clear search button

#### `collapsible_widget.py`
**Purpose**: Expandable/collapsible sections
**Contains**:
- Section header with expand/collapse button
- Smooth animation transitions
- Content area management
- State persistence
- Custom styling support

---

## Engine Directory (`engine/`)

### `__init__.py`
**Purpose**: Core engine package initialization
**Contains**:
- Engine version information
- Core class exports
- Configuration constants

### `app_manager.py`
**Purpose**: Application lifecycle management
**Contains**:
- App installation logic
- App uninstallation with cleanup
- App launching functionality
- Installation path management
- App metadata handling
- Dependency checking
- License verification

### `download_manager.py`
**Purpose**: File download handling with progress
**Contains**:
- Multi-threaded download implementation
- Progress callback system
- Resume interrupted downloads
- Download queue management
- Bandwidth throttling
- Checksum verification
- Temporary file handling

### `update_checker.py`
**Purpose**: Version comparison and update detection
**Contains**:
- Local vs remote version comparison
- Update availability checking
- Change log retrieval
- Update scheduling
- Incremental update support
- Rollback functionality

### `spec_checker.py`
**Purpose**: System compatibility verification
**Contains**:
- Hardware specification detection
- Minimum requirements checking
- OS version compatibility
- Available disk space verification
- RAM and CPU requirement validation
- Graphics card detection (for 3D apps)

### `windows_installer.py`
**Purpose**: Windows-specific installation handling
**Contains**:
- .exe installer execution
- .msi package installation
- .zip portable app extraction
- Silent installation parameters
- Installation verification
- Error handling and logging

### `registry_helper.py`
**Purpose**: Windows registry operations
**Contains**:
- Registry key reading/writing
- Uninstall information management
- File association handling
- Start menu shortcut creation
- Program registration
- Registry cleanup on uninstall

### `background_tasks.py`
**Purpose**: Threaded operations management
**Contains**:
- Task queue implementation
- Worker thread pool
- Progress callback handling
- Task cancellation support
- Error propagation
- Task priority management

---

## Data Directory (`data/`)

### `databases/` Directory

#### `app.db`
**Purpose**: Local application metadata storage
**Schema**:
- Apps table (id, name, version, install_path, status)
- Categories table (id, name, description)
- Downloads table (id, app_id, date, size, duration)
- User preferences and settings

#### `server_app.db`
**Purpose**: Cached remote application metadata
**Schema**:
- Remote apps table (id, name, latest_version, download_url)
- Update information and changelogs
- Repository metadata
- Temporary cache for update checking

### `cache/` Directory

#### `downloads/`
**Purpose**: Temporary download file storage
**Contains**:
- Partially downloaded files
- Complete downloads awaiting installation
- Resume information files
- Download metadata

#### `thumbnails/`
**Purpose**: Cached application icons and screenshots
**Contains**:
- App icons in multiple sizes
- Application screenshots
- Banner images
- Thumbnail cache index

#### `temp/`
**Purpose**: General temporary file storage
**Contains**:
- Extraction temporary files
- Processing temporary files
- Log rotation backup files
- Cleanup candidate files

### `logs/` Directory

#### `app.log`
**Purpose**: Main application activity logging
**Contains**:
- Application startup/shutdown events
- User actions and interactions
- System state changes
- Performance metrics

#### `downloads.log`
**Purpose**: Download activity tracking
**Contains**:
- Download start/completion times
- Download speeds and statistics
- Failed download attempts
- Resume operations

#### `errors.log`
**Purpose**: Error and exception tracking
**Contains**:
- Exception stack traces
- System error messages
- Installation failures
- Network connectivity issues

### `user_data/` Directory

#### `settings.json`
**Purpose**: User configuration storage
**Contains**:
```json
{
  "theme": "dark",
  "auto_update": true,
  "install_path": "C:\\Program Files\\CreativeTools",
  "bandwidth_limit": 0,
  "startup_behavior": "minimize"
}
```

#### `favorites.json`
**Purpose**: User's favorite applications
**Contains**:
```json
{
  "favorites": ["gimp", "blender", "krita"],
  "recently_used": ["audacity", "gimp"],
  "hidden_apps": ["deprecated_tool"]
}
```

#### `install_paths.json`
**Purpose**: Custom installation directories
**Contains**:
```json
{
  "gimp": "C:\\Graphics\\GIMP",
  "blender": "D:\\3D\\Blender",
  "default": "C:\\Program Files\\CreativeTools"
}
```

### `specs.json`
**Purpose**: Cached system specifications
**Contains**:
```json
{
  "os": "Windows 10",
  "cpu": "Intel i7-8700K",
  "ram": "16GB",
  "gpu": "NVIDIA GTX 1060",
  "disk_space": "500GB available",
  "last_updated": "2025-07-30T10:00:00Z"
}
```

---

## Config Directory (`config/`)

### `__init__.py`
**Purpose**: Configuration package initialization
**Contains**:
- Configuration loading utilities
- Default configuration values
- Configuration validation

### `settings.py`
**Purpose**: Application settings management
**Contains**:
- Settings class definitions
- Default configuration values
- Settings validation logic
- Settings persistence methods
- Configuration migration handling

### `app_definitions/` Directory

#### `creative_tools.json`
**Purpose**: Graphics and design tool definitions
**Contains**:
```json
{
  "gimp": {
    "name": "GIMP",
    "description": "GNU Image Manipulation Program",
    "category": "Graphics",
    "website": "https://gimp.org",
    "download_url": "https://download.gimp.org/...",
    "version": "2.10.34",
    "file_size": "200MB",
    "requirements": {
      "os": "Windows 7+",
      "ram": "1GB",
      "disk": "500MB"
    }
  }
}
```

#### `video_tools.json`
**Purpose**: Video editing and 3D software definitions
**Contains**:
- Blender configuration
- DaVinci Resolve settings
- OpenToonz parameters
- Video codec requirements

#### `audio_tools.json`
**Purpose**: Audio editing software definitions
**Contains**:
- Audacity configuration
- LMMS settings
- Audio plugin information
- Audio driver requirements

#### `productivity.json`
**Purpose**: Utility and productivity tool definitions
**Contains**:
- File managers
- Text editors
- Compression tools
- System utilities

### `repositories.json`
**Purpose**: Remote repository configuration
**Contains**:
```json
{
  "primary": {
    "name": "Official Repository",
    "url": "https://api.frozecrate.com/apps",
    "priority": 1,
    "enabled": true
  },
  "community": {
    "name": "Community Repository",
    "url": "https://community.frozecrate.com/apps",
    "priority": 2,
    "enabled": false
  }
}
```

### `categories.json`
**Purpose**: Application categorization system
**Contains**:
```json
{
  "graphics": {
    "name": "Graphics & Design",
    "icon": "graphics.png",
    "description": "Image editing and graphic design tools"
  },
  "video": {
    "name": "Video & 3D",
    "icon": "video.png",
    "description": "Video editing and 3D modeling software"
  }
}
```

---

## Resources Directory (`resources/`)

### `images/` Directory

#### `logo.png`
**Purpose**: Application logo
**Specifications**: High-resolution PNG, transparent background, multiple sizes

#### `banner.png`
**Purpose**: Application banner for main panel
**Specifications**: Wide format, branded design, dark theme compatible

#### `backgrounds/`
**Purpose**: Background images and patterns
**Contains**: Gradient backgrounds, texture patterns, theme-specific backgrounds

### `icons/` Directory

#### `ui/`
**Purpose**: User interface icons
**Contains**: Settings icon, download icon, update icon, search icon, menu icons

#### `apps/`
**Purpose**: Application icons
**Contains**: Default app icon, placeholder icons, category icons

### `styles/` Directory

#### `main.qss`
**Purpose**: Main application stylesheet
**Contains**:
- Global color scheme
- Font definitions
- Base widget styling
- Layout spacing and margins

#### `dark_theme.qss`
**Purpose**: Dark theme specific styles
**Contains**:
- Dark color palette
- High contrast elements
- Dark mode optimized colors
- Theme-specific adjustments

#### `components.qss`
**Purpose**: Component-specific styling
**Contains**:
- App card styling
- Button variations
- Progress bar themes
- Dialog styling

### `fonts/`
**Purpose**: Custom font files (optional)
**Contains**: Brand fonts, icon fonts, specialized typefaces

---

## Utils Directory (`utils/`)

### `__init__.py`
**Purpose**: Utilities package initialization
**Contains**: Common utility imports, helper constants

### `paths.py`
**Purpose**: Windows path handling utilities
**Contains**:
- Path normalization functions
- Special folder detection (AppData, Program Files)
- Path validation
- Directory creation helpers
- File permission checking

### `logger.py`
**Purpose**: Logging system configuration
**Contains**:
- Logger setup and configuration
- Log rotation management
- Different log levels (DEBUG, INFO, ERROR)
- Custom log formatters
- File and console output handlers

### `ui_helpers.py`
**Purpose**: UI building and styling utilities
**Contains**:
- Common widget creation functions
- Style application helpers
- Layout management utilities
- Icon loading and caching
- Theme switching support

### `file_operations.py`
**Purpose**: File and folder manipulation
**Contains**:
- Safe file copying and moving
- Directory creation and deletion
- File extraction (zip, 7z, tar)
- File integrity checking
- Cleanup operations

### `network_utils.py`
**Purpose**: Network and download utilities
**Contains**:
- HTTP request helpers
- Connection testing
- Proxy support
- SSL certificate handling
- Network timeout management

### `system_info.py`
**Purpose**: System information gathering
**Contains**:
- Hardware detection functions
- OS version identification
- Available disk space calculation
- Memory usage monitoring
- CPU and GPU information

### `validators.py`
**Purpose**: Input validation functions
**Contains**:
- Path validation
- URL validation
- Version string parsing
- File format verification
- User input sanitization

---

## Tests Directory (`tests/`)

### `__init__.py`
**Purpose**: Test package initialization
**Contains**: Test configuration, common test utilities

### `test_engine/` Directory

#### `test_app_manager.py`
**Purpose**: Application manager testing
**Contains**:
- Installation process tests
- Uninstallation verification tests
- App launch functionality tests
- Error handling tests

#### `test_download_manager.py`
**Purpose**: Download functionality testing
**Contains**:
- Download progress tests
- Resume functionality tests
- Error recovery tests
- Multi-threaded download tests

#### `test_update_checker.py`
**Purpose**: Update detection testing
**Contains**:
- Version comparison tests
- Update availability tests
- Repository connectivity tests
- Update scheduling tests

### `test_ui/` Directory

#### `test_widgets.py`
**Purpose**: UI component testing
**Contains**:
- Widget creation tests
- User interaction tests
- Style application tests
- Layout responsiveness tests

### `fixtures/`
**Purpose**: Test data and mock objects
**Contains**:
- Sample app definitions
- Mock download files
- Test database schemas
- Fake system specifications

---

## Docs Directory (`docs/`)

### `user_guide.md`
**Purpose**: End user documentation
**Contains**:
- Installation instructions
- Feature explanations
- Troubleshooting guide
- FAQ section

### `developer_guide.md`
**Purpose**: Contributor documentation
**Contains**:
- Development setup instructions
- Code contribution guidelines
- Architecture overview
- API documentation

### `api_reference.md`
**Purpose**: Technical API documentation
**Contains**:
- Class and method documentation
- Configuration options
- Extension points
- Plugin development guide

### `screenshots/`
**Purpose**: Application screenshots
**Contains**: UI screenshots, feature demonstrations, installation steps

---

## Scripts Directory (`scripts/`)

### `build_installer.py`
**Purpose**: Windows installer creation
**Contains**:
- PyInstaller configuration
- Installer package creation
- Asset bundling
- Distribution preparation

### `update_app_db.py`
**Purpose**: Database maintenance utilities
**Contains**:
- Database schema updates
- Data migration scripts
- Database cleanup operations
- Integrity checking

### `cleanup.py`
**Purpose**: Development and maintenance cleanup
**Contains**:
- Temporary file removal
- Cache clearing
- Log rotation
- Development artifact cleanup

---

This detailed breakdown shows how each file contributes to the overall application architecture, making it easier to understand responsibilities and plan development priorities.
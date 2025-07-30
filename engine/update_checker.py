import json
import requests
import os
import shutil
from datetime import datetime, timedelta
import hashlib

# Import custom modules (assuming they exist in your project)
try:
    from json_loader import load_json
    from logger import log_event
except ImportError:
    # Fallback functions if modules don't exist
    def load_json(file_path):
        """Fallback JSON loader function"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def log_event(message, level="INFO"):
        """Fallback logger function"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")

class UpdateChecker:
    def __init__(self):
        self.remote_url = "https://www.example.com/app-data/api=1"
        self.local_db_path = "data/app.db"
        self.server_db_path = "data/server_app.db"
        self.settings_path = "settings.json"
        self.last_check_file = "data/last_update_check.json"
        
    def should_check_for_updates(self):
        """Check if 24 hours have passed since last update check"""
        try:
            settings = load_json(self.settings_path)
            
            # Check if update checker is enabled
            if not settings.get("update_checker", False):
                log_event("Update checker is disabled in settings", "INFO")
                return False
            
            # Check interval setting (default 24 hours)
            interval_hours = settings.get("update_interval_hours", 24)
            
            # Check last update time
            try:
                last_check_data = load_json(self.last_check_file)
                last_check_str = last_check_data.get("last_check")
                
                if last_check_str:
                    last_check = datetime.fromisoformat(last_check_str)
                    time_diff = datetime.now() - last_check
                    
                    if time_diff < timedelta(hours=interval_hours):
                        log_event(f"Update check skipped. Next check in {interval_hours - time_diff.total_seconds()/3600:.1f} hours", "INFO")
                        return False
                        
            except (FileNotFoundError, ValueError, KeyError):
                # If no last check file or invalid format, proceed with check
                pass
                
            return True
            
        except Exception as e:
            log_event(f"Error checking update settings: {str(e)}", "ERROR")
            return False
    
    def update_last_check_time(self):
        """Update the last check timestamp"""
        try:
            os.makedirs(os.path.dirname(self.last_check_file), exist_ok=True)
            last_check_data = {
                "last_check": datetime.now().isoformat()
            }
            with open(self.last_check_file, 'w') as f:
                json.dump(last_check_data, f, indent=2)
        except Exception as e:
            log_event(f"Error updating last check time: {str(e)}", "ERROR")
    
    def get_file_hash(self, file_path):
        """Calculate MD5 hash of a file for comparison"""
        try:
            if not os.path.exists(file_path):
                return None
                
            hash_md5 = hashlib.md5()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            log_event(f"Error calculating hash for {file_path}: {str(e)}", "ERROR")
            return None
    
    def download_remote_db(self):
        """Download the remote database file"""
        try:
            log_event("Downloading remote database...", "INFO")
            
            response = requests.get(self.remote_url, timeout=30)
            response.raise_for_status()
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.server_db_path), exist_ok=True)
            
            # Save the downloaded file
            with open(self.server_db_path, 'wb') as f:
                f.write(response.content)
                
            log_event(f"Remote database downloaded successfully to {self.server_db_path}", "INFO")
            return True
            
        except requests.exceptions.RequestException as e:
            log_event(f"Error downloading remote database: {str(e)}", "ERROR")
            return False
        except Exception as e:
            log_event(f"Unexpected error downloading database: {str(e)}", "ERROR")
            return False
    
    def compare_versions(self, app_local, app_remote):
        """Compare local and remote app versions"""
        try:
            # Compare file hashes
            local_hash = self.get_file_hash(app_local)
            remote_hash = self.get_file_hash(app_remote)
            
            if local_hash is None:
                log_event(f"Local file {app_local} not found or unreadable", "WARNING")
                return True  # Treat as update needed
                
            if remote_hash is None:
                log_event(f"Remote file {app_remote} not found or unreadable", "ERROR")
                return False  # Cannot determine, don't update
            
            files_different = local_hash != remote_hash
            
            if files_different:
                log_event(f"Files are different - Local: {local_hash}, Remote: {remote_hash}", "INFO")
            else:
                log_event("Files are identical - no update needed", "INFO")
                
            return files_different
            
        except Exception as e:
            log_event(f"Error comparing versions: {str(e)}", "ERROR")
            return False
    
    def replace_local_db(self):
        """Replace local database with downloaded server database"""
        try:
            if not os.path.exists(self.server_db_path):
                log_event("Server database file not found for replacement", "ERROR")
                return False
            
            # Backup existing local database
            if os.path.exists(self.local_db_path):
                backup_path = f"{self.local_db_path}.backup"
                shutil.copy2(self.local_db_path, backup_path)
                log_event(f"Local database backed up to {backup_path}", "INFO")
            
            # Replace local database
            shutil.copy2(self.server_db_path, self.local_db_path)
            log_event(f"Local database updated successfully", "INFO")
            
            # Clean up server database file
            os.remove(self.server_db_path)
            log_event("Temporary server database file cleaned up", "INFO")
            
            return True
            
        except Exception as e:
            log_event(f"Error replacing local database: {str(e)}", "ERROR")
            return False
    
    def check_for_updates(self):
        """Main function to check for updates and apply them if needed"""
        try:
            log_event("Starting update check...", "INFO")
            
            # Check if we should perform update check
            if not self.should_check_for_updates():
                return False
            
            # Download remote database
            if not self.download_remote_db():
                log_event("Failed to download remote database", "ERROR")
                return False
            
            # Compare versions
            needs_update = self.compare_versions(self.local_db_path, self.server_db_path)
            
            if needs_update:
                log_event("Update available - replacing local database", "INFO")
                
                if self.replace_local_db():
                    log_event("Database update completed successfully", "INFO")
                    self.update_last_check_time()
                    return True
                else:
                    log_event("Failed to replace local database", "ERROR")
                    return False
            else:
                log_event("No update needed - local database is up to date", "INFO")
                # Clean up downloaded file
                if os.path.exists(self.server_db_path):
                    os.remove(self.server_db_path)
                self.update_last_check_time()
                return False
                
        except Exception as e:
            log_event(f"Unexpected error during update check: {str(e)}", "ERROR")
            return False

def check_for_updates():
    """Convenience function to create UpdateChecker instance and check for updates"""
    checker = UpdateChecker()
    return checker.check_for_updates()

def compare_versions(app_local, app_remote):
    """Convenience function to compare two database files"""
    checker = UpdateChecker()
    return checker.compare_versions(app_local, app_remote)

if __name__ == "__main__":
    # Example usage
    check_for_updates()
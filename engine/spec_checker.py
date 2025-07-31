import os
import json
import platform
import psutil
import subprocess
import sys
from pathlib import Path

def get_cpu_info():
    """Get detailed CPU information"""
    try:
        import cpuinfo
        cpu_info = cpuinfo.get_cpu_info()
        
        return {
            "brand": cpu_info.get('brand_raw', 'Unknown'),
            "model": cpu_info.get('brand_raw', 'Unknown'),
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "base_clock_ghz": round(cpu_info.get('hz_advertised_friendly', 0) / 1_000_000_000, 2) if cpu_info.get('hz_advertised_friendly') else 0,
            "max_clock_ghz": round(cpu_info.get('hz_actual_friendly', 0) / 1_000_000_000, 2) if cpu_info.get('hz_actual_friendly') else 0
        }
    except ImportError:
        # Fallback without cpuinfo library
        return {
            "brand": platform.processor(),
            "model": platform.processor(),
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "base_clock_ghz": 0,
            "max_clock_ghz": 0
        }

def get_memory_info():
    """Get memory information"""
    memory = psutil.virtual_memory()
    
    return {
        "total_ram_gb": round(memory.total / (1024**3), 2),
        "type": "Unknown",  # Requires specialized tools to detect
        "speed_mhz": 0  # Requires specialized tools to detect
    }

def get_storage_info():
    """Get storage information"""
    storage_devices = []
    
    try:
        partitions = psutil.disk_partitions()
        processed_devices = set()
        
        for partition in partitions:
            if partition.device not in processed_devices:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    storage_devices.append({
                        "type": "Unknown",  # SSD/HDD detection requires specialized tools
                        "interface": "Unknown",
                        "capacity_gb": round(usage.total / (1024**3), 2)
                    })
                    processed_devices.add(partition.device)
                except PermissionError:
                    continue
    except Exception:
        pass
    
    return storage_devices if storage_devices else [{"type": "Unknown", "interface": "Unknown", "capacity_gb": 0}]

def get_graphics_info():
    """Get graphics information"""
    graphics = {
        "integrated": {
            "brand": "Unknown",
            "model": "Unknown"
        },
        "dedicated": {
            "brand": "Unknown",
            "model": "Unknown",
            "vram_gb": 0
        }
    }
    
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]  # Get first GPU
            graphics["dedicated"] = {
                "brand": "NVIDIA" if "nvidia" in gpu.name.lower() else "AMD" if "amd" in gpu.name.lower() else "Unknown",
                "model": gpu.name,
                "vram_gb": round(gpu.memoryTotal / 1024, 2)
            }
    except ImportError:
        pass
    
    return graphics

def get_display_info():
    """Get display information"""
    try:
        import screeninfo
        monitors = screeninfo.get_monitors()
        if monitors:
            monitor = monitors[0]  # Get primary monitor
            return {
                "size_inches": 0,  # Physical size detection requires specialized tools
                "resolution": f"{monitor.width}x{monitor.height}",
                "refresh_rate_hz": 60  # Default assumption
            }
    except ImportError:
        pass
    
    return {
        "size_inches": 0,
        "resolution": "Unknown",
        "refresh_rate_hz": 60
    }

def get_os_info():
    """Get operating system information"""
    return {
        "name": f"{platform.system()} {platform.release()}",
        "architecture": platform.architecture()[0]
    }

def get_network_info():
    """Get network information"""
    network_info = {
        "wifi": "Unknown",
        "bluetooth": "Unknown",
        "ethernet": False
    }
    
    try:
        # Check for network interfaces
        interfaces = psutil.net_if_addrs()
        for interface_name in interfaces:
            if "wifi" in interface_name.lower() or "wireless" in interface_name.lower():
                network_info["wifi"] = interface_name
            elif "ethernet" in interface_name.lower() or "eth" in interface_name.lower():
                network_info["ethernet"] = True
    except Exception:
        pass
    
    return network_info

def get_system_info():
    """Get basic system information"""
    system_info = {
        "manufacturer": "Unknown",
        "model": "Unknown",
        "type": "Desktop"  # Default assumption
    }
    
    try:
        if platform.system() == "Windows":
            # Try to get manufacturer and model from WMI
            try:
                result = subprocess.run(['wmic', 'computersystem', 'get', 'manufacturer,model'], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    if len(lines) > 1:
                        data = lines[1].strip().split()
                        if len(data) >= 2:
                            system_info["manufacturer"] = data[0]
                            system_info["model"] = ' '.join(data[1:])
            except (subprocess.TimeoutExpired, subprocess.SubprocessError):
                pass
        elif platform.system() == "Darwin":  # macOS
            try:
                result = subprocess.run(['system_profiler', 'SPHardwareDataType'], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    system_info["manufacturer"] = "Apple"
                    # Parse model from output
                    for line in result.stdout.split('\n'):
                        if 'Model Name:' in line:
                            system_info["model"] = line.split(':')[1].strip()
                            break
            except (subprocess.TimeoutExpired, subprocess.SubprocessError):
                pass
    except Exception:
        pass
    
    return system_info

def get_ports_info():
    """Get ports information (basic estimation)"""
    return {
        "usb_c": 0,  # Requires specialized detection
        "usb_a": 0,  # Requires specialized detection
        "thunderbolt_3": 0,  # Requires specialized detection
        "audio_jack": True  # Common assumption
    }

def get_battery_info():
    """Get battery information"""
    try:
        battery = psutil.sensors_battery()
        if battery:
            return {
                "capacity_wh": 0,  # Requires specialized tools
                "estimated_life_hours": f"{round(battery.secsleft / 3600, 1)} hours" if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "Unknown"
            }
    except Exception:
        pass
    
    return {
        "capacity_wh": 0,
        "estimated_life_hours": "Unknown"
    }

def get_firmware_info():
    """Get firmware/BIOS information"""
    firmware = {
        "bios_version": "Unknown",
        "bios_vendor": "Unknown"
    }
    
    try:
        if platform.system() == "Windows":
            try:
                # Get BIOS version
                result = subprocess.run(['wmic', 'bios', 'get', 'smbiosbiosversion'], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    if len(lines) > 1:
                        firmware["bios_version"] = lines[1].strip()
                
                # Get BIOS vendor
                result = subprocess.run(['wmic', 'bios', 'get', 'manufacturer'], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    if len(lines) > 1:
                        firmware["bios_vendor"] = lines[1].strip()
            except (subprocess.TimeoutExpired, subprocess.SubprocessError):
                pass
    except Exception:
        pass
    
    return firmware

def check_system_specs():
    """Main function to check and return system specifications"""
    
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    specs_file = data_dir / "specs.json"
    
    # Check if specs file already exists and is recent (less than 24 hours old)
    if specs_file.exists():
        try:
            file_age = os.path.getmtime(specs_file)
            current_time = os.path.getctime(".")
            
            # If file is less than 24 hours old, load and return existing specs
            if (current_time - file_age) < 86400:  # 24 hours in seconds
                with open(specs_file, 'r') as f:
                    print("Loading cached system specifications...")
                    return json.load(f)
        except (OSError, json.JSONDecodeError):
            pass
    
    print("Gathering system specifications...")
    
    # Collect all system information
    specs = {
        "system": get_system_info(),
        "processor": get_cpu_info(),
        "memory": get_memory_info(),
        "storage": get_storage_info(),
        "graphics": get_graphics_info(),
        "display": get_display_info(),
        "operating_system": get_os_info(),
        "network": get_network_info(),
        "ports": get_ports_info(),
        "battery": get_battery_info(),
        "firmware": get_firmware_info()
    }
    
    # Save specs to file
    try:
        with open(specs_file, 'w') as f:
            json.dump(specs, f, indent=2)
        print(f"System specifications saved to {specs_file}")
    except IOError as e:
        print(f"Warning: Could not save specs to file: {e}")
    
    return specs

def print_specs_summary(specs):
    """Print a summary of the system specifications"""
    print("\n" + "="*50)
    print("SYSTEM SPECIFICATIONS SUMMARY")
    print("="*50)
    
    print(f"System: {specs['system']['manufacturer']} {specs['system']['model']}")
    print(f"OS: {specs['operating_system']['name']} ({specs['operating_system']['architecture']})")
    print(f"CPU: {specs['processor']['brand']} ({specs['processor']['cores']} cores, {specs['processor']['threads']} threads)")
    print(f"RAM: {specs['memory']['total_ram_gb']} GB")
    print(f"Storage: {len(specs['storage'])} device(s)")
    for i, storage in enumerate(specs['storage']):
        print(f"  - Device {i+1}: {storage['capacity_gb']} GB {storage['type']}")
    print(f"Graphics: {specs['graphics']['dedicated']['brand']} {specs['graphics']['dedicated']['model']}")
    if specs['graphics']['dedicated']['vram_gb'] > 0:
        print(f"  VRAM: {specs['graphics']['dedicated']['vram_gb']} GB")
    print(f"Display: {specs['display']['resolution']} @ {specs['display']['refresh_rate_hz']}Hz")
    print("="*50)

if __name__ == "__main__":
    try:
        # Check system specifications
        system_specs = check_system_specs()
        
        # Print summary
        print_specs_summary(system_specs)
        
        # Optional: Print full specs in JSON format
        if len(sys.argv) > 1 and sys.argv[1] == "--full":
            print("\nFull specifications (JSON format):")
            print(json.dumps(system_specs, indent=2))
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error occurred while checking system specifications: {e}")
        sys.exit(1)
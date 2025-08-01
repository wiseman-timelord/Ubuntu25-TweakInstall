#!/usr/bin/env python3
# Script: `.\scripts\utility.py`

# Imports
import subprocess
import os
from typing import Dict, Tuple, Optional
import tempfile
import shutil

# Get the original user when run with sudo
SUDO_USER = os.getenv("SUDO_USER")
HOME_DIR = os.path.expanduser(f"~{SUDO_USER}") if SUDO_USER else os.path.expanduser("~")

# Folder management
USER_DIRS_FILE = os.path.join(HOME_DIR, ".config/user-dirs.dirs")

DEFAULT_DIRS = {
    "XDG_DESKTOP_DIR": f"{HOME_DIR}/Desktop",
    "XDG_DOWNLOAD_DIR": f"{HOME_DIR}/Downloads",
    "XDG_TEMPLATES_DIR": f"{HOME_DIR}/Templates",
    "XDG_PUBLICSHARE_DIR": f"{HOME_DIR}/Public",
    "XDG_DOCUMENTS_DIR": f"{HOME_DIR}/Documents",
    "XDG_MUSIC_DIR": f"{HOME_DIR}/Music",
    "XDG_PICTURES_DIR": f"{HOME_DIR}/Pictures",
    "XDG_VIDEOS_DIR": f"{HOME_DIR}/Videos"
}

def read_user_dirs() -> Tuple[str, Dict[str, str]]:
    """Read user directory configurations"""
    if not os.path.exists(USER_DIRS_FILE):
        return "No custom folder configurations found. Using defaults.", DEFAULT_DIRS.copy()
    
    user_dirs = {}
    with open(USER_DIRS_FILE, "r") as file:
        for line in file:
            if line.startswith("XDG_") and "=" in line:
                key, value = line.strip().split("=")
                user_dirs[key] = value.strip('"')
    return "Custom folder configurations loaded.", user_dirs

def save_user_dirs(updated_dirs: Dict[str, str]) -> str:
    """Save updated directory configurations"""
    lines = []
    if os.path.exists(USER_DIRS_FILE):
        with open(USER_DIRS_FILE, "r") as file:
            lines = file.readlines()
    
    with open(USER_DIRS_FILE, "w") as file:
        for line in lines:
            if not any(line.startswith(key) for key in updated_dirs):
                file.write(line)
        for key, value in updated_dirs.items():
            file.write(f'{key}="{value}"\n')
    return "User folder configurations saved."

def apply_default_dirs() -> str:
    """Reset directory configurations to defaults"""
    with open(USER_DIRS_FILE, "w") as file:
        for key, value in DEFAULT_DIRS.items():
            file.write(f'{key}="{value}"\n')
    return "Default folder configurations applied."

# System installation functions
def update_system() -> bool:
    """Update package lists"""
    try:
        subprocess.run(["sudo", "apt", "update", "-y"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Update failed: {e}")
        return False

def install_essential_tools() -> bool:
    """Install basic system tools"""
    try:
        subprocess.run([
            "sudo", "apt", "install", "-y",
            "software-properties-common",
            "vim", "nano", "curl", "wget",
            "git", "htop", "dkms", "build-essential"
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
        return False

def upgrade_system() -> bool:
    """Upgrade all packages"""
    try:
        subprocess.run(["sudo", "apt", "upgrade", "-y", "--fix-missing"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Upgrade failed: {e}")
        return False

def perform_basic_installation() -> bool:
    """Full system setup (update + tools + upgrade)"""
    return all([
        update_system(),
        install_essential_tools(),
        upgrade_system()
    ])

def setup_unattended_upgrades() -> bool:
    """Configure automatic security updates"""
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "unattended-upgrades"], check=True)
        subprocess.run(["sudo", "dpkg-reconfigure", "-plow", "unattended-upgrades"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Unattended upgrades setup failed: {e}")
        return False

# Software management
def install_kvm_packages() -> bool:
    """Install virtualization packages"""
    try:
        subprocess.run([
            "sudo", "apt", "install", "-y",
            "qemu-kvm", "libvirt-daemon-system",
            "virtinst", "virt-manager"
        ], check=True)
        subprocess.run(["sudo", "usermod", "-aG", "libvirt,kvm", os.getenv("SUDO_USER", os.getlogin())])
        subprocess.run(["sudo", "systemctl", "enable", "--now", "libvirtd"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"KVM installation failed: {e}")
        return False

def setup_software_managers() -> bool:
    """Install package managers"""
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run([
            "sudo", "apt", "install", "-y",
            "gnome-software", "synaptic", "snapd"
        ], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "--now", "snapd"])
        subprocess.run(["sudo", "ln", "-s", "/var/lib/snapd/snap", "/snap"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Software manager setup failed: {e}")
        return False

def is_tor_installed() -> bool:
    """Check if Tor Browser is installed"""
    return os.path.exists("/opt/tor-browser/Browser/start-tor-browser")

def install_tor() -> Optional[bool]:
    """Install or uninstall Tor Browser with dependency handling"""
    try:
        if is_tor_installed():
            print("\nTor Browser is already installed. Uninstalling...")
            # Remove installation directory (owned by root due to sudo in install)
            subprocess.run(["sudo", "rm", "-rf", "/opt/tor-browser"], check=True)
            # Remove desktop entry from user's home directory
            user = os.getenv("SUDO_USER", os.getlogin())
            desktop_entry = os.path.join(HOME_DIR, ".local/share/applications/tor-browser.desktop")
            if os.path.exists(desdesktop_entry):
                subprocess.run(["sudo", "-u", user, "rm", desktop_entry], check=True)
            return False  # Successful uninstall
        else:
            print("\ sabatoInstalling Tor Browser...")
            # Create installation directory
            os.makedirs("/opt/tor-browser", exist_ok=True)
            
            # Download and extract Tor Browser (per notation)
            url = "https://archive.torproject.org/tor-package-archive/torbrowser/14.5.4/tor-expert-bundle-linux-x86_64-14.5.4.tar.gz"
            subprocess.run(
                f"curl -L {url} | sudo tar -xz -C /opt/tor-browser --strip-components=1",
                shell=True, check=True
            )
            
            # Install dependencies (per notation)
            subprocess.run([
                "sudo", "apt", "install", "-y", 
                "libgtk-3-0", "libnss3", "libasound2"
            ], check=True)
            
            # Register application (per notation)
            subprocess.run([
                "sudo", "/opt/tor-browser/Browser/start-tor-browser", 
                "--register-app"
            ], check=True)
            
            return True  # Successful install
    except subprocess.CalledProcessError as e:
        print(f"Tor operation failed: {e}")
        return None

def is_opensnitch_installed() -> bool:
    """Check if OpenSnitch is installed"""
    try:
        subprocess.run(["which", "opensnitch"], check=True, 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

# Update the install hospensnitch function
def install_opensnitch() -> bool:
    """Install or uninstall OpenSnitch firewall with verification"""
    try:
        # Check if already installed
        if is_opensnitch_installed():
            print("\nOpenSnitch is already installed. Uninstalling...")
            subprocess.run(["sudo", "apt", "remove", "-y", "opensnitch", "python3-opensnitch-ui"], check=True)
            # Remove autostart entry
            autostart_file = os.path.join(HOME_DIR, ".config/autostart/opensnitch-ui.desktop")
            if os.path.exists(autostart_file):
                os.remove(autostart_file)
            return False  # Return False for uninstall

        version = "1.7.1-1"
        base_url = "https://github.com/evilsocket/opensnitch/releases/download/v1.7.1/"
        
        # Determine architecture
        arch = subprocess.check_output(["uname", "-m"]).decode().strip()
        if archipelago in ["x86_64", "amd64"]:
            pkg_arch = "amd64"
            pkg_checksum = "ab114e4be2a286891bb9ff23a142bd97c0385cc711af8ab36921534bc89106b4"
        elif arch.startswith("arm"):
            pkg_arch = "arm64" if "64" in arch else "armhf"
            pkg_checksum = "b153c57fc1c0fd80c275ecb0e35c8ae0de4450781a1380fe6588c15b560018ac"
        else:
            print(f"Unsupported architecture: {arch}")
            return False

        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Download packages with progress
        opensnitch_pkg = os.path.join(temp_dir, f"opensnitch_{version}_{pkg_arch}.deb")
        ui_pkg = os.path.join(temp_dir, "python3-opensnitch-ui_1.7.1-1_all.deb")
        
        print("Downloading OpenSnitch package...")
        subprocess.run(["wget", "--show-progress", f"{base_url}opensnitch_{version}_{pkg_arch}.deb", "-O", opensnitch_pkg], check=True)
        print("\nDownloading OpenSnitch UI package...")
        subprocess.run(["wget", "--show-progress", f"{base_url}python3-opensnitch-ui_1.7.1-1_all.deb", "-O", ui_pkg], check=True)
        
        # Verify checksums
        print("\nVerifying package integrity...")
        actual_checksum = subprocess.check_output(
            ["sha256sum", opensnitch_pkg], text=True
        ).split()[0]
        
        if actual_checksum != pkg_checksum:
            print(f"Checksum mismatch!\nExpected: {pkg_checksum}\nActual: {actual_checksum}")
            return False

        # Install packages
        print("\nInstalling packages...")
        subprocess.run([
            "sudo", "apt", "install", "-y",
            opensnitch_pkg, ui_pkg
        ], check=True)
        
        # Enable service
        subprocess.run(["sudo", "systemctl", "enable", "--now", "opensnitch"], check=True)
        
        # Configure autostart
        autostart_dir = os.path.join(HOME_DIR, ".config/autostart")
        os.makedirs(autostart_dir, exist_ok=True)
        with open(os.path.join(autostart_dir, "opensnitch-ui.desktop"), "w") as f:
            f.write("[Desktop Entry]\nType=Application\nName=OpenSnitch\nExec=opensnitch-ui\n")
        
        # Run OpenSnitch UI
        print("\nLaunching OpenSnitch UI...")
        subprocess.Popen(["opensnitch-ui"], start_new_session=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"OpenSnitch operation failed: {e}")
        return False
    except Exception as e:
        print(f"Error during OpenSnitch operation: {e}")
        return False
    finally:
        # Clean up temporary directory
        if 'temp_dir' in locals() and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

def is_notepadqq_installed():
    """
    Check if Notepadqq is installed by checking if the notepadqq command exists.
    Returns True if installed, False otherwise.
    """
    try:
        result = subprocess.run(['dpkg', '-l', 'notepadqq'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return 'ii' in result.stdout
    except subprocess.CalledProcessError:
        return False

def install_notepadqq():
    """
    Installs or uninstalls Notepadqq on Ubuntu 25.04 and configures an rsyslog filter to suppress its logs.
    Returns True for successful install, False for successful uninstall, None for failure.
    """
    try:
        is_installed = is_notepadqq_installed()
        if is_installed:
            # Uninstall Notepadqq
            subprocess.run(['apt-get', 'remove', '-y', 'notepadqq'], check=True)
            subprocess.run(['add-apt-repository', '--remove', '-y', 'ppa:notepadqq-team/notepadqq'], check=True)
            subprocess.run(['apt-get', 'update'], check=True)
            # Remove rsyslog filter
            filter_path = '/etc/rsyslog.d/10-notepadqq.conf'
            if os.path.exists(filter_path):
                os.remove(filter_path)
                subprocess.run(['systemctl', 'restart', 'rsyslog'], check=True)
            print("Notepadqq uninstalled successfully.")
            return False
        else:
            # Install Notepadqq
            subprocess.run(['add-apt-repository', '-y', 'ppa:notepadqq-team/notepadqq'], check=True)
            subprocess.run(['apt-get', 'update'], check=True)
            subprocess.run(['apt-get', 'install', '-y', 'notepadqq'], check=True)
            # Create rsyslog filter to suppress notepadqq logs
            filter_content = ':programname, contains, "notepadqq" stop\n'
            with open('/etc/rsyslog.d/10-notepadqq.conf', 'w') as f:
                f.write(filter_content)
            subprocess.run(['systemctl', 'restart', 'rsyslog'], check=True)
            print("Notepadqq installed successfully with rsyslog filter.")
            return True
    except subprocess.CalledProcessError as e:
        print(f"Error during Notepadqq operation: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during Notepadqq operation: {e}")
        return None

def is_wine_installed() -> bool:
    """Check if Wine (winehq-stable) is installed"""
    try:
        result = subprocess.run(['dpkg', '-l', 'winehq-stable'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return 'ii' in result.stdout
    except subprocess.CalledProcessError:
        return False

def install_wine_winetricks() -> Optional[bool]:
    """Install or uninstall Wine and Winetricks for Ubuntu 25.04"""
    try:
        if is_wine_installed():
            print("\nWine is already installed. Uninstalling Wine and Winetricks...")
            subprocess.run(["sudo", "apt", "remove", "-y", "winehq-stable", "winetricks"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/etc/apt/sources.list.d/winehq.list"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/etc/apt/sources.list.d/*wine*"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/etc/apt/keyrings/winehq-archive.key"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/usr/share/keyrings/winehq-archive.gpg"], check=True)
            subprocess.run(["sudo", "sed", "-i", "/winehq.org/d", "/etc/apt/sources.list"], check=True)
            subprocess.run(["sudo", "apt", "update"], check=True)
            return False
        else:
            print("\nInstalling Wine and Winetricks...")
            # Ensure 32-bit architecture is enabled
            subprocess.run(["sudo", "dpkg", "--add-architecture", "i386"], check=True)
            
            # Clean up any existing WineHQ repository files
            subprocess.run(["sudo", "rm", "-f", "/etc/apt/sources.list.d/winehq.list"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/etc/apt/sources.list.d/*wine*"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/etc/apt/keyrings/winehq-archive.key"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/usr/share/keyrings/winehq-archive.gpg"], check=True)
            subprocess.run(["sudo", "sed", "-i", "/winehq.org/d", "/etc/apt/sources.list"], check=True)
            
            # Import WineHQ GPG key
            print("Importing WineHQ GPG key...")
            key_url = "https://dl.winehq.org/wine-builds/winehq.key"
            key_file = "/etc/apt/keyrings/winehq-archive.key"
            try:
                # Download the key
                subprocess.run(["wget", "-qO", "-", key_url], stdout=open("/tmp/winehq.key", "wb"), check=True)
                # Dearmor the key to the correct location
                subprocess.run(["sudo", "gpg", "--dearmor", "-o", key_file, "/tmp/winehq.key"], check=True)
                # Clean up temporary key file
                subprocess.run(["rm", "-f", "/tmp/winehq.key"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to import WineHQ GPG key: {e}")
                return None
            
            # Verify key file exists
            if not os.path.exists(key_file):
                print(f"Error: WineHQ GPG key file not found at {key_file}.")
                return None
            
            # Add WineHQ repository for Ubuntu 25.04 (plucky)
            with open("/etc/apt/sources.list.d/winehq.list", "w") as f:
                f.write(f"deb [arch=amd64,i386 signed-by={key_file}] https://dl.winehq.org/wine-builds/ubuntu/ plucky main\n")
            
            # Update package lists
            print("Updating package lists...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            
            # Install Wine and Winetricks
            subprocess.run(["sudo", "apt", "install", "-y", "--install-recommends", "winehq-stable"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "winetricks"], check=True)
            print("Wine and Winetricks installed successfully.")
            return True
    except subprocess.CalledProcessError as e:
        print(f"Wine operation failed: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during Wine operation: {e}")
        return None

# Hardware optimization
def is_cuda_installed() -> bool:
    """Check if CUDA Toolkit is properly installed"""
    try:
        # Check nvcc existence and validity
        nvcc_check = subprocess.run(["which", "nvcc"], capture_output=True, text=True)
        if nvcc_check.returncode != 0:
            return False
            
        # Verify nvcc outputs version info
        version_check = subprocess.run(["nvcc", "--version"], capture_output=True, text=True)
        return "release" in version_check.stdout
        
    except Exception:
        return False

def install_cuda_toolkit() -> Optional[bool]:
    """Install/uninstall CUDA Toolkit for Ubuntu 25.04 using Ubuntu 24.04 repo"""
    try:
        # Pre-flight checks
        if not os.path.exists("/usr/bin/nvidia-smi"):
            print("ERROR: NVIDIA drivers not detected. Install drivers first.")
            return None
            
        if is_cuda_installed():
            print("\nUninstalling CUDA Toolkit...")
            subprocess.run([
                "sudo", "apt", "purge", "-y", 
                "cuda-toolkit*", "cuda-*", "nvidia-cuda-toolkit"
            ], check=True)
            subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
            subprocess.run(["sudo", "rm", "/etc/apt/sources.list.d/cuda*.list"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/etc/apt/trusted.gpg.d/cuda*.gpg"], check=True)
            # Clean environment variables
            subprocess.run(["sed", "-i", "/CUDA/d", f"{HOME_DIR}/.bashrc"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/etc/profile.d/cuda.sh"], check=True)
            # Remove symlinks
            subprocess.run(["sudo", "rm", "-f", "/usr/local/cuda"], check=True)
            subprocess.run(["sudo", "rm", "-f", "/usr/local/cuda-12.5"], check=True)
            subprocess.run(["sudo", "apt", "update"])
            return False
            
        # Installation process
        print("\nInstalling CUDA Toolkit for Ubuntu 25.04 using Ubuntu 24.04 repository...")
        
        # 1. Install prerequisites
        subprocess.run([
            "sudo", "apt", "install", "-y", 
            "software-properties-common", "wget"
        ], check=True)
        
        # 2. Add CUDA repository (Ubuntu 24.04 repo for 25.04 compatibility)
        cuda_version = "12-5"  # Current stable
        keyring_deb = "cuda-keyring_1.1-1_all.deb"
        
        # Use Ubuntu 24.04 repository
        repo_url = "https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb"
        
        subprocess.run(["wget", repo_url], check=True)
        subprocess.run(["sudo", "dpkg", "-i", keyring_deb], check=True)
        os.remove(keyring_deb)
        
        # 3. Install CUDA
        subprocess.run(["sudo", "apt", "update"], check=True)
        install_result = subprocess.run([
            "sudo", "apt", "install", "-y", 
            f"cuda-toolkit-{cuda_version}"
        ], capture_output=True, text=True)
        
        if install_result.returncode != 0:
            if "Secure Boot" in install_result.stderr:
                print("\nSECURE BOOT CONFLICT:")
                print("You must enroll NVIDIA's key in Secure Boot:")
                print("1. Reboot and enter BIOS")
                print("2. Enroll MOK when prompted")
                print("3. Complete installation after reboot")
            return None
            
        # 4. Post-install configuration
        # Create cuda symlink (skip if already exists)
        if not os.path.exists("/usr/local/cuda"):
            subprocess.run(["sudo", "ln", "-s", f"/usr/local/cuda-{cuda_version.replace('-','.')}", "/usr/local/cuda"], check=True)
        
        # Add to system-wide profile
        with open("/etc/profile.d/cuda.sh", "w") as f:
            f.write("#!/bin/sh\n")
            f.write("export PATH=/usr/local/cuda/bin:$PATH\n")
            f.write("export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH\n")
        subprocess.run(["sudo", "chmod", "+x", "/etc/profile.d/cuda.sh"])
        
        # Install missing components
        subprocess.run([
            "sudo", "apt", "install", "-y",
            f"cuda-nvcc-{cuda_version}", 
            f"cuda-nvrtc-dev-{cuda_version}"
        ], check=True)
        
        # 5. Verify installation
        try:
            # Check using absolute path to avoid PATH issues
            nvcc_check = subprocess.run(["/usr/local/cuda/bin/nvcc", "--version"], 
                                      capture_output=True, text=True, check=True)
            if "release" in nvcc_check.stdout:
                print("\nCUDA Toolkit successfully installed")
                print("Run 'source /etc/profile.d/cuda.sh' or reboot to apply paths")
                return True
            print("\nWARNING: nvcc found but version check failed")
            return None
        except subprocess.CalledProcessError:
            print("\nERROR: nvcc verification failed after installation")
            # Try alternative verification
            try:
                nvidia_smi = subprocess.run(["nvidia-smi"], capture_output=True, text=True, check=True)
                if "CUDA Version" in nvidia_smi.stdout:
                    print("CUDA detected through nvidia-smi but nvcc missing")
                    print("Try manually installing: sudo apt install cuda-nvcc-12-5")
                return None
            except:
                return None
            
    except subprocess.CalledProcessError as e:
        print(f"\nCUDA operation failed: {e}")
        if "404" in str(e):
            print("Repository may not be available for Ubuntu 24.04/25.04")
        return None
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return None

def amd_cpu_setup() -> bool:
    """Configure AMD CPU microcode"""
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "amd64-microcode"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"AMD CPU setup failed: {e}")
        return False

def intel_cpu_setup() -> bool:
    """Configure Intel CPU microcode"""
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "intel-microcode"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Intel CPU setup failed: {e}")
        return False

def amdgpu_non_rocm_setup() -> bool:
    """Configure AMD GPU (non-ROCm)"""
    try:
        subprocess.run([
            "sudo", "apt", "install", "-y",
            "xserver-xorg-video-amdgpu",
            "vulkan-tools", "mesa-vulkan-drivers"
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"AMD GPU setup failed: {e}")
        return False

def amdgpu_rocm_setup() -> bool:
    """Configure AMD GPU with ROCm"""
    try:
        with open("/etc/apt/sources.list.d/rocm.list", "w") as f:
            f.write("deb [arch=amd64] https://repo.radeon.com/rocm/apt/6.0 noble main\n")
        
        subprocess.run(
            "wget -qO- https://repo.radeon.com/rocm/rocm.gpg.key | "
            "sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/rocm.gpg",
            shell=True, check=True
        )
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "rocm-dkms"], check=True)
        subprocess.run([
            "sudo", "usermod", "-a", "-G",
            "video,render", os.getenv("SUDO_USER", os.getlogin())
        ])
        return True
    except subprocess.CalledProcessError as e:
        print(f"ROCm setup failed: {e}")
        return False

def nvidia_gpu_setup() -> bool:
    """Configure NVIDIA GPU drivers"""
    try:
        subprocess.run([
            "sudo", "add-apt-repository", "-y",
            "ppa:graphics-drivers/ppa"
        ], check=True)
        driver = subprocess.getoutput(
            "ubuntu-drivers devices | grep -oP 'driver : \\K\\S+' | head -1"
        ) or "nvidia-driver-550"
        
        subprocess.run([
            "sudo", "apt", "install", "-y",
            driver, "dkms"
        ], check=True)
        print("\nWARNING: Secure Boot key enrollment required after reboot!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"NVIDIA setup failed: {e}")
        return False

def arm64_firmware_setup() -> bool:
    """Configure ARM64 firmware tools"""
    try:
        subprocess.run([
            "sudo", "sed", "-i",
            "s/restricted$/restricted multiverse/",
            "/etc/apt/sources.list"
        ], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run([
            "sudo", "apt", "install", "-y",
            "qcom-firmware-extract"
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ARM64 setup failed: {e}")
        return False

def intel_gpu_setup() -> bool:
    """Configure Intel GPU drivers"""
    try:
        subprocess.run([
            "sudo", "apt", "install", "-y",
            "intel-media-va-driver-non-free"
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Intel GPU setup failed: {e}")
        return False

# System tweaks
def check_sudo_nopasswd() -> bool:
    """Check if sudo password prompt is disabled"""
    if not os.path.exists("/etc/sudoers.d/nopasswd"):
        return False
    
    user = os.getenv("SUDO_USER", os.getlogin())
    with open("/etc/sudoers.d/nopasswd", "r") as f:
        return f"{user} ALL=(ALL) NOPASSWD: ALL" in f.read()

def toggle_sudo_nopasswd() -> bool:
    """Toggle sudo password requirement"""
    try:
        user = os.getenv("SUDO_USER", os.getlogin())
        if check_sudo_nopasswd():
            subprocess.run(["sudo", "rm", "/etc/sudoers.d/nopasswd"], check=True)
            print("WARNING: Sudo password protection ENABLED")
        else:
            # Use secure temp file
            with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
                f.write(f"{user} ALL=(ALL) NOPASSWD: ALL\n")
                tmp_path = f.name
            
            subprocess.run(["sudo", "mv", tmp_path, "/etc/sudoers.d/nopasswd"], check=True)
            subprocess.run(["sudo", "chmod", "0440", "/etc/sudoers.d/nopasswd"], check=True)
            print("SECURITY WARNING: Sudo password protection DISABLED")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Sudo toggle failed: {e}")
        return False

def check_auto_login() -> bool:
    """Check if auto-login is enabled"""
    if not os.path.exists("/etc/gdm3/custom.conf"):
        return False
    
    user = os.getenv("SUDO_USER", os.getlogin())
    with open("/etc/gdm3/custom.conf", "r") as f:
        return f"AutomaticLogin={user}" in f.read()

def toggle_auto_login() -> bool:
    """Toggle automatic login"""
    try:
        user = os.getenv("SUDO_USER", os.getlogin())
        if check_auto_login():
            subprocess.run([
                "sudo", "sed", "-i",
                f"s/^AutomaticLogin={user}/#  AutomaticLogin/",
                "/etc/gdm3/custom.conf"
            ], check=True)
        else:
            subprocess.run([
                "sudo", "sed", "-i",
                f"s/^#  AutomaticLogin/AutomaticLogin={user}/",
                "/etc/gdm3/custom.conf"
            ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Auto-login toggle failed: {e}")
        return False

def check_windows_commands() -> bool:
    """Check if Windows-like commands are installed"""
    return os.path.exists("/etc/profile.d/windows_commands.sh")

def implement_windows_commands() -> bool:
    """Install Windows-like command aliases"""
    try:
        with open("/tmp/windows_commands.sh", "w") as f:
            f.write("""\
function dir() { ls -l "$@"; }
function copy() { cp -i "$@"; }
function move() { mv -i "$@"; }
function del() { rm -i "$@"; }
function md() { mkdir -p "$@"; }
function rd() { rmdir "$@"; }
function cls() { clear; }
function type() { cat "$@"; }
function where() { which "$@"; }
function echo() { printf "%s\\n" "$*"; }
function shutdown() { sudo shutdown -h now; }
function restart() { sudo shutdown -r now; }
""")
        subprocess.run([
            "sudo", "mv", "/tmp/windows_commands.sh",
            "/etc/profile.d/windows_commands.sh"
        ], check=True)
        subprocess.run([
            "sudo", "chmod", "+x",
            "/etc/profile.d/windows_commands.sh"
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Windows commands setup failed: {e}")
        return False

def check_windows_shortcuts() -> bool:
    """Check if Windows-like shortcuts (Super+E for Nautilus) are configured"""
    try:
        user = os.getenv("SUDO_USER", os.getlogin())
        uid = subprocess.check_output(["id", "-u", user]).decode().strip()
        bus_addr = f"unix:path=/run/user/{uid}/bus"
        
        # Check if Super+E is bound to Nautilus
        output = subprocess.check_output([
            "sudo", "-u", user, f"DBUS_SESSION_BUS_ADDRESS={bus_addr}",
            "gsettings", "get",
            "org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/",
            "binding"
        ], text=True).strip()
        
        return output == "'<Super>e'"
    except:
        return False

def set_windows_shortcuts() -> bool:
    """Configure Windows-like keyboard shortcuts (Super+E for Nautilus)"""
    try:
        user = os.getenv("SUDO_USER", os.getlogin())
        uid = subprocess.check_output(["id", "-u", user]).decode().strip()
        bus_addr = f"unix:path=/run/user/{uid}/bus"
        
        # Create shortcuts directory if not exists
        shortcuts_dir = f"{HOME_DIR}/.local/share/applications"
        os.makedirs(shortcuts_dir, exist_ok=True)
        
        # Configure keyboard shortcuts
        subprocess.run([
            "sudo", "-u", user, f"DBUS_SESSION_BUS_ADDRESS={bus_addr}",
            "gsettings", "set", "org.gnome.settings-daemon.plugins.media-keys",
            "custom-keybindings", "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"
        ], check=True)
        
        # Set Super+E shortcut for Nautilus
        base_path = "org.gnome.settings-daemon.plugins.media-keys.custom-keybinding"
        custom_path = "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/"
        
        subprocess.run([
            "sudo", "-u", user, f"DBUS_SESSION_BUS_ADDRESS={bus_addr}",
            "gsettings", "set", f"{base_path}:{custom_path}",
            "name", "'File Explorer'"
        ], check=True)
        
        subprocess.run([
            "sudo", "-u", user, f"DBUS_SESSION_BUS_ADDRESS={bus_addr}",
            "gsettings", "set", f"{base_path}:{custom_path}",
            "command", "'nautilus --new-window'"
        ], check=True)
        
        subprocess.run([
            "sudo", "-u", user, f"DBUS_SESSION_BUS_ADDRESS={bus_addr}",
            "gsettings", "set", f"{base_path}:{custom_path}",
            "binding", "'<Super>e'"
        ], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to set shortcuts: {e}")
        return False

def get_hang_timeout() -> int:
    """Get current GNOME hang timeout"""
    try:
        user = os.getenv("SUDO_USER", os.getlogin())
        uid = subprocess.check_output(["id", "-u", user]).decode().strip()
        output = subprocess.check_output([
            "sudo", "-u", user,
            "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + uid + "/bus",
            "gsettings", "get", "org.gnome.mutter", "check-alive-timeout"
        ], text=True).strip()
        return int(output.replace("uint32 ", "")) // 1000
    except:
        return 5  # Default 5 seconds

def adjust_hang_timeout() -> bool:
    """Adjust GNOME hang timeout"""
    try:
        current = get_hang_timeout()
        new_seconds = input(f"Enter new timeout in seconds (current: {current}, 0=disable): ").strip()
        if not new_seconds.isdigit():
            print("Invalid input. Must be a number.")
            return False
            
        new_milliseconds = int(new_seconds) * 1000
        user = os.getenv("SUDO_USER", os.getlogin())
        uid = subprocess.check_output(["id", "-u", user]).decode().strip()
        
        subprocess.run([
            "sudo", "-u", user,
            "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + uid + "/bus",
            "gsettings", "set", "org.gnome.mutter",
            "check-alive-timeout", f"uint32 {new_milliseconds}"
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Timeout adjustment failed: {e}")
        return False
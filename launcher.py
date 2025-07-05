#!/usr/bin/env python3
# Script: `.\launcher.py`

# Imports
import os
import subprocess
from scripts.interface import main_menu

def verify_ubuntu_version():
    """Check if running on Ubuntu 25.x (major version match only)"""
    try:
        version = subprocess.check_output(["lsb_release", "-rs"], text=True).strip().split('.')[0]
        version_full = subprocess.check_output(["lsb_release", "-rs"], text=True).strip()
        if version != "25":
            print("Error: This program requires Ubuntu 25.x")
            print(f"Detected version: {version}.x")
            return False
        elif version_full < "25.04":
            print("Warning: Optimized for Ubuntu 25.04+, minor issues may occur")
        return True
    except Exception as e:
        print(f"Version check failed: {e}")
        return False

if __name__ == "__main__":
    if verify_ubuntu_version():
        main_menu()
    else:
        print("Exiting due to version incompatibility.")
        exit(1)

import os
from scripts.utility import *

SEPARATOR_WIDTH = 80

def thick_separator():
    print("=" * SEPARATOR_WIDTH)

def thin_separator():
    print("-" * SEPARATOR_WIDTH)

def print_title(title):
    thick_separator()
    print(f"    Ubuntu25-TweakInstall - {title}")
    thick_separator()
    print("")

def main_menu():
    while True:
        os.system('clear')
        print_title("System Tweaks and Installer")
        print("\n\n")
        print("    1. System Installation and Updates\n\n"
              "    2. Software and Package Management\n\n"
              "    3. Hardware Optimization and Drivers\n\n"
              "    4. System Tweaks and Customizations\n\n"
              "    5. User Folder Configurations\n\n")
        print("\n")
        thin_separator()
        print("Selection; Menu Options 1-5, Exit Program = X: ", end="")
        choice = input().strip().upper()
        if choice == "1":
            system_installation_menu()
        elif choice == "2":
            software_management_menu()
        elif choice == "3":
            hardware_optimization_menu()
        elif choice == "4":
            system_tweaks_menu()
        elif choice == "5":
            user_folder_menu()
        elif choice == "X":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def system_installation_menu():
    while True:
        os.system('clear')
        print_title("System Install and Updates")
        print("    1. Perform basic system update and install essential tools\n\n")
        thin_separator()
        print("Selection; Menu Options 1-1, Back To Main = B: ", end="")
        choice = input().strip().upper()
        if choice == "1":
            os.system('clear')
            print_title("Performing Basic System Update")
            try:
                perform_basic_installation()
                print("\nBasic system update and installation completed.\n")
            except Exception as e:
                print(f"\nError during basic system update: {e}\n")
            input("Press Enter to continue...")
        elif choice == "B":
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def software_management_menu():
    while True:
        os.system('clear')
        print_title("Software and Packages")
        print("    1. Install virtualization packages (KVM, Libvirt)\n\n"
              "    2. Setup software managers (Gnome, Synaptic, Snap)\n\n"
              "    3. Install Wine and Winetricks\n\n"
              "    4. Install Python and related packages\n\n")
        thin_separator()
        print("Selection; Menu Options 1-4, Back To Main = B: ", end="")
        choice = input().strip().upper()
        if choice == "1":
            os.system('clear')
            print_title("Installing Virtualization Packages")
            try:
                install_kvm_packages()
                print("\nVirtualization packages installed.\n")
            except Exception as e:
                print(f"\nError during virtualization packages installation: {e}\n")
            input("Press Enter to continue...")
        elif choice == "2":
            os.system('clear')
            print_title("Setting Up Software Managers")
            try:
                setup_software_managers()
                print("\nSoftware managers setup completed.\n")
            except Exception as e:
                print(f"\nError during software managers setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "3":
            os.system('clear')
            print_title("Installing Wine and Winetricks")
            try:
                install_wine_winetricks()
                print("\nWine and Winetricks installed.\n")
            except Exception as e:
                print(f"\nError during Wine and Winetricks installation: {e}\n")
            input("Press Enter to continue...")
        elif choice == "4":
            os.system('clear')
            print_title("Installing Python and Related Packages")
            try:
                install_python_packages()
                print("\nPython packages installed.\n")
            except Exception as e:
                print(f"\nError during Python packages installation: {e}\n")
            input("Press Enter to continue...")
        elif choice == "B":
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def hardware_optimization_menu():
    while True:
        os.system('clear')
        print_title("Hardware and Drivers")
        print("    1. CPU Setup\n\n"
              "    2. GPU Setup\n\n"
              "    3. ARM64 Firmware (Snapdragon)\n\n")  # New option
        thin_separator()
        print("Selection; Menu Options 1-3, Back To Main = B: ", end="")
        choice = input().strip().upper()
        if choice == "1":
            cpu_setup_menu()
        elif choice == "2":
            gpu_setup_menu()
        elif choice == "3":  # New ARM64 handler
            os.system('clear')
            print_title("ARM64 Firmware Setup")
            try:
                arm64_firmware_setup()
                print("\nARM64 firmware tools installed.\n")
            except Exception as e:
                print(f"\nError during ARM64 setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "B":
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def cpu_setup_menu():
    while True:
        os.system('clear')
        print_title("Processor Setup")
        print("    1. AMD CPU\n\n"
              "    2. Intel CPU\n\n")
        thin_separator()
        print("Selection; Menu Options 1-2, Back To Main = B: ", end="")
        choice = input().strip().upper()
        if choice == "1":
            os.system('clear')
            print_title("Setting Up AMD CPU")
            try:
                amd_cpu_setup()
                print("\nAMD CPU setup completed.\n")
            except Exception as e:
                print(f"\nError during AMD CPU setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "2":
            os.system('clear')
            print_title("Setting Up Intel CPU")
            try:
                intel_cpu_setup()
                print("\nIntel CPU setup completed.\n")
            except Exception as e:
                print(f"\nError during Intel CPU setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "B":
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def gpu_setup_menu():
    while True:
        os.system('clear')
        print_title("Graphics Setup")
        print("    1. AMDGPU (Non-ROCm)\n\n"
              "    2. AMDGPU (ROCm)\n\n"
              "    3. NVIDIA GPU\n\n"
              "    4. Intel GPU\n\n")
        thin_separator()
        print("Selection; Menu Options 1-4, Back To Main = B: ", end="")
        choice = input().strip().upper()
        if choice == "1":
            os.system('clear')
            print_title("Setting Up AMDGPU (Non-ROCm)")
            try:
                amdgpu_non_rocm_setup()
                print("\nAMDGPU (Non-ROCm) setup completed.\n")
            except Exception as e:
                print(f"\nError during AMDGPU (Non-ROCm) setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "2":
            os.system('clear')
            print_title("Setting Up AMDGPU (ROCm)")
            try:
                amdgpu_rocm_setup()
                print("\nAMDGPU (ROCm) setup completed.\n")
            except Exception as e:
                print(f"\nError during AMDGPU (ROCm) setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "3":
            os.system('clear')
            print_title("Setting Up NVIDIA GPU")
            try:
                nvidia_gpu_setup()
                print("\nNVIDIA GPU setup completed.\n")
            except Exception as e:
                print(f"\nError during NVIDIA GPU setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "4":
            os.system('clear')
            print_title("Setting Up Intel GPU")
            try:
                intel_gpu_setup()
                print("\nIntel GPU setup completed.\n")
            except Exception as e:
                print(f"\nError during Intel GPU setup: {e}\n")
            input("Press Enter to continue...")
        elif choice == "B":
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def system_tweaks_menu():
    while True:
        os.system('clear')
        print_title("Tweaks and Hacks")
        sudo_status = "Enabled" if check_sudo_nopasswd() else "Disabled"
        auto_login_status = "Enabled" if check_auto_login() else "Disabled"
        windows_commands_status = "Enabled" if check_windows_commands() else "Disabled"
        hang_timeout = get_hang_timeout()
        wellbeing_status = "Enabled" if check_wellbeing_panel() else "Disabled"
        print(f"    1. Toggle sudo password prompt (Status: {sudo_status})\n\n"
              f"    2. Toggle auto-login (Status: {auto_login_status})\n\n"
              f"    3. Implement Windows-like commands (Status: {windows_commands_status})\n\n"
              f"    4. Adjust GNOME hang timeout (Current: {hang_timeout}s)\n\n"
              f"    5. Toggle Wellbeing Panel (Status: {wellbeing_status})\n\n")
        thin_separator()
        print("Selection; Menu Options 1-5, Back To Main = B: ", end="")
        choice = input().strip().upper()
        if choice == "1":
            os.system('clear')
            print_title("Toggling Sudo Password Prompt")
            try:
                toggle_sudo_nopasswd()
                print("\nSudo password prompt updated.\n")
            except Exception as e:
                print(f"\nError during sudo password prompt toggle: {e}\n")
            input("Press Enter to continue...")
        elif choice == "2":
            os.system('clear')
            print_title("Toggling Auto-Login")
            try:
                toggle_auto_login()
                print("\nAuto-login updated.\n")
            except Exception as e:
                print(f"\nError during auto-login toggle: {e}\n")
            input("Press Enter to continue...")
        elif choice == "3":
            os.system('clear')
            print_title("Implementing Windows-like Commands")
            try:
                implement_windows_commands()
                print("\nWindows-like commands implemented.\n")
            except Exception as e:
                print(f"\nError during Windows-like commands implementation: {e}\n")
            input("Press Enter to continue...")
        elif choice == "4":
            os.system('clear')
            print_title("Adjusting GNOME Hang Timeout")
            try:
                adjust_hang_timeout()
                print("\nHang timeout updated.\n")
            except Exception as e:
                print(f"\nError during GNOME hang timeout adjustment: {e}\n")
            input("Press Enter to continue...")
        elif choice == "5":
            os.system('clear')
            print_title("Toggling Wellbeing Panel")
            try:
                toggle_wellbeing_panel()
                print("\nWellbeing Panel setting updated.\n")
            except Exception as e:
                print(f"\nError during Wellbeing Panel toggle: {e}\n")
            input("Press Enter to continue...")
        elif choice == "B":
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def user_folder_menu():
    while True:
        os.system('clear')
        print_title("Common Folders")
        status, user_dirs = read_user_dirs()
        folder_keys = sorted(user_dirs.keys())
        for i, key in enumerate(folder_keys, 1):
            print(f"    {i}. {key.replace('XDG_', '').replace('_DIR', '').title()} ({user_dirs[key]})\n")
        thin_separator()
        print(f"Selection; Menu Options 1-{len(folder_keys)}, Set To Defaults = R, Back To Main = B: ", end="")
        choice = input().strip().upper()
        if choice.isdigit() and 1 <= int(choice) <= len(folder_keys):
            selected_key = folder_keys[int(choice) - 1]
            os.system('clear')
            print_title(f"Modify {selected_key.replace('XDG_', '').replace('_DIR', '').title()}")
            print(status + "\n")
            current_value = user_dirs[selected_key]
            default_value = DEFAULT_DIRS.get(selected_key, "N/A")
            print(f"Current: {current_value}\nDefault: {default_value}\n\n")
            new_path = input("Enter new path, 'R' to reset to default, or Enter to keep: ").strip()
            updated_dirs = {}
            if new_path.lower() == 'r':
                updated_dirs[selected_key] = DEFAULT_DIRS[selected_key]
            elif new_path:
                updated_dirs[selected_key] = new_path
            if updated_dirs:
                result = save_user_dirs(updated_dirs)
                print(f"\n{result}\n")
            else:
                print("\nNo changes made.\n")
            input("Press Enter to continue...")
        elif choice == "R":
            os.system('clear')
            print_title("Reset to Default Folder Configurations")
            result = apply_default_dirs()
            print(result + "\n")
            input("Press Enter to continue...")
        elif choice == "B":
            break
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

if __name__ == "__main__":
    main_menu()

#!/bin/bash

# Constants
SEPARATOR_WIDTH=80
HEADER_TITLE="Ubuntu 25 - Tweaks and Installer"

# Display Functions
print_separator() {
    printf '%*s\n' "$SEPARATOR_WIDTH" '' | tr ' ' "$1"
}

print_thick_separator() {
    print_separator "="
}

print_thin_separator() {
    print_separator "-"
}

clear_screen() {
    clear
    print_thick_separator
    echo "    $HEADER_TITLE"
    print_thick_separator
    echo ""
}

show_error() {
    echo ""
    print_thick_separator
    echo "ERROR: $1"
    print_thin_separator
    sleep "$2"
    [ "$3" = "exit" ] && exit 1
}

# Initialization
check_ubuntu_version() {
    clear_screen
    echo "Checking Ubuntu Version..."
    
    if [ ! -f /etc/os-release ]; then
        show_error "Not running on Ubuntu Linux" 3 exit
    fi
    
    source /etc/os-release
    UBUNTU_MAJOR=$(echo "$VERSION_ID" | cut -d'.' -f1)
    
    if [ "$UBUNTU_MAJOR" != "25" ]; then
        show_error "Requires Ubuntu 25.x (Detected: $VERSION_ID)" 3 exit
    fi
    
    echo "System check passed (Ubuntu $VERSION_ID)"
    sleep 1
}

# Menu Functions
show_menu() {
    clear_screen
    printf "\n\n\n\n\n\n"
    echo "    1. Launch Program"
    echo ""
    echo "    2. Check Files"
    echo ""
    printf "\n\n\n\n\n\n"
    print_thin_separator
    echo -n "Selection; Menu Options 1-2, Exit Program = X: "
}

verify_files() {
    clear_screen
    echo "Checking required files..."
    echo ""
    
    local missing=0
    local files=("launcher.py" "scripts/interface.py" "scripts/utility.py")
    
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            echo "    [✓] $file"
        else
            echo "    [✗] $file (missing)"
            missing=1
        fi
    done
    
    if [ $missing -eq 0 ]; then
        printf "\nAll files present.\n\n\n\n\n\n\n\n\n\n"
    else
        printf "\nMissing required files.\n\n\n\n\n\n\n\n\n\n"
    fi
    
    print_thin_separator
    read -rp "Press Enter to continue..."
}

# Main Execution
check_ubuntu_version

while true; do
    show_menu
    read -r choice
    
    case "$choice" in
        1)
            clear_screen
            echo "Launching main program..."
            print_thin_separator
            python3 launcher.py
            read -rp "Press Enter to continue..."
            ;;
        2)
            verify_files
            ;;
        [Xx])
            clear_screen
            printf "Exiting Bash Script...\n"
            sleep 2
            exit 0
            ;;
        *)
            clear_screen
            echo "Invalid option: $choice"
            print_thin_separator
            sleep 2
            ;;
    esac
done

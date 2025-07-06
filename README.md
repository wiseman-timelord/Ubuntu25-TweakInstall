# Ubuntu 25 - Tweaks & Installer
- Status: Beta (Considered early release).

### Description:
This project includes install/tweaking for, ubuntu 25 and ubuntu 25 common packages. The Installer saves time, researching and finding the correct commands, to do basic stuff after install of `Ubuntu 25.04`, ensuring system updates and installations, are printed and errors handled. The tweaker script focuses on implementing features and other tweaks, including the addition of Windows-like common commands to go along side the relating common linux commands. The point is to take the hastle out of the bulk of the work, or if you are new to linux and are unsure.

### Features:
- Basic OS installation includes system updates and essential tools like vim, nano, curl, wget, git, and htop. (Both)
- Intermediate OS setup includes development tools, QEMU, libvirt, GCC, GNOME tweaks, and Vulkan drivers. (Both)
- Wine libraries for enhanced audio, graphics, USB device support, Linux integration with X11, multimedia formats, font rendering, and image formats for better compatibility with Windows applications. (Both)
- CPU setup offers options for AMD and Intel CPUs-specific tools and optimizations, for performance tuning. (Both)
- GPU setup provides options for AMDGPU (Non-ROCm and ROCm), NVIDIA, and Intel GPU drivers and optimizations for graphics performance. (Both)
- The main menu dynamically updates with the status of each installation step for user clarity. (Both)
- Option to implement Windows-like commands such as dir, copy, move, del, md, rd, cls, type, where, echo, shutdown, and restart for familiar terminal use. (Both)
- Option to disable sudo password prompts, and password complexity requirements to mimic Windows-like behavior (e.g., disabling UAC and Software Protection for ease of administration). (Both)
- User folder configurations allow individual folder tweaks (e.g., Desktop, Downloads) with current paths displayed, supporting reset to defaults for personalized file organization. (Both)

### Preview:
- The `Main Menu` has sub-menus...
```
================================================================================
    Ubuntu 25 - Tweaks and Installer
================================================================================




    1. System Installation and Updates

    2. Software and Package Management

    3. Hardware Optimization and Drivers

    4. System Tweaks and Customizations

    5. User Folder Configurations




--------------------------------------------------------------------------------
Selection; Menu Options 1-5, Exit Program = X: 


```


### INSTRUCTIONS:
1. download the latest release version, and extract to your chosen programs folder (there are no requirements or libraries to install). 
2. Ensure, `./Ubuntu25-TweakInstall.sh` is executable via `sudo chmod +x ./Ubuntu24-TweakInstall.sh` or `RightClick > Properties > TickExecutable`.
3. run "sudo ./Ubuntu25-TweakInstall.sh", this will load the bash menu, allowing checking files and launching. Select "Run Program".
4. Investigate the appropriate menus, take a look at what it offers, plan what features you intend to use, and select them (ensuring to note errors that pop up). Ensure to think about what you are doing, dont install stuff you dont need and wont use.
5. After finishing configutation, then exit the program and restart computer, to enable all tweaks/installs to take effect. 
6. If there are issues with anything immediately, then check the notes you made (if any), and investigate appropriately to complete relating install/tweak.
- hopefully whatever tweak or install you did worked out for you, if not, then I advise asking gpt/deepseek/grok/etc, and input the output you got from the terminal with your prompt.

### Notation:
- This program is typically tested/updated when the creator does a new install of ubuntu 25.
- Minimum Windows 10 for Vertio/Kvm/QEmu Drivers from `Virtio-Win-0.1.262.Iso`, Windows 7-81 did not complete Setup.  
- For `Ubuntu 25` Assistance, I advise, ChatGPT `https://chatgpt.com` or DeepSeek `https://chat.deepseek.com/`, and prompt mentioning your specific version is 25.xx.
- Version 25 required me to use the USB installer in the motherboard usb port, and would NOT work in the front usb port.
- Its a continuation of the `Ubuntu24-TweakInstall` project.
- Additional Windows Commands in the terminal are shortcut to relating linux commands  (fixing/improving is done here `/etc/profile.d/windows_commands.sh`)...
```
`dir` - Lists directory contents in a detailed format.
`copy` - Copies files and directories.
`move` - Moves files and directories.
`del` - Deletes files and directories.
`md` - Creates directories.
`rd` - Removes directories.
`cls` - Clears the terminal screen.
`type` - Displays the contents of a file.
`where` - Locates the binary, source, or manual page files for a command.
`echo` - Prints text to the terminal.
`shutdown` - Shuts down the system.
`restart` - Restarts the system.
```
- Unsafe tweaks removed for, ufw and apparmor.

### File Structure
Program files are like this...
```
.\Ubuntu25-TweakInstall.sh
.\launcher.py
.\scripts\interface.py
.\scripts\utility.py
```

### Development 
- Planned work...
1. Add hybrid graphics install with radeon as main and nvidia as compute, in the method I used. Possibly detect cards, then present options, which is main/secondary/compute, and install appropriately.
2. The Individual `VM` related install seems odd now, needs to be made into Modular submenu again. `LLM` option had to be removed, error with build-tools was it? But still, LLM was a bad choice, because people will want custom Torch version possibly. Maybe Just expand out the options for the VM setup, so as to include different VM modules.
- No release until next reinstall of OS, to ensure fully tested, but it is assumed most stuff works. 

### Warnings:
- If there is some issue with a device, after restarting, after using the Installer, then try re-starting again, this fixed itself for me, but I had a blank screen on one of the monitors.

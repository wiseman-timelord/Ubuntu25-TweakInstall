# Ubuntu 25 - Tweaks & Installer
- Status: Alpha (converting code now).

### Description:
This project includes install/tweaking for, ubuntu 25 and ubuntu 25 common packages. The Installer saves time, researching and finding the correct commands, to do basic stuff after install of `Ubuntu 25.04`, ensuring system updates and installations, are printed and errors handled. The tweaker script focuses on implementing features and other tweaks, including the addition of Windows-like common commands to go along side the relating common linux commands. The point is to take the hastle out of the bulk of the work, or if you are new to linux and are unsure.

<br>
(editing below here)
<br>

### Features:
- Basic OS installation includes system updates and essential tools like vim, nano, curl, wget, git, and htop. (Both)
- Intermediate OS setup includes development tools, QEMU, libvirt, GCC, GNOME tweaks, and Vulkan drivers. (Both)
- Wine libraries for enhanced audio, graphics, USB device support, Linux integration with X11, multimedia formats, font rendering, and image formats for better compatibility with Windows applications. (Both)
- CPU setup offers options for AMD and Intel CPUs-specific tools and optimizations, for performance tuning. (Both)
- GPU setup provides options for AMDGPU (Non-ROCm and ROCm), NVIDIA, and Intel GPU drivers and optimizations for graphics performance. (Both)
- The main menu dynamically updates with the status of each installation step for user clarity. (Both)
- Option to implement Windows-like commands such as dir, copy, move, del, md, rd, cls, type, where, echo, shutdown, and restart for familiar terminal use. (Both)
- Option to disable sudo password prompts, AppArmor, and password complexity requirements to mimic Windows-like behavior (e.g., disabling UAC and Software Protection for ease of administration). (Both)
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
2. Ensure, `./Ubuntu24-TweakInstall.sh` is executable via `sudo chmod +x ./Ubuntu24-TweakInstall.sh` or `RightClick > Properties > TickExecutable`.
3. run "sudo ./Ubuntu24-TweakInstall.sh", this will load the bash menu, allowing checking files and launching. Select "Run Program".
4. Investigate the appropriate menus, take a look at what it offers, plan what features you intend to use, and select them (ensuring to note errors that pop up). Ensure to think about what you are doing, dont install stuff you dont need and wont use.
5. After finishing configutation, then exit the program and restart computer, to enable all tweaks/installs to take effect. 
6. If there are issues with anything immediately, then check the notes you made (if any), and investigate appropriately to complete relating install/tweak.
- hopefully whatever tweak or install you did worked out for you, if not, then I advise asking gpt/deepseek/grok/etc, and input the output you got from the terminal with your prompt.

### Notation:
- This program is typically tested/updated when the creator does a new install of ubuntu 24.
- Minimum Windows 10 for Vertio/Kvm/QEmu Drivers from `Virtio-Win-0.1.262.Iso`, Windows 7-81 did not complete Setup.  
- For `Ubuntu 24` Assistance, go for example, here `https://chatgpt.com/g/g-sQSBQqeR8-sysadmin-for-ubuntu-22-04` or here `https://chatgpt.com/g/g-OPkIvf0HN-java-21-postgresql-16`, and prompt mentioning your specific version is 24.xx. 
- Would make a better GPT for 24, but people also need to, go fund me or patreon, to assist in paying gpt subscription to do so again..
- Its for 24, because thats the version I was using at the time, this may later expand like 22-24 or there will be new version ie Ubuntu26-TweakInstall.
- I was unable to install `24.04.x`, so I installed `24.10 Beta`, which did not have these install issues, and turned out quite good. 
- Its a continuation of the `Fedora40-TweakInstall` project, `Ubuntu24-TweakInstall` is more safer/complete. `Fedora40-TweakInstall` is hidden due to untested tweaks, that require inspection/fixing/testing, which wont happen unless I reinstall Fedora.
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
.\Ubuntu24-TweakInstall.sh
.\launcher.py
.\scripts\interface.py
.\scripts\utility.py
```

### Development 
- Planned work...
1. Add opensnitch using method found to be working via flatpack as instructed on the github repository. (this method works)
2. Add hybrid graphics install with radeon as main and nvidia as compute, in the method I used.
3. `Start + e` :- Go to `Settings>Keyboard>Add Custom`, then type in `nautilus` for the command, and put `Start + e` in the Shortcut, and give it a fitting title like `Explorer Shortcut`. NEed to add this and other tweaks for keyboard shortcuts from windows.
4. The Individual `VM` related install seems odd now, needs to be made into Modular submenu again. `LLM` option had to be removed, error with build-tools was it? But still, LLM was a bad choice, because people will want custom Torch version possibly. Maybe Just expand out the options for the VM setup, so as to include different VM modules.

### Warnings:
- If there is some issue with a device, after restarting, after using the Installer, then try re-starting again, this fixed itself for me, but I had a blank screen on one of the monitors, its an iffy old monitor prone to issues though.

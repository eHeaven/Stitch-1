import os
import subprocess


def _install_osx(path="{}/build/reqs/osx_requirements.txt", verbose=False):
    pip_cmd = ["pip", "install", "-r", path.format(os.getcwd())]
    if verbose:
        print("\033[93m[d]\033[0m running command: '{}'..".format(' '.join(pip_cmd)))
    return subprocess.call(pip_cmd)


def osx_main(verbose=False):
    print("\033[36m[i]\033[0m installing OSX packages..")
    _install_osx(verbose=verbose)
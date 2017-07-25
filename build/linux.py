import os
import subprocess
from build.windows import _install_pil


def _install_scripted(dst_dir="{}/build".format(os.getcwd()), verbose=False):
    if verbose: print("\033[93m[d]\033[0m installing the scripted packages in '{}'.. ".format(dst_dir))
    install_cmd = ["sudo", "sh", "{}/install.sh".format(dst_dir)]
    if verbose: print("\033[93m[d]\033[0m running command: '{}'..".format(' '.join(install_cmd)))
    subprocess.call(install_cmd)


def _install_other_reqs(req_file="lnx_requirements.txt", verbose=False):
    reqs_file_path = "{}/build/reqs/{}".format(os.getcwd(), req_file)
    if verbose: print("\033[93m[d]\033[0m reading from '{}'..".format(reqs_file_path))
    pip_cmd = ["sudo", "-H", "pip", "install", "-r", reqs_file_path]
    if verbose: print("\033[93m[d]\033[0m running command: '{}'..".format(' '.join(pip_cmd)))
    return subprocess.call(pip_cmd)


def linux_main(verbose=False):
    print("\033[36m[i]\033[0m installing Linux packages..")
    __funcs__ = [
        _install_pil, _install_scripted,
        _install_other_reqs
    ]
    for func in __funcs__:
        func(verbose=verbose)

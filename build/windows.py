import os
import subprocess
import platform


# check the platform architecture, 64 or 32 bit
def _check_arc(tup=platform.architecture()): return tup[0:2]


def _install_py2exe(verbose=False, dist_url="http://sourceforge.net/projects/py2exe/files/latest/download?source=files"):
    """
     install py2exe from the sourceforge page, not sure how safe this is will create
     a checksum checker later, but for now i just wanna get this thing launched and
     fix the installation issues with it.
    """
    pip_cmd = ["pip", "install", dist_url]
    if verbose:
        print("[d] running command: '{}'..".format(' '.join(pip_cmd)))
    return subprocess.call(pip_cmd)


def _install_pil(verbose=False, dist_url="https://dist.plone.org/thirdparty/", pack_name="PIL"):
    """
     install PIL from the dist website, this once again idk how safe it is, but it's
     going to work and that's what we're gonna do.
    """
    pip_cmd = ["pip", "install", "--no-index", "-f", dist_url, "-U", pack_name]
    if verbose:
        print("[d] running command: '{}'..".format(' '.join(pip_cmd)))
    return subprocess.call(pip_cmd)


def _install_pyhook(verbose=False, whl_start_name="pyHook-1.5.1-cp36-cp36m-"):
    """
     install pyhook from the .whl files
    """
    full_whl = whl_start_name + "win32.whl" if _check_arc() == "32" else "win_amd64.whl"
    full_whl_path = "{}/build/reqs/whls/{}".format(os.getcwd(), full_whl)
    pip_cmd = ["pip", "install", full_whl_path]
    if verbose:
        print("[d] running command: '{}'..".format(pip_cmd))
    return subprocess.call(pip_cmd)


def _install_other(verbose=False, reqs_file_path="{}/build/reqs/win_requirements.txt"):
    """
     install all other dependencies.
    """
    pip_cmd = ["pip", "install", "-r", reqs_file_path.format(os.getcwd())]
    if verbose:
        print("[d] running command: '{}'..".format(' '.join(pip_cmd)))
    return subprocess.call(pip_cmd)


def win_main(verbose=False):
    __funcs__ = [
        _install_pyhook, _install_py2exe,
        _install_pil, _install_other
    ]
    print("[i] installing Windows requirements..")
    for installation in __funcs__:
        installation(verbose=verbose)

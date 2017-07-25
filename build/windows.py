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


def _install_pyhook(verbose=False, whl_start_dir=os.listdir("{}/build/reqs/whls".format(os.getcwd()))):
    """
     install pyhook from the .whl files. There is an issue with Windows 8 and above
     where the wheel files will not be supported
    """
    all_whls = set()
    os_arc = _check_arc()
    if verbose:
        print("[d] searching for .whl files that are compatible with {} OS..".format(os_arc[0]))
    for whl in whl_start_dir:
        if os_arc == "32":
            if "-win32.whl" in whl:
                all_whls.add(whl)
        else:
            if "-win_amd64.whl" in whl:
                all_whls.add(whl)
    for whl in list(all_whls):
        whl_path = "{}/build/reqs/whls/".format(os.getcwd()) + whl
        pip_cmd = ["pip", "install", "--use-wheel", "--no-index", whl_path]
        if verbose:
            print("[d] running command: '{}'..".format(' '.join(pip_cmd)))
        subprocess.call(pip_cmd)


def _install_pywin(verbose=False, dist_url="https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/{}/download"):
    """
     install py2exe from the dist website, dunno if it's secure, don't really care,
     it's gonna work.
    """
    exe_filenames = ("pywin32-220.win-amd64-py2.7.exe", "pywin32-220.win32-py2.7.exe")
    arc = _check_arc()
    if arc == "32":
        dist_url = dist_url.format(exe_filenames[1])
    else:
        dist_url = dist_url.format(exe_filenames[0])
    pip_cmd = ["pip" "install", dist_url]
    if verbose:
        print("[d] running command: '{}'..".format(' '.join(pip_cmd)))
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
        _install_pil, _install_py2exe,
        _install_other
    ]
    print("[i] installing Windows requirements..")
    for installation in __funcs__:
        installation(verbose=verbose)

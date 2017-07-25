import os
import subprocess
from build.windows import _install_pil


def _install_scripted(dst_dir="{}/build".format(os.getcwd()), verbose=False):
    if verbose:
        print("[d] installing the scripted packages in '{}'.. ".format(dst_dir))
    install_cmd = ["sudo", "sh", "{}/install.sh".format(dst_dir)]
    subprocess.call(install_cmd)


def _install_other_reqs(req_file="lnx_requirements.txt", verbose=False):
    reqs_file_path = "{}/build/reqs/{}".format(os.getcwd(), req_file)
    pip_cmd = ["sudo", "-H", "pip", "install", "-r", reqs_file_path]
    if verbose:
        print("[d] running command: '{}'..".format(pip_cmd))
    return subprocess.call(pip_cmd)


'''def _install_pil(verbose=False, dist_url="https://dist.plone.org/thirdparty/", pack_name="PIL"):
    """
     install PIL from the dist website, this once again idk how safe it is, but it's
     going to work and that's what we're gonna do.
    """
    pip_cmd = ["sudo", "-H", "pip", "install", "--no-index", "-f", dist_url, "-U", pack_name]
    if verbose:
        print("[d] running command: '{}'..".format(' '.join(pip_cmd)))
    return subprocess.call(pip_cmd)'''


def linux_main(verbose=False):
    print("[i] installing Linux packages..")
    __funcs__ = [
        _install_pil, _install_scripted,
        _install_other_reqs
    ]
    for func in __funcs__:
        func(verbose=verbose)

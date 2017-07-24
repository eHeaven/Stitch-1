import os
import subprocess
#from build.windows import _install_pil


def _install_scripted(dst_dir="{}/build".format(os.getcwd()), verbose=False):
    if verbose:
        print("[d] installing the scripted packages in '{}'.. ".format(dst_dir))
    install_cmd = ["{}/install.sh".format(dst_dir)]
    subprocess.call(install_cmd)


def _install_other_reqs(reqs_path="{}/reqs", req_file="lnx_requirements.txt", verbose=False):
    pip_cmd = ["pip", "install", "-r", reqs_path.format(os.getcwd() + "/" + req_file)]
    if verbose:
        print("[d] running command: '{}'..".format(pip_cmd))
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


def linux_main(verbose=False):
    print("[i] installing Linux packages..")
    _install_pil(verbose=verbose)
    _install_scripted(verbose=verbose)
    _install_other_reqs()

#!/usr/bin/env python
# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

try:
    from application.stitch_cmd import *
    server_main()
except ImportError:
    import platform
    import sys
    from build import (
        linux,
        windows,
        osx
    )

    print(
        "[F] the application requires packages that have not been installed yet, "
        "running the setup for the installation.."
    )

    def _find_os(system=platform.platform()):
        if "Linux" in system:
            return "linux"
        elif "Windows" in system:
            return "windows"
        else:
            return "osx"

    def _launch_install_scripts(system, verbose=False):
        if system == "linux":
            linux.linux_main(verbose=verbose)
        elif system == "windows":
            windows.win_main(verbose=verbose)
        else:
            osx.osx_main()

    if "verbose" in sys.argv:
        _launch_install_scripts(_find_os(), verbose=True)
    else:
        _launch_install_scripts(_find_os())
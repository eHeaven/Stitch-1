#!/usr/bin/env python
# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

try:
    from application.stitch_cmd import server_main
    server_main()
except ImportError:  # if this happens we're gonna try and reinstall the dependencies.
    import platform
    import sys
    from build import (
        linux,
        windows,
        osx
    )

    print(
        "\033[31m[F]\033[0m the application requires packages that have not been installed yet, "
        "running the setup for the installation.."
    )
    verbosity = raw_input("Would you like to run verbosely (more output)[y/N]: ")
    if verbosity.lower().startswith("y"):
        verbose_output = True
    else:
        verbose_output = False

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
            osx.osx_main(verbose=verbose)

    _launch_install_scripts(system=_find_os(), verbose=verbose_output)
except Exception as ex:  # if this happens we'll go ahead and grab some information from it
    raise RuntimeError(handle_exception_clause(ex))
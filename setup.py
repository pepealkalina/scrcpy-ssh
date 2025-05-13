from cx_Freeze import setup, Executable

buildOptions = dict(
    include_msvcr=True
)

import sys

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('remoteScrcpyUtils.py')
]

setup(
    name="remoteScrcpyUtils",
    version="0.1",
    description="My GUI application!",
    options=dict(build_exe=buildOptions), 
    executables=executables)
from cx_Freeze import setup

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
}

setup(
    name="build",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[{"script": "remoteScrcpySSH.py", "base": "gui"}],
)
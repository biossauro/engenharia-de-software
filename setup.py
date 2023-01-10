"""
Setup (build) script for the package.
"""
from cx_Freeze import setup, Executable

setup(
    name="calculator",
    version="1.0",
    description="My calculator app!",
    options={"build_exe": {"packages": ["os"], "excludes": ["tkinter"],
                           "build_exe": "build"}},
    executables=[Executable("main.py", base=None,
                            target_name="calculator.exe")],
)

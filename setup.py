from cx_Freeze import Executable, setup

execuetables = [
    Executable(
        "Fluent Calculator.py",
        icon="Calculator.ico",
        shortcut_name="Fluent Python Calculator",
        shortcut_dir="DesktopFolder",
    )
]

build_exe_options = {
    "include_files": ("Calculator.ico"),
    "includes": ["tkinter", "darkdetect", "sv_ttk", "ntkutils"],
}

bdist_msi_options = {
    "add_to_path": False,
    "install_icon": "Calculator.ico",
    "target_name": "Fluent Python Calculator",
}

setup(
    name="Fluent Python Calculator",
    version="1.1",
    description="A modern calculator made completely in python!",
    executables=execuetables,
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    }
)
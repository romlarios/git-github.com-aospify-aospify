#!d:\programs\python\python36-32\python.exe
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

setup(name = "AOSPify" ,
      version = "1.0" ,
      description = "" ,
      executables = [Executable("main.py")])

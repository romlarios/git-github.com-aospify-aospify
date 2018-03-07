#!/usr/bin/env python3
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

setup(name = "AOSPify" ,
      version = "1.0" ,
      description = "" ,
      executables = [Executable("main.py")])

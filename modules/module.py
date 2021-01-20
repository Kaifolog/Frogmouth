from os import listdir
from os.path import isfile
from pathlib import Path
import importlib


class Module:
    """Base class for all modules"""
    pass


class ModuleManager:
    def __init__(self, app):
        self.modules = []
        self.modules_path = app.config.MODULE_PATH

        self.modules = [file for file in listdir(self.modules_path)
                        if isfile(self.modules_path + file) and file.endswith(".py") and file != "__init__.py"
                        and file != "module.py" or isfile(self.modules_path + file + "/__init__.py")]


if __name__ == "__main__":
    pass

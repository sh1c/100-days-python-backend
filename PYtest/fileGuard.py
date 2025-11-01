import os
import shutil  # copy2(a,b)将a内容复制到b
from tkinter import N
from typing import Optional


class FileGurad:
    # bak路径参数
    def __init__(self, path):
        self.path = path
        self.bak: Optional[str] = None

    def __enter__(self):
        if os.path.exists(self.path):
            self.bak = self.path + ".bak"
            shutil.copy2(self.path, self.bak)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and self.bak:
            shutil.move(self.bak, self.path)
        elif self.bak:
            os.remove(self.bak)

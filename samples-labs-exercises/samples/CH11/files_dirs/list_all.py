from typing import Callable
import os

def list_all(dir: str, action: Callable[..., None]):
    action(dir)
    for entry in os.scandir(dir):
        fullpath = f'{dir}\\{entry.name}'
        if entry.is_dir():
            list_all(fullpath, action)
        elif entry.is_file():
            print(fullpath)

list_all(r'c:\workspace', print)
from typing import Callable
import os

def list_all(dir: str, action: Callable[..., None]):
    for dirpath, dirnames, filenames in os.walk(dir):
        action(dirpath)
        for filename in filenames:
            action(f'{dirpath}\\{filename}')

list_all(r'c:\workspace', print)
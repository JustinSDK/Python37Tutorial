from typing import Dict, Type

TLogger = Type['Logger']

class Logger:
    __loggers: Dict[str, TLogger] = {}

    def __new__(cls: TLogger, name: str) -> TLogger:
        if name not in cls.__loggers:
            logger = object.__new__(cls)
            cls.__loggers[name] = logger
            return logger
        return cls.__loggers[name]

    def __init__(self, name: str) -> None:
        if 'name' not in vars(self):
            self.name = name

    def log(self, message: str):
        print(f'{self.name}: {message}')

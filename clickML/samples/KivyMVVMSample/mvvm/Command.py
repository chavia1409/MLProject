from typing import Callable


class Command:
    def __init__(self, callable:Callable[[object], None]) -> None:
        self.__callable = callable

    __callable:Callable[[object], None]
    
    def invoke(self, args):
        if self.__callable is None:
            return
        self.__callable(args)
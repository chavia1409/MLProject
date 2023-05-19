from typing import Callable


class Command:
    """ See Command pattern 
    """
    def __init__(self, callable:Callable[[object], None]) -> None:
        """
        Parameters
        ----------
        callable : Callable[[object], None]
            The callable (e.g. lambda or function) that gets invoked when call the invoke function
        """
        self.__callable = callable

    __callable:Callable[[object], None]
    
    def invoke(self, args):
        """
        Invokes the Command function
        Parameters
        ----------
        args
            arguments that get passed to the Command function
        """
        if self.__callable is None:
            return
        self.__callable(args)
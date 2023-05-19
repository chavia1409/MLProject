from .propertychangedeventargs import PropertyChangedEventArgs


from collections.abc import Callable

class PropertyChangedEvent:
    def __init__(self) -> None:
        self.__registeredFunc = list[Callable[[object, PropertyChangedEventArgs], None]]()
        pass
    """
    This class implements the Observer pattern.
    Its the Observable. 
    """
    __registeredFunc:list[Callable[[object, PropertyChangedEventArgs], None]] 
    
    def invoke(self, sender, propertyChangedEventArgs:PropertyChangedEventArgs):
        """
        invokes all registered functions of the observers
        Parameters
        ----------
        sender : object
            sender of the event
        propertyChangedEventArgs : PropertyChangedEventArgs
            The arguments that the Observers get
        """
        for registered in self.__registeredFunc:
            registered(sender, propertyChangedEventArgs)
    
    def __iadd__(self, toRegister: Callable[[object, PropertyChangedEventArgs], None]):
        self.__registeredFunc.append(toRegister)
        return self

    def __isub__(self, toRemove: Callable[[object, PropertyChangedEventArgs], None]):
        self.__registeredFunc.remove(toRemove)
        return self

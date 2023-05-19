from mvvm.PropertyChangedEventArgs import PropertyChangedEventArgs


from collections.abc import Callable

class PropertyChangedEvent:
    __registeredFunc:list[Callable[[object, PropertyChangedEventArgs], None]] = list[Callable[[object, PropertyChangedEventArgs], None]]()
    
    def invoke(self, sender, propertyChangedEventArgs:PropertyChangedEventArgs):
        for registered in self.__registeredFunc:
            registered(sender, propertyChangedEventArgs)
    
    def __iadd__(self, toRegister: Callable[[object, PropertyChangedEventArgs], None]):
        self.__registeredFunc.append(toRegister)
        return self

    def __isub__(self, toRemove: Callable[[object, PropertyChangedEventArgs], None]):
        self.__registeredFunc.remove(toRemove)
        return self

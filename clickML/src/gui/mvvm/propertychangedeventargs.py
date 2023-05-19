class PropertyChangedEventArgs:
    """
    Arguments for the Property Changed event
    """
    def __init__(self, propertyName, value) -> None:
        self.__propertyName = propertyName
        self.__value = value
    __propertyName:str
    __value = None
    
    @property
    def propertyName(self) -> str:
        """
        Name of the property of the viewmodel taht changed
        """
        return self.__propertyName
    
    @property
    def value(self):
        """
        The new value
        """
        return self.__value
    
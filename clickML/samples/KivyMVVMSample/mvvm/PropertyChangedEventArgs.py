class PropertyChangedEventArgs:
    def __init__(self, propertyName, value) -> None:
        self.__propertyName = propertyName
        self.__value = value
    __propertyName:str
    __value = None
    
    @property
    def propertyName(self) -> str:
        return self.__propertyName
    
    @property
    def value(self):
        return self.__value
    
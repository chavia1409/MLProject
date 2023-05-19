from mvvm.PropertyChangedEvent import PropertyChangedEvent
from mvvm.PropertyChangedEventArgs import PropertyChangedEventArgs


class ViewModelBase:
    __propertyChangedEvent:PropertyChangedEvent = PropertyChangedEvent()

    @property
    def propertyChangedEvent(self):
        return self.__propertyChangedEvent
    
    @propertyChangedEvent.setter
    def propertyChangedEvent(self, value):
        self.__propertyChangedEvent = value
        
    def OnPropertyChanged(self, propertyName:str, value):
        self.__propertyChangedEvent.invoke(self, PropertyChangedEventArgs(propertyName, value))
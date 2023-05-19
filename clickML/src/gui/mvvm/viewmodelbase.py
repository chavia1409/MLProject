from .propertychangedevent import PropertyChangedEvent
from .propertychangedeventargs import PropertyChangedEventArgs


class ViewModelBase:
    """
    Baseclass for all ViewModels
    """
    __propertyChangedEvent:PropertyChangedEvent = None

    def __init__(self):
        self.__propertyChangedEvent = PropertyChangedEvent()

    @property
    def propertyChangedEvent(self):
        """
        The event observers registers on to get notified when property of this viewmodel changed
        """
        return self.__propertyChangedEvent
    
    @propertyChangedEvent.setter
    def propertyChangedEvent(self, value):
        self.__propertyChangedEvent = value
        
    def _notify_property_changed(self, propertyName:str, value):
        """
        This methode invokes the event
        Parameters
        propertyName : str
            name of the property that has changed
        value : object
            new value of the property
        """
        self.__propertyChangedEvent.invoke(self, PropertyChangedEventArgs(propertyName, value))
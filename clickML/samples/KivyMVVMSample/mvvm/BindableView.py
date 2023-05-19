from multiprocessing import context
from mvvm.PropertyChangedEventArgs import PropertyChangedEventArgs
from mvvm.ViewModelBase import ViewModelBase


class BindableView:
    __context:ViewModelBase = None
    __bindingMap = {}

    @property
    def context(self):
        return self.__context
    
    @context.setter
    def context(self, value):
        if self.__context != None:
            self._removeBindings()
            self.__context.propertyChangedEvent -= self._handlePropertyChanged

        self.__context = value

        if self.__context != None:
            self._defineBindings()
            self.__context.propertyChangedEvent += self._handlePropertyChanged
        
        self._onContextChanged()

    def _removeBindings(self, oldViewModel:ViewModelBase):
        pass
    
    def _defineBindings(self):
        pass
    
    def _bindToContext(self, propertyName, bindingName):
        self.__bindingMap[bindingName] = propertyName
        currentValue = self.__getValueFromContext(bindingName)
        setattr(self, propertyName, currentValue)
        self.fbind(propertyName, self._changeContextProperty, propertyName=bindingName)
    
    def __getValueFromContext(self, bindingName):
        return getattr(self.context, bindingName)

    def _changeContextProperty(self, obj, value, propertyName):
        setattr(self.context, propertyName, value)

    def _onContextChanged(self):
        pass

    def _handlePropertyChanged(self, sender, propertyChangedEventArgs:PropertyChangedEventArgs):
        if propertyChangedEventArgs.propertyName not in self.__bindingMap:
            return
        property = self.__bindingMap[propertyChangedEventArgs.propertyName]
        setattr(self, property, propertyChangedEventArgs.value)
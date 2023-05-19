from .converterbase import ConverterBase
from .propertychangedevent import PropertyChangedEventArgs
from .viewmodelbase import ViewModelBase
from kivy.logger import Logger


class ContextView:
    """
    Baseclass for widgets etc. that should be bind to a View Model
    """
    __context: ViewModelBase = None
    __bindingMap: {}

    def __init__(self):
        self.__bindingMap = {}
        self.__converter_map = {}

    @property
    def context(self):
        """
        Returns
        -------
        context : ViewModelBase
            The context that this view is bind to
        """
        return self.__context

    @context.setter
    def context(self, value):
        """
        Sets the Context and remove the old Context
        Parameters
        ----------
        value
            the new context
        """
        if self.__context is not None:
            self.__remove_bindings()
            self.__context.propertyChangedEvent -= self.__handle_property_changed

        self.__context = value

        if self.__context is not None:
            self._define_bindings()
            self.__context.propertyChangedEvent += self.__handle_property_changed

        self._on_context_changed()

    def _define_bindings(self):
        """
        Gets called everytime the context changes.
        This function should be overriden in child class to set the bindings.
        """
        pass

    def __remove_bindings(self):
        """
        Removes the binding from the Kivy Properties
        """
        for kvp in self.__bindingMap.items():
            self.funbind(kvp[0], self.__change_context_property, binding_name=kvp[1], property_name=kvp[0])
        self.__bindingMap.clear()
        self.__converter_map.clear()

    def _bind_to_context(self, property_name:str, binding_name:str, converter: ConverterBase = None) -> None:
        """
        Bind a Kivy Property to a Property of the viewmodel
        Parameters
        ----------
        property_name : str
            name of the kivy Property
        binding_name : str
            name of the Property of the viewmodel
        """
        self.__bindingMap[binding_name] = property_name
        if converter is not None:
            self.__converter_map[property_name] = converter

        current_value = self.__get_value_from_context(binding_name)
        # if current_value is None:
        #     return

        self.__set_property(property_name, current_value)
        self.fbind(property_name, self.__change_context_property, binding_name=binding_name, property_name=property_name)



    def __get_value_from_context(self, binding_name):
        try:
            return getattr(self.context, binding_name)
        except:
            Logger.info(f"Context has no attribute {binding_name}")
        return None


    def __change_context_property(self, obj, value, binding_name, property_name):
        if property_name in self.__converter_map:
            converter = self.__converter_map[property_name]
            setattr(self.context, binding_name, converter.convert_back(value))
            return
        setattr(self.context, binding_name, value)

    def _on_context_changed(self):
        """
        This function gets called after the context has changed.
        Override it if you need to react when the context has change
        """
        pass

    def __handle_property_changed(self, sender, property_changed_event_args: PropertyChangedEventArgs):
        if property_changed_event_args.propertyName not in self.__bindingMap:
            return
        bound_property = self.__bindingMap[property_changed_event_args.propertyName]
        self.__set_property(bound_property, property_changed_event_args.value)

    def __set_property(self, property_name, value):
        if property_name in self.__converter_map:
            converter = self.__converter_map[property_name]
            setattr(self, property_name, converter.convert(value))
            return
        setattr(self, property_name, value)
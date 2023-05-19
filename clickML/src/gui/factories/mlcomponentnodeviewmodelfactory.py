from typing import Callable

from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.mlcomponentnodeviewmodelfactorybase import MLComponentNodeViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel


class MLComponentNodeViewModelFactory(MLComponentNodeViewModelFactoryBase):

    def __init__(self):
        self.__factory_methods_with_descriptor = {}
        self.__factory_methods = {}

    def create_by_descriptor(self, descriptor: MLComponentDescriptor):
        if descriptor.component_type not in self.__factory_methods_with_descriptor:
            raise Exception(f'Component Type {descriptor.component_type} is not registered. Please registere it')
        return self.__factory_methods_with_descriptor[descriptor.component_type](descriptor)


    def create(self, component_type: str):
        if component_type not in self.__factory_methods:
            raise Exception(f'Component Type {component_type} is not registered. Please registere it')
        return self.__factory_methods[component_type]()

    def register(self, component_type:str, factory_method: Callable[[], MLComponentNodeViewModel],
                 factory_method_with_descriptor: Callable[[MLComponentDescriptor], MLComponentNodeViewModel]):
        if component_type in self.__factory_methods_with_descriptor:
            raise Exception(f'Component Type {component_type} is allready registered')

        if component_type in self.__factory_methods:
            raise Exception(f'Component Type {component_type} is allready registered')

        self.__factory_methods_with_descriptor[component_type] = factory_method_with_descriptor
        self.__factory_methods[component_type] = factory_method

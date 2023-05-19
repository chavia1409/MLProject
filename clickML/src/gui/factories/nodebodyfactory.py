from typing import Callable
from gui.factories.nodebodyfactorybase import NodeBodyFactoryBase


class NodeBodyFactory(NodeBodyFactoryBase):

    def __init__(self) -> None:
        self.__factoryMethodeMap = {}
        
    def create(self, component_type:str):
        if component_type not in self.__factoryMethodeMap:
            raise Exception(f'Component Type {component_type} is not registered. Please registere it')
        return self.__factoryMethodeMap[component_type]()

    def register(self, component_type:str, factory_methode: Callable[[], object]):
        if component_type in self.__factoryMethodeMap:
            raise Exception(f'Component Type {component_type} is allready registered')
        self.__factoryMethodeMap[component_type] = factory_methode

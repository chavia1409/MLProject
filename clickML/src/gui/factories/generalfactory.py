from typing import Type, Callable

from gui.factories.generalfactorybase import GeneralFactoryBase


class GeneralFactory(GeneralFactoryBase):

    def __init__(self):
        self.__factory_methode_map = {}

    def create(self, t: Type, **kwargs):
        if t not in self.__factory_methode_map:
            raise Exception(f'Type {t} is not registered')
        return self.__factory_methode_map[t](kwargs)

    def register(self, t: Type, factory_methode: Callable[[dict], object]):
        if t in self.__factory_methode_map:
            raise Exception(f'Type {t} is already registered')
        self.__factory_methode_map[t] = factory_methode

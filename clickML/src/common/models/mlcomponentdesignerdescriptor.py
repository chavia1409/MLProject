import uuid
from typing import Dict


class MLComponentDesignerDescriptor:

    def __init__(self, component_id:uuid, x, y):
        self.__component_id = component_id
        self.__x = x
        self.__y = y

    @property
    def component_id(self):
        return self.__component_id

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

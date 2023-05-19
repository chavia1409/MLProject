import uuid
from typing import List

from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.mlcomponentdesignerdescriptor import MLComponentDesignerDescriptor
from gui.mvvm.viewmodelbase import ViewModelBase
from varname import nameof
from .inputdotviewmodel import InputDotViewModel
from .outputdotviewmodel import OutputDotViewModel
from ..helper import get_input_dots
from ...factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase


class NodeViewModelBase(ViewModelBase):
    __x = 0
    __y = 0

    def __init__(self):
        super().__init__()

    @property
    def component_type(self) -> str:
        return 'Base'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__x == value:
            return
        self.__x = value
        self._notify_property_changed('x', value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__y == value:
            return
        self.__y = value
        self._notify_property_changed('y', value)

    @property
    def title(self):
        return 'Base'


class MLComponentNodeViewModel(NodeViewModelBase):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor):
        super().__init__()
        self._descriptor = ml_component_descriptor

    @property
    def component_id(self):
        return self._descriptor.component_id

    @property
    def component_type(self):
        return self._descriptor.component_type

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        return None

    @property
    def ml_component_designer_descriptor(self) -> MLComponentDesignerDescriptor:
        return MLComponentDesignerDescriptor(self._descriptor.component_id, self.x, self.y)

    @ml_component_designer_descriptor.setter
    def ml_component_designer_descriptor(self, value):
        self.x = value.x
        self.y = value.y

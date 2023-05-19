from common.models.component_descriptors.text_processing.cd_text_console_input import TextConsoleInputDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import OutputDotViewModelFactoryBase, \
    InputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel


class TextConsoleInputNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__output = self.__output_dot_factory.create(self._descriptor.component_id, self._descriptor.suc)
    @property
    def title(self):
        return 'Text Console Input'

    @property
    def output(self):
        return self.__output

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = TextConsoleInputDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        return descriptor
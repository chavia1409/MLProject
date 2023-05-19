from varname import nameof

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_replace_sequences import ReplaceSequencesDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class ReplaceSequencesNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__input_dot_factory = input_dot_factory
        self.__output_dot_factory = output_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__input: InputDotViewModel = self.__input_dot_factory.create(self._descriptor.component_id,
                                                                          self._descriptor.pre)
        self.__output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__sequences_original = self._descriptor.sequences_original
        if self.__sequences_original == DEFAULT:
            self.__sequences_original = []
        self.__sequences_replace = self._descriptor.sequences_replace
        if self.__sequences_replace == DEFAULT:
            self.__sequences_replace = []

    @property
    def sequences_original(self):
        return self.__sequences_original

    @sequences_original.setter
    def sequences_original(self, value):
        if value == self.__sequences_original:
            return
        self.__sequences_original = value
        self._notify_property_changed('sequences_original', value)

    @property
    def sequences_replace(self):
        return self.__sequences_replace

    @sequences_replace.setter
    def sequences_replace(self, value):
        if value == self.__sequences_replace:
            return
        self.__sequences_replace = value
        self._notify_property_changed('sequences_replace', value)

    @property
    def title(self):
        return 'Replace Sequences'

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = ReplaceSequencesDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        descriptor.pre = self.input.predecessor_descriptor
        if self.__sequences_original == []:
            descriptor.sequences_original = DEFAULT
        else:
            descriptor.sequences_original = self.__sequences_original

        if self.__sequences_replace == []:
            descriptor.sequences_replace = DEFAULT
        else:
            descriptor.sequences_replace = self.__sequences_replace
        return descriptor

    @property
    def input(self):
        return self.__input

    @property
    def output(self):
        return self.__output

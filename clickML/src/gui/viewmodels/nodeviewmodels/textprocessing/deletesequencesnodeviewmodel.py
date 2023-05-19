from varname import nameof

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_delete_sequences import DeleteSequencesDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class DeleteSequencesNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase,):
        super().__init__(ml_component_descriptor)
        self.__input_dot_factory = input_dot_factory
        self.__output_dot_factory = output_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__input: InputDotViewModel = self.__input_dot_factory.create(self._descriptor.component_id,
                                                                          self._descriptor.pre)
        self.__sequences = self._descriptor.sequences
        if self.__sequences == DEFAULT:
            self.__sequences = []

    @property
    def title(self):
        return 'Delete Sequences'

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        if value == self.__output:
            return
        self.__output = value
        self._notify_property_changed("output", value)

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, value):
        if value == self.__input:
            return
        self.__input = value
        self._notify_property_changed("input", value)

    @property
    def sequences(self):
        return self.__sequences

    @sequences.setter
    def sequences(self, value):
        if value == self.__sequences:
            return
        self.__sequences = value
        self._notify_property_changed('sequences', value)





    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = DeleteSequencesDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        descriptor.pre = self.input.predecessor_descriptor
        if self.__sequences == []:
            descriptor.sequences = DEFAULT
        else:
            descriptor.sequences = self.__sequences

        return descriptor
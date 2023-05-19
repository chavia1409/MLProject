"""READY FOR IMPLEMENTATION"""

import uuid
from typing import Union

from backend.ml_components.csv_processing.c_save_to_ArrayOrCSV import Create_Array_CSV
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT


class SaveToArrayOrCsvDescriptor(MLComponentDescriptor):
    """
    Descriptor for ReadCSV component

    pre: Predecessor Descriptor
        (required)
    suc: Successor Descriptor
        (optional)

    #Attributes for creating Read_CSV:
    ArrayOrCsv = str
        (required - Choice between save to csv or save to array; Default: save to csv)
    targetFilePath : str
        (required if 'save to csv' is ticked - file path where the new Read_CSV should be saved)

    targetFileName = str
        (optional - file name of the new Read_CSV file)
    indexing = bool
        (optional, default: Yes - Read_CSV will be created without indexes unless opted in)

    arrayName = str
        (optional, in case of Create_Array_CSV succeding Regression modules
            this attribute will be already saved within the script.
            If it's not already given, the name of the to be translated array
            MUST be passed)
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        self.pre = PredecessorDescriptor("Input")  # required
        self.suc = SuccessorDescriptor("Array output")  # optional

        self.ArrayOrCsv: str = "Read_CSV"  # required, 'To Array' or 'To CSV' selection (Default: CSV)
        self.targetFileName: str = DEFAULT  # optional
        self.targetFilePath: str = DEFAULT  # required, path to saving location
        self.indexing: bool = True  # required

    @property
    def component_type(self) -> str:
        return Create_Array_CSV.__name__

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    def restore_component(self) -> Create_Array_CSV:
        return Create_Array_CSV(self)

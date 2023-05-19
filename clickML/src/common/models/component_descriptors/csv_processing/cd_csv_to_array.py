"""READY FOR IMPLEMENTATION"""
import copy
import uuid
from typing import Union

from backend.ml_components.csv_processing.c_csv_to_array import CSV_to_array
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT


class ReadCSVDescriptor(MLComponentDescriptor):
    """
    Descriptor for reading a Read_CSV from given filepath and transforming it into an array

    #Deleted: Predecessor obsolete

    suc: SuccessorDescriptor
        (required)

    #Attributes for CSV_to_array / mainf_csv_read()
    csvFilePathX = str
        (required) Path of csv file as string
    csvFilePathY = str
        (required) Path of second dataset
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id = component_id

        self.suc = SuccessorDescriptor("Processed Read_CSV")  # REQUIRED

        # required Attributes:
        self.csvFilePath: str = DEFAULT  # REQUIRED

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return CSV_to_array.__name__

    def restore_component(self) -> CSV_to_array:
        return CSV_to_array(self)

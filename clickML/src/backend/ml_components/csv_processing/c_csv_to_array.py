from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from common.exceptions.click_ml_exceptions import SpecificationError
import pandas as pd

if TYPE_CHECKING:
    from common.models.component_descriptors.csv_processing.cd_csv_to_array import ReadCSVDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


# REACHED FINAL STATE
class CSV_to_array(MLComponent):

    def __init__(self, descriptor: ReadCSVDescriptor) -> None:
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.suc = desc.suc

        self.csvFilePath = desc.csvFilePath

        self.csvName: str = f"CSV_{HelpingMethods.check_return_use_validity(self.type())}"
        HelpingMethods.ComponentList.append(self.type())

    # DONE
    def to_code(self) -> str:
        code: str = self.csvName + " = pd.read_csv(self.csvFilePath) \n"

        return code

    def get_needed_imports(self) -> list[str]:
        return ["import pandas as pd"]

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return []

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return {self.suc.csvName: self.csvName}

    def do_preprocessing(self) -> None:
        pass

    # DONE
    def check_if_valid(self) -> None:
        self.attribute_check()

    def attribute_check(self):
        try:
            testing = pd.read_csv(self.csvFilePath)
        except FileNotFoundError:
            raise SpecificationError("csvFilePath", self.csvFilePath, CSV_to_array.__name__, "File is not readable")

    def type(self) -> Components:
        return Components.CREATE_CSV

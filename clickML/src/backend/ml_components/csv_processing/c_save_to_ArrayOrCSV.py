from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
import numpy as np
from common.exceptions.click_ml_exceptions import ComponentConnectionError, ComponentCompositionError, InternalError

if TYPE_CHECKING:
    from common.models.component_descriptors.csv_processing.cd_save_array_csv import SaveToArrayOrCsvDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


class Create_Array_CSV(MLComponent):

    def type(self) -> Components:
        return Components.CREATE_CSV

    def __init__(self, descriptor: SaveToArrayOrCsvDescriptor):
        self.resultingArrayName = None
        self.pred_array = None
        self.pred_component_name = None
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.suc = desc.suc

        self.CsvOrArray = desc.ArrayOrCsv
        self.fileName = desc.targetFileName
        self.filePath = desc.targetFilePath
        self.indexing = desc.indexing

        HelpingMethods.ComponentList.append(self.type())

    def to_code(self):
        code = self.pdt_to_array() + "\n"

        # TODO
        code += f"{self.resultingArrayName}.to_csv({self.fileName}) \n"

        return code

    def get_needed_imports(self) -> list[str]:
        return ["import pandas as pd", "import numpy as np"]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return {self.suc.name: list[self.type(), self.resultingArrayName]}

    def check_if_valid(self) -> None:
        self.check_pred()

    def do_preprocessing(self) -> None:
        self.pred_component_name = self.pre[0]
        self.pred_array = self.pre[1]

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    def pdt_to_array(self) -> str:
        new_name = f'ResultArray_{HelpingMethods.check_return_use_validity()} '
        self.resultingArrayName = f"Resulting_Array_{HelpingMethods.check_return_use_validity()}"

        return f'{self.resultingArrayName}.concatenate({self.pred_array}, {new_name})'

    def check_pred(self) -> None:
        if self.pred_component_name is not Components.TRAIN_FIT_LINEAR or Components.TRAIN_FIT_LOGISTIC or Components.PREDICT_LIN_LOG:
            raise ComponentCompositionError(self.type())

        try:
            if self.pred_component_name is (Components.TRAIN_FIT_LOGISTIC or Components.TRAIN_FIT_LINEAR):
                if self.pre[self.pre.len()] == self.type():
                    raise ComponentConnectionError(
                        self.type() + " has an Illegal connection to component " + self.pred_component_name)
        except IndexError:
            raise InternalError

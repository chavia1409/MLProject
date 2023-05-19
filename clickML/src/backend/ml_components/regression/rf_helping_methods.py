# Collaborators: Julian Klitzke \\
from __future__ import annotations

from typing import TYPE_CHECKING

from common.exceptions.click_ml_exceptions import InternalError, ProjectCompositionError

if TYPE_CHECKING:
    from backend.component_enum import Components


class HelpingMethods:
    check_count = 0
    ConstraintList: list[str] = None
    ComponentList: list[Components] = None
    RaiseError = True

    ConstraintError: bool

    @staticmethod
    def get_needed_imports(Type) -> list[str]:
        imports: list[str] = ["from sklearn.model_selection import train_test_split", "import numpy as np",
                              "import pandas as pd"]

        if Type == "linear":
            imports.append("from sklearn.linear_model import LinearRegressions as lg")
            return imports

        if Type == "logistic":
            imports.append("from sklearn.linear_model import LogisticRegression as logreg")
            return imports

        raise InternalError

    def check_desc_reg_type_validity_log(self) -> None:
        # This Method checks the validity of the regression, specifically wether the model was trained and fitted
        # @Taymaz: This method must not be modified. Please ask and explain how you want to modify it before

        for component in self.ComponentList:
            if component is Components.TRAIN_FIT_LOGISTIC:
                self.RaiseError = False

        if self.RaiseError:
            raise ProjectCompositionError("missing regression entry-point")

        if self.ComponentList[0] is not Components.Read_CSV:
            raise ProjectCompositionError("Missing Read_CSV input")

    def check_desc_reg_type_validity(self) -> None:
        # This Method checks the validity of the regression, specifically wether the model was trained and fitted

        for component in self.ComponentList:
            if component is Components.TRAIN_FIT_LOGISTIC or Components.TRAIN_FIT_LINEAR:
                self.RaiseError = False

        if self.RaiseError:
            raise ProjectCompositionError("missing regression entry-point")

        if self.ComponentList[0] is not Components.Read_CSV:
            raise ProjectCompositionError("Missing Read_CSV input")

    def check_constraint(self, constraint) -> bool:
        for const in self.ConstraintList:
            if constraint in const:
                return True

        return False

    def check_return_use_validity(self, _component_type) -> int:
        # Method as validity check

        match _component_type:
            case Components.PREDICT_LIN_LOG:
                return self.__count_use__(_component_type)
            case Components.TRAIN_FIT_LINEAR:
                return self.__count_use__(_component_type)
            case Components.TRAIN_FIT_LOGISTIC:
                return self.__count_use__(_component_type)
            case Components.Read_CSV:
                return self.__count_use__(_component_type)
            case Components.CREATE_CSV:
                return self.__count_use__(_component_type)

        raise InternalError()

    def __count_use__(self, component_type) -> int:
        count = 1

        if not component_type:
            raise InternalError("Internal error: missing argument")

        for _component_type in self.ComponentList:
            if _component_type is component_type:
                count += 1

        return count

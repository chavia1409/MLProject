from __future__ import annotations

from backend.code_generation_components.abstract_tools.project_type_validator import ProjectTypeValidator
from backend.ml_components.ml_component import MLComponent
from common.exceptions.click_ml_exceptions import ProjectCompositionError

from typing import TYPE_CHECKING

# if TYPE_CHECKING:
    # from backend.ml_components.regression.rf_helping_methods import HelpingMethods


class RegressionTypeValidator(ProjectTypeValidator):

    def check_if_valid(self, components: list[MLComponent]) -> None:
        """
        # Component Validation
        if HelpingMethods.RaiseError:
            raise ProjectCompositionError("Project module composition is invalid")

        # Domain check
        if HelpingMethods.ConstraintError:
            raise ProjectCompositionError("Invalid constraints")
        """
        """
        raises exception if something specific to regression projects is wrong,
        (general validity of project is provided (means check_if_valid is already called for all components and the
        project is connected))

        Points that need to be checked:
        - are the components combined in a way that is invalid for a project of this type (just look at combinations of
            components that are not adjacent, because everything else is already checked in the MLComponents)
        - are there special constraints for the domain of some user inputs in components (e.g. the sequential model
        for text processing projects may only have special types of layers)?
        """

    """
    Method may not be used for now:
    
    def check_component_order(self, components: list[MLComponent]):

        csv_1_exists: bool = False
        csv_2_exists: bool = False
        pred_fit_exists: bool = False

        for component in components:
            if component is ReadCSVDescriptor.component_type:
                csv_1_exists = True

            if csv_1_exists and component is ReadCSVDescriptor.component_type:
                csv_2_exists = True

            if component is (Train_Fit_Lin_Descriptor.component_type or
                            Train_Fit_Log_Descriptor.component_type):
                pred_fit_exists = True

            if csv_2_exists and component is not (Train_Fit_Lin_Descriptor.component_type or
                                                  Train_Fit_Log_Descriptor.component_type or
                                                  adapterDescriptor.component_type or plotDescriptor.component_type):
                raise ProjectCompositionError("")
    """

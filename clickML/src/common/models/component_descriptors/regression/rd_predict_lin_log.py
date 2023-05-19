import uuid
from typing import Union

from backend.ml_components.regression.r_predict_lin_log import Predict
from backend.ml_components.regression.r_predict_lin_log import pred_type
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT


class PredictDescriptor(MLComponentDescriptor):
    """
    pre = PredecessorDescriptor
        (required)
    suc = SuccessorDescriptor
        (optional - for further regression modules)
    suc 2 = SuccessorDescriptor
        (optional - e.g. save to csv module can be connected here)
    suc 3 = SuccessorDescriptor
        (optional - used to for plot module)

    Attributes:

        from_column: int
            (required)
        prediction_type: str
            (required - either 'PredictDescriptor' (this one's default), 'predict_proba (logistic)' or
            'predict_log_proba (logistic)' (single choice))
    """

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor('Prediction input')
        self.suc = SuccessorDescriptor('Prediction output')
        self.suc_2 = SuccessorDescriptor('Save_to')
        self.suc_3 = SuccessorDescriptor('Plot')

        self.from_column: Union[int, str, None] = None  # optional
        self.to_column: Union[int, str, None] = None  # optional
        self.from_row: Union[int, str, None] = None  # optional
        self.to_row: Union[int, str, None] = None  # optional

        self.prediction_type = pred_type.pred  # required - single choice

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Predict.__name__

    def restore_component(self) -> Predict:
        return Predict(self)

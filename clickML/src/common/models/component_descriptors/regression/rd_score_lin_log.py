import uuid

from backend.ml_components.regression.r_score_lin_log import ScoreLinLog
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class scoreDescriptor(MLComponentDescriptor):

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor("Regression input")  # required
        self.suc = SuccessorDescriptor("Output")  # optional

        self.print = False  # optional - as opt-out option / or single choice

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return ScoreLinLog.__name__

    def restore_component(self) -> ScoreLinLog:
        return ScoreLinLog(self)

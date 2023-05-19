# Collaborators: Julian Klitzke \\

from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_save_logfile import SaveLogfileDescriptor

# Most likely to be decommisioned
class SaveLogfile(MLComponent):

    def __init__(self, descriptor: SaveLogfileDescriptor):
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre

        self.filePath = desc.filePath

        self.pre_input = None

    logfile: list[str]
    logfilestr: str

    def write_logfile(self, output):
        self.logfilestr += self.logfile.pop(0)
        self.logfilestr += ">>> " + output + "\n\n"

    def save_logfile(self):
        pass
    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return[self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return[]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return{}

    def to_code(self) -> str:
        pass

    def get_needed_imports(self) -> list[str]:
        return[]

    def check_if_valid(self) -> None:
        pass

    def do_preprocessing(self) -> None:
        self.pre_input = self.toolkit.get_data_from_predecessor(self.pre)

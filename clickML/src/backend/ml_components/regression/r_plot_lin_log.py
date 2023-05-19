# Collaborators: Julian Klitzke \\

from __future__ import annotations

import copy
from typing import Any, TYPE_CHECKING

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_plot_ling_log import plotDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


class Plotter(MLComponent):

    def type(self) -> Components:
        return Components.PLOT_LIN_LOG

    def __init__(self, descriptor: plotDescriptor):
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.pre_2 = desc.pre_2

        self.pre_input_2 = None
        self.pre_input = None

        self.plt_x = None
        self.plt_y = None

        HelpingMethods.ComponentList.append(self.type())

    def to_code(self) -> str:
        code = f"plt.scatter({self.plt_x}, {self.plt_y}, marker='+', color='red')"
        code += f"plt.plot({self.plt_x}, {self.plt_y}, color = 'blue', linestyle = 6)"
        code += "plt.show()"

        # TODO: save plot to logfile

        return code

    def get_needed_imports(self) -> list[str]:
        return ["import matplotlib.pyplot as plt"]

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return[self.pre, self.pre_2]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return[]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return{}

    def do_preprocessing(self) -> None:
        self.pre_input = self.toolkit.get_data_from_predecessor(self.pre)
        self.pre_input_2 = self.toolkit.get_data_from_predecessor(self.pre_2)

    def check_if_valid(self) -> None:
        pass
    
    def check_predecessors(self):
        pass
        

from typing import List, Type

from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


def get_input_dots(vm) -> List[InputDotViewModel]:
    return get_attributes_with_type(vm, InputDotViewModel)


def get_output_dots(vm) -> List[OutputDotViewModel]:
    return get_attributes_with_type(vm, OutputDotViewModel)


def get_attributes_with_type(vm, t: Type):
    attributes = list(dir(vm))
    result = []
    for attr in attributes:
        if attr == 'ml_component_designer_descriptor':
            continue
        if not hasattr(vm, attr):
            continue
        if attr[:1] == '_':
            continue
        instance = getattr(vm, attr)
        if instance is None:
            continue
        if not isinstance(instance, t):
            continue
        result.append(instance)
    return result


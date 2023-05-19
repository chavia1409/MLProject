import uuid
from dataclasses import dataclass, field
from typing import Union

from common.models.component_descriptors.component_constants import DEFAULT


@dataclass
class PredecessorDescriptor:
    """Reference on SuccessorDescriptor of predecessor component."""
    name: str
    name_prev: str = field(init=False, default=DEFAULT)
    id_prev: Union[type(uuid), str] = field(init=False, default=DEFAULT)


@dataclass
class SuccessorDescriptor:
    """Reference on PredecessorDescriptor of successor component."""
    name: str
    name_next: str = field(init=False, default=DEFAULT)
    id_next: Union[type(uuid), str] = field(init=False, default=DEFAULT)

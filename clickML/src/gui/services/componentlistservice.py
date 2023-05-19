from abc import ABC

from gui.services.componentlistservicebase import ComponentListServiceBase


class ComponentListService(ComponentListServiceBase):
    def __init__(self):
        self.componentList = []

    def set(self, descriptor, name, parent):
        self.componentList.append([descriptor, name, parent])

    def get_list(self) -> list[[]]:
        return self.componentList

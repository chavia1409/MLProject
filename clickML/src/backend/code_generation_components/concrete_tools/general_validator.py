from backend.code_generation_components.abstract_tools.project_general_validator import ProjectGeneralValidator
from backend.ml_components.ml_component import MLComponent
from common.exceptions.click_ml_exceptions import ProjectCompositionError
from common.models.component_descriptors.component_constants import DEFAULT


class GeneralValidator(ProjectGeneralValidator):

    def check_if_valid(self, components: list[MLComponent]) -> None:
        self.__check_connectivity(components)
        self.__component_validation(components)

    @staticmethod
    def __component_validation(components: list[MLComponent]) -> None:
        """calls check_if_valid() for all MLComponents"""
        for component in components:
            component.check_if_valid()

    @staticmethod
    def __check_connectivity(components: list[MLComponent]) -> None:
        """checks if component graph is connected"""
        unconnected_components = components.copy()
        connected_components = [unconnected_components[0], ]
        while True:
            found_connected_component = False
            unconnected_components = \
                [component for component in unconnected_components if component not in connected_components]
            for component in unconnected_components:
                if not GeneralValidator.__is_connected(component, connected_components):
                    continue
                connected_components.append(component)
                found_connected_component = True
            if not found_connected_component:
                break
        if unconnected_components:
            raise ProjectCompositionError("Some components are not connected to project.")

    @staticmethod
    def __is_connected(component: MLComponent, connected_components: list[MLComponent]) -> bool:
        """checks if component has any connection to connected_components"""
        connections = []
        for connected_component in connected_components:
            connections += [pre.id_prev for pre in connected_component.predecessors if pre.id_prev != DEFAULT]
            connections += [suc.id_next for suc in connected_component.successors if suc.id_next != DEFAULT]
        return component.id in connections

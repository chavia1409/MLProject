from backend.code_generation_components.abstract_tools.project_optimizer import ProjectOptimizer
from backend.ml_components.ml_component import MLComponent
from backend.ml_components.text_processing.c_delete_sequences import DeleteSequences
from backend.ml_components.text_processing.c_letter_case import LetterCase
from backend.ml_components.text_processing.c_replace_sequences import ReplaceSequences
from backend.project_toolkit import ProjectToolkit
from common.models.component_descriptors.component_constants import DEFAULT


class Optimizer(ProjectOptimizer):

    def optimize_project(self, components: list[MLComponent]) -> list[MLComponent]:
        components = self.__optimize_letter_case(components)
        components = self.__optimize_replace_sequences(components)
        components = self.__optimize_delete_sequences(components)
        return components

    def __optimize_letter_case(self, components: list[MLComponent]) -> list[MLComponent]:
        """Using only the last configuration of LetterCase components when multiple ones follow one another directly"""
        optimized_components = components
        toolkit = ProjectToolkit(components)

        for component in optimized_components:

            # checking if optimization is possible
            if not isinstance(component, LetterCase) or component.pre.id_prev == DEFAULT:
                continue
            predecessor = toolkit.get_component(component.pre.id_prev)
            if not isinstance(predecessor, LetterCase):
                continue

            # setting predecessor and successor
            predecessor.suc = component.suc
            predecessor.case = component.case
            if component.suc.id_next != DEFAULT:
                successor = toolkit.get_component(component.suc.id_next)
                for pre in successor.predecessors:
                    if pre.id_prev == component.id:
                        pre.id_prev = predecessor.id
                        pre.name_prev = predecessor.suc.name

            # deleting unneeded component and checking if more optimizations of this kind are possible
            optimized_components.remove(component)
            optimized_components = self.__optimize_letter_case(optimized_components)
            break

        return optimized_components

    def __optimize_replace_sequences(self, components: list[MLComponent]) -> list[MLComponent]:
        """merging ReplaceSequences components that follow one another directly"""

        optimized_components = components
        toolkit = ProjectToolkit(components)

        for component in optimized_components:

            # checking if optimization is possible
            if not isinstance(component, ReplaceSequences) or component.pre.id_prev == DEFAULT:
                continue
            predecessor = toolkit.get_component(component.pre.id_prev)
            if not isinstance(predecessor, ReplaceSequences):
                continue

            # setting predecessor and successor
            predecessor.suc = component.suc
            predecessor.sequences_original += component.sequences_original
            predecessor.sequences_replace += component.sequences_replace
            if component.suc.id_next != DEFAULT:
                successor = toolkit.get_component(component.suc.id_next)
                for pre in successor.predecessors:
                    if pre.id_prev == component.id:
                        pre.id_prev = predecessor.id
                        pre.name_prev = predecessor.suc.name

            # deleting unneeded component and checking if more optimizations of this kind are possible
            optimized_components.remove(component)
            optimized_components = self.__optimize_replace_sequences(optimized_components)
            break

        return optimized_components

    def __optimize_delete_sequences(self, components: list[MLComponent]) -> list[MLComponent]:
        """merging DeleteSequences components that follow one another directly"""

        optimized_components = components
        toolkit = ProjectToolkit(components)

        for component in optimized_components:

            # checking if optimization is possible
            if not isinstance(component, DeleteSequences) or component.pre.id_prev == DEFAULT:
                continue
            predecessor = toolkit.get_component(component.pre.id_prev)
            if not isinstance(predecessor, DeleteSequences):
                continue

            # setting predecessor and successor
            predecessor.suc = component.suc
            predecessor.sequences += component.sequences
            if component.suc.id_next != DEFAULT:
                successor = toolkit.get_component(component.suc.id_next)
                for pre in successor.predecessors:
                    if pre.id_prev == component.id:
                        pre.id_prev = predecessor.id
                        pre.name_prev = predecessor.suc.name

            # deleting unneeded component and checking if more optimizations of this kind are possible
            optimized_components.remove(component)
            optimized_components = self.__optimize_delete_sequences(optimized_components)
            break

        return optimized_components

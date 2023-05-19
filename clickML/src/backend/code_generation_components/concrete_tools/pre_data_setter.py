from backend.code_generation_components.abstract_tools.project_pre_data_setter import ProjectPreDataSetter
from backend.ml_components.ml_component import MLComponent
from backend.ml_components.ml_layer_component import MLLayerComponent
from backend.project_toolkit import ProjectToolkit


class PreDataSetter(ProjectPreDataSetter):

    def set_pre_data(self, components: list[MLComponent]) -> list[MLComponent]:
        toolkit = ProjectToolkit(components)

        # giving components access to global scope
        MLComponent.toolkit = toolkit
        MLLayerComponent.toolkit = toolkit

        # calling do_preprocessing from MLComponents in valid order
        already_set = []
        while toolkit.has_settable_component(already_set):
            for component in components:
                if toolkit.has_unset_predecessors(component, already_set):
                    continue
                component.do_preprocessing()
                already_set.append(component)

        return components







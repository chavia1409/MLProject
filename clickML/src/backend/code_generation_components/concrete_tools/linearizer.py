from backend.code_generation_components.abstract_tools.project_linearizer import ProjectLinearizer
from backend.ml_components.ml_component import MLComponent
from backend.project_toolkit import ProjectToolkit


class Linearizer(ProjectLinearizer):

    def to_linear_sequence(self, components: list[MLComponent]) -> list[MLComponent]:

        toolkit = ProjectToolkit(components)
        unused_components = components.copy()
        linearized_components = []

        while toolkit.has_settable_component(linearized_components):
            unused_components = [component for component in unused_components if component not in linearized_components]
            for component in unused_components:
                if toolkit.has_unset_predecessors(component, linearized_components):
                    continue
                linearized_components.append(component)
        return linearized_components

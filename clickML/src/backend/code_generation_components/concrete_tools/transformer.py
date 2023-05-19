from backend.code_generation_components.abstract_tools.project_transformer import ProjectTransformer
from backend.ml_components.ml_component import MLComponent
from common.models.mlcomponentdescriptor import MLComponentDescriptor


class Transformer(ProjectTransformer):
    """turns a list of MlComponentDescriptors into list of MlComponents"""

    def do_transformation(self, components: list[MLComponentDescriptor]) -> list[MLComponent]:
        return [component.restore_component() for component in components]

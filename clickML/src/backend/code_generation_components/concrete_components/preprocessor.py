from backend.code_generation_components.abstract_components.project_preprocessor import ProjectPreprocessor
from backend.code_generation_components.abstract_tools.project_optimizer import ProjectOptimizer
from backend.code_generation_components.abstract_tools.project_pre_data_setter import ProjectPreDataSetter
from backend.code_generation_components.abstract_tools.project_transformer import ProjectTransformer
from backend.ml_components.ml_component import MLComponent
from common.models.mlcomponentdescriptor import MLComponentDescriptor


class Preprocessor(ProjectPreprocessor):
    """class for needed conversion of given data model from frontend to complete model"""

    def __init__(self, transformer: ProjectTransformer, pre_data_setter: ProjectPreDataSetter,
                 optimizer: ProjectOptimizer) -> None:
        self.__transformer = transformer
        self.__pre_data_setter = pre_data_setter
        self.__optimizer = optimizer

    def do_preprocessing(self, components: list[MLComponentDescriptor]) -> list[MLComponent]:
        """returns preprocessed set of MLComponents"""

        # turning set[MLComponentDescriptor] to set[MLComponent]
        transformed_components = self.__transformer.do_transformation(components)

        # setting information about predecessors of components
        pre_set_components = self.__pre_data_setter.set_pre_data(transformed_components)

        # optimizing project structure to equivalent but shortest possible shape
        optimized_components = self.__optimizer.optimize_project(pre_set_components)

        return optimized_components

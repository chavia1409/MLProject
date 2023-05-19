from backend.code_generation_components.abstract_components.project_code_generator import ProjectCodeGenerator
from backend.code_generation_components.abstract_tools.project_code_combiner import ProjectCodeCombiner
from backend.code_generation_components.abstract_tools.project_code_styler import ProjectCodeStyler
from backend.code_generation_components.abstract_tools.project_header_maker import ProjectHeaderMaker
from backend.code_generation_components.abstract_tools.project_import_manager import ProjectImportManager
from backend.code_generation_components.abstract_tools.project_linearizer import ProjectLinearizer
from backend.ml_components.ml_component import MLComponent


class CodeGenerator(ProjectCodeGenerator):
    """class for putting code and import snippets of MLComponents together"""

    def __init__(self, linearizer: ProjectLinearizer, header_maker: ProjectHeaderMaker,
                 import_manager: ProjectImportManager, code_combiner: ProjectCodeCombiner,
                 code_styler: ProjectCodeStyler) -> None:
        self.__linearizer = linearizer
        self.__header_maker = header_maker
        self.__import_manager = import_manager
        self.__code_combiner = code_combiner
        self.__code_styler = code_styler

    def to_code(self, components: list[MLComponent], project_name: str) -> str:
        """returns a string containing the code for given components"""

        # turning set[MLComponent] to list[MLComponent]
        linearized_components = self.__linearizer.to_linear_sequence(components)

        # creating file header
        header = self.__header_maker.create_file_header(components, project_name)

        # generating imports
        imports = self.__import_manager.get_shaped_imports(linearized_components)

        # generating rest of code
        code = self.__code_combiner.get_combined_code(linearized_components)

        # combining code parts
        merged_code = header + imports + code

        # improving code style
        styled_code = self.__code_styler.improve_style(merged_code)

        return styled_code

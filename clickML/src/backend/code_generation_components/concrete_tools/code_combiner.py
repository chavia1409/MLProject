from backend.code_generation_components.abstract_tools.project_code_combiner import ProjectCodeCombiner
from backend.ml_components.ml_component import MLComponent


class CodeCombiner(ProjectCodeCombiner):

    def get_combined_code(self, components: list[MLComponent]) -> str:
        code = ""
        for component in components:
            code += (component.to_code().rstrip() + "\n\n")
        return code

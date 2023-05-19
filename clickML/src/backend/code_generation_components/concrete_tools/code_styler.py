from backend.code_generation_components.abstract_tools.project_code_styler import ProjectCodeStyler


class CodeStyler(ProjectCodeStyler):

    def improve_style(self, code: str) -> str:
        return (code.strip() + "\n").replace("\t", "    ")

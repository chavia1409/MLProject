from datetime import date

from backend.code_generation_components.abstract_tools.project_header_maker import ProjectHeaderMaker
from backend.ml_components.ml_component import MLComponent
from .type_categorizer import TypeCategorizer


class HeaderMaker(ProjectHeaderMaker):

    def create_file_header(self, components: list[MLComponent], project_name: str) -> str:
        project_type = TypeCategorizer.get_most_likely_category(components).value
        return f'"""\n' \
               f"Python script generated with clickML.\n\n" \
               f"Project name: {project_name}\n" \
               f"Project type: {project_type.upper()}\n" \
               f"Creation date: {date.today()}\n" \
               f"Number of MLComponents: {len(components)}\n" \
               f'"""\n\n'

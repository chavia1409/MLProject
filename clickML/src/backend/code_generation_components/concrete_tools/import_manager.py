from backend.code_generation_components.abstract_tools.project_import_manager import ProjectImportManager
from backend.ml_components.ml_component import MLComponent


class ImportManager(ProjectImportManager):

    def get_shaped_imports(self, components: list[MLComponent]) -> str:
        import_list = []
        for component in components:
            import_list += component.get_needed_imports()
        import_list = list(set(ImportManager.__imports_to_shape(import_list)))
        import_list = ImportManager.__imports_in_order(import_list)
        imports = ""
        for needed_import in import_list:
            imports += (needed_import + "\n")
        return imports + "\n" if imports else ""

    @staticmethod
    def __imports_to_shape(import_list: list[str]) -> list[str]:
        """Makes sure that given import statements fit a basic shape."""
        shaped_import_list = []
        for needed_import in import_list:
            import_split = needed_import.strip().split()
            import_split[0] += " "
            for import_snippet in import_split[1:]:
                if import_snippet == "import" or import_snippet == "as":
                    import_split[import_split.index(import_snippet)] = " " + import_snippet + " "
            shaped_import = "".join(import_split).replace(",", ", ")
            if len(shaped_import) > 120:
                index = shaped_import.rfind("import")
                shaped_import = shaped_import[:index-1] + "\n\t" + shaped_import[index:]
            shaped_import_list.append(shaped_import)
        return shaped_import_list

    @staticmethod
    def __imports_in_order(import_list: list[str]) -> list[str]:
        """Puts given imports in an order."""
        ordered_import_list = []

        starts_with_import = [imp for imp in import_list if imp.startswith("import")]
        starts_with_import.sort()
        ordered_import_list += starts_with_import

        starts_with_from = [imp for imp in import_list if imp.startswith("from")]
        starts_with_from.sort()
        ordered_import_list += starts_with_from

        return ordered_import_list

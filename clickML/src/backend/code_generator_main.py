"""implements CodeGenerator interface"""

import os
from ast import parse

from backend.code_generation_components.abstract_components.project_code_generator import ProjectCodeGenerator
from backend.code_generation_components.abstract_components.project_preprocessor import ProjectPreprocessor
from backend.code_generation_components.abstract_components.project_validator import ProjectValidator
from common.exceptions.click_ml_exceptions import SpecificationError, InternalError, ProjectCompositionError
from common.interfaces.PythonCodeGenerator import CodeGenerator
from common.models.mlcomponentdescriptor import MLComponentDescriptor


class CodeGeneratorMain(CodeGenerator):

    def __init__(self, preprocessor: ProjectPreprocessor, validator: ProjectValidator,
                 generator: ProjectCodeGenerator) -> None:
        self.__preprocessor = preprocessor
        self.__validator = validator
        self.__generator = generator

    def generate_code(self, ml_component_descriptors: list[MLComponentDescriptor], project_name: str) -> str:
        """returns code for given MLComponentDescriptors if everything is valid"""

        if not ml_component_descriptors:
            raise ProjectCompositionError("Project should have at least one component!")

        # turning set of MLComponentDescriptors to set of MLComponents, setting code variable names, optimizing etc.
        components_preprocessed = self.__preprocessor.do_preprocessing(ml_component_descriptors)

        # checking if given model is valid
        self.__validator.check_if_valid(components_preprocessed)

        # generating python code from model
        generated_code = self.__generator.to_code(components_preprocessed, project_name)

        # internal check if code is parsable, just for debugging
        try:
            parse(generated_code)
        except SyntaxError:
            raise InternalError("Parsing went wrong!") from None

        return generated_code

    def generate_unchecked_code(self, ml_component_descriptors: list[MLComponentDescriptor], project_name: str) -> str:
        """returns code for given MLComponentDescriptors without checking if valid"""

        if not ml_component_descriptors:
            raise ProjectCompositionError("Project should have at least one component!")

        # turning set of MLComponentDescriptors to set of MLComponents, setting code variable names, optimizing etc.
        components_preprocessed = self.__preprocessor.do_preprocessing(ml_component_descriptors)

        # generating python code from model
        generated_code = self.__generator.to_code(components_preprocessed, project_name)

        return generated_code

    @staticmethod
    def code_to_file(code: str, saving_dir: str, project_name: str) -> None:
        """writes given code to specified file"""

        if not os.path.isdir(saving_dir):
            raise SpecificationError("saving_dir", saving_dir, "ProjectModel")
        with open(os.path.join(saving_dir, f"{project_name}.py"), "w") as file:
            file.write(code)

    def generate_code_file(self, ml_components: list[MLComponentDescriptor],
                           saving_dir: str, name: str, validator_mode: str = "on") -> None:
        """generates code from set of MLComponentDescriptors and writes it to given file"""

        generator_callables = {"on": self.generate_code, "off": self.generate_unchecked_code}
        generated_code = generator_callables[validator_mode](ml_components, name)
        self.code_to_file(generated_code, saving_dir, name)

from backend.code_generation_components.abstract_tools.project_type_validator import ProjectTypeValidator
from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from backend.ml_components.neural_networks.c_sequential_model import SequentialModel
from backend.ml_components.neural_networks.keras_layers.l_dense import Dense
from backend.project_toolkit import ProjectToolkit
from common.exceptions.click_ml_exceptions import SpecificationError, ProjectCompositionError


class TextGenerationTypeValidator(ProjectTypeValidator):

    def check_if_valid(self, components: list[MLComponent]) -> None:
        self.__check_component_types(components)
        self.__check_number_of_occurrences(components)
        self.__check_component_domain_constraints(components)

    @staticmethod
    def __check_component_types(components: list[MLComponent]):

        valid_types = [Components.DELETE_SEQUENCES, Components.DIVIDE_CHARS_BY_LENGTH,
                       Components.DIVIDE_CHARS_BY_SENTENCES, Components.DIVIDE_WORDS_BY_LENGTH,
                       Components.DIVIDE_WORDS_BY_SENTENCES, Components.GENERATE_CHARS, Components.GENERATE_WORDS,
                       Components.LETTER_CASE, Components.PRINT_TEXT, Components.REPLACE_SEQUENCES,
                       Components.SAVE_TEXT, Components.TEXT_CONSOLE_INPUT, Components.TEXT_READER,
                       Components.SEQUENTIAL_MODEL, Components.TRAIN_SEQUENTIAL]

        for component in components:
            if component.type() not in valid_types:
                raise ProjectCompositionError(f"The component {component.type().value} is not valid for "
                                              f"text generation projects!")

    @staticmethod
    def __check_number_of_occurrences(components: list[MLComponent]):
        toolkit = ProjectToolkit(components)

        input_types = {Components.TEXT_READER, Components.TEXT_CONSOLE_INPUT}
        divide_types = {Components.DIVIDE_CHARS_BY_LENGTH, Components.DIVIDE_CHARS_BY_SENTENCES,
                        Components.DIVIDE_WORDS_BY_LENGTH, Components.DIVIDE_WORDS_BY_SENTENCES}
        generator_types = {Components.GENERATE_CHARS, Components.GENERATE_WORDS}

        if toolkit.get_number_of_occurrences(input_types) > 1:
            raise ProjectCompositionError("Only one text input component allowed!")
        if toolkit.get_number_of_occurrences(divide_types) > 1:
            raise ProjectCompositionError("Only one text divider component allowed!")
        if toolkit.get_number_of_occurrences(generator_types) > 1:
            raise ProjectCompositionError("Only one text generator component allowed!")

    @staticmethod
    def __check_component_domain_constraints(components: list[MLComponent]) -> None:
        for component in components:
            if not isinstance(component, SequentialModel):
                continue
            valid_layers = {Components.LSTM, Components.GRU, Components.DENSE, Components.DROPOUT}
            layers_repr = [layer.type().value for layer in component.layers]
            if not {layer.type() for layer in component.layers}.issubset(valid_layers):
                raise SpecificationError("layers", layers_repr, component.type().value,
                                         "Sequential model can only contain 'Dense', 'Dropout', "
                                         "'LSTM' and 'GRU' layers.")
            if not(isinstance(component.layers[-1], Dense) and component.layers[-1].activation == "softmax"):
                raise SpecificationError("layers", layers_repr, component.type().value,
                                         "Last layer must be 'Dense' with 'softmax' activation.")



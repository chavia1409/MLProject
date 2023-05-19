from backend.code_generation_components.abstract_tools.project_type_categorizer import ProjectTypeCategorizer
from backend.component_enum import Categories, Components
from backend.ml_components.ml_component import MLComponent


class TypeCategorizer(ProjectTypeCategorizer):
    """determines category of given ClickMlProjectModel"""

    def get_category(self, components: list[MLComponent]) -> Categories:
        return TypeCategorizer.get_most_likely_category(components)

    @staticmethod
    def get_most_likely_category(components: list[MLComponent]) -> Categories:
        type_probabilities = {
            Categories.REGRESSION: TypeCategorizer.__regression_type_probability(components),
            Categories.IMAGE_CLASSIFICATION: TypeCategorizer.__image_classification_type_probability(components),
            Categories.TEXT_GENERATION: TypeCategorizer.__text_generation_type_probability(components)
        }
        return max(type_probabilities, key=type_probabilities.get)

    @staticmethod
    def __regression_type_probability(components: list[MLComponent]) -> float:
        """returns probability between zero and one whether it is a regression type"""
        possible_types = [Components.Read_CSV, Components.TRAIN_FIT_LINEAR, Components.TRAIN_FIT_LOGISTIC,
                          Components.CREATE_CSV, Components.SPARSIFY, Components.SET_PARAMS, Components.SCORE_LIN_LOG,
                          Components.GET_PARAMS_LOG, Components.SET_PARAMS, Components.PREDICT_LIN_LOG,
                          Components.PLOT_LIN_LOG, Components.DENSIFY_LOG, Components.DECISION_FUNCTION_LOG,
                          Components.ADAPTER]

        return TypeCategorizer.__calculate_rate(components, possible_types)

    @staticmethod
    def __image_classification_type_probability(components: list[MLComponent]) -> float:
        """returns probability between zero and one whether it is an image classification type"""
        possible_types = [Components.IMAGE_DATASET, Components.SEQUENTIAL_MODEL, Components.TRAIN_SEQUENTIAL]

        return TypeCategorizer.__calculate_rate(components, possible_types)

    @staticmethod
    def __text_generation_type_probability(components: list[MLComponent]) -> float:
        """returns probability between zero and one whether it is a text generation type"""

        possible_types = [Components.DELETE_SEQUENCES, Components.DIVIDE_CHARS_BY_LENGTH,
                          Components.DIVIDE_CHARS_BY_SENTENCES, Components.DIVIDE_WORDS_BY_LENGTH,
                          Components.DIVIDE_WORDS_BY_SENTENCES, Components.GENERATE_CHARS, Components.GENERATE_WORDS,
                          Components.LETTER_CASE, Components.PRINT_TEXT, Components.REPLACE_SEQUENCES,
                          Components.SAVE_TEXT, Components.TEXT_CONSOLE_INPUT, Components.TEXT_READER,
                          Components.SEQUENTIAL_MODEL, Components.TRAIN_SEQUENTIAL]

        return TypeCategorizer.__calculate_rate(components, possible_types)

    @staticmethod
    def __calculate_rate(components: list[MLComponent], possible_types: list[Components]) -> float:
        """calculates the fraction of how many components in the list match any valid type"""
        valid_components = 0
        for component in components:
            if component.type() in possible_types:
                valid_components += 1
        return valid_components / len(components)

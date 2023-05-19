"""module for GenerateWords component"""

from __future__ import annotations

import copy
from typing import TYPE_CHECKING

from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT
from common.exceptions.click_ml_exceptions import SpecificationError
from backend.ml_components.valid_connections import MODEL_PROVIDERS, WORD_GENERATION_INPUT
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_generate_words import GenerateWordsDescriptor


class GenerateWords(MLComponent):

    def __init__(self, descriptor: GenerateWordsDescriptor):
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        self.pre: PredecessorDescriptor = des.pre
        self.pre_2: PredecessorDescriptor = des.pre_2
        self.suc: SuccessorDescriptor = des.suc

        self.init_words_mode: str = des.init_words_mode
        self.number_of_words: str = des.number_of_words

        # preprocessing
        self.model: str = DEFAULT
        self.init_words: dict[str, str] = {}

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre, self.pre_2]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: "generated_text"}

    def to_code(self) -> str:
        start_input = "# picking start sequence\n" + self.init_words[self.init_words_mode] + "\n\n"
        generation = f"# generate text\n" \
                     f"{self.values_for_successors[self.suc.name]} = ''\n" \
                     f"for _ in range({self.number_of_words}):\n" \
                     f"\tx = numpy.reshape(pattern, (1, len(pattern), 1))\n" \
                     f"\tx = x / float(len(unique_words))\n" \
                     f"\tprediction = {self.model}.predict(x, verbose=0)\n" \
                     f"\tindex = numpy.argmax(prediction)\n" \
                     f"\tresult = int_to_word[index]\n" \
                     f"\t{self.values_for_successors[self.suc.name]} += ' ' + result\n" \
                     f"\tpattern.append(index)\n" \
                     f"\tpattern = pattern[1:]"
        return start_input + generation

    def get_needed_imports(self) -> list[str]:
        return ["import numpy", "from keras.models import Sequential"]

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if (isinstance(self.number_of_words, str) and self.number_of_words != DEFAULT or
                isinstance(self.number_of_words, int) and self.number_of_words < 0):
            raise SpecificationError("number_of_words", self.number_of_words, GenerateWords.__name__)

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre, self.pre_2], GenerateWords.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, MODEL_PROVIDERS)
        self.toolkit.check_pre_connection_validity(self.pre_2, WORD_GENERATION_INPUT)

    def do_preprocessing(self) -> None:
        self.model = self.toolkit.get_data_from_predecessor(self.pre)
        self.init_words = self.toolkit.get_data_from_predecessor(self.pre_2)

    def type(self) -> Components:
        return Components.GENERATE_WORDS

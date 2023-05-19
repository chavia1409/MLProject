from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import BASIC_TEXT_PREPROCESSING_CONNECTIONS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_divide_words_by_length \
        import DivideWordsByLengthDescriptor


class DivideWordsByLength(MLComponent):
    """
    Component that divides text into sequences of chars with fixed length.

    Attributes:
        # attributes for possible predecessors and successors
        pre: Union[type(uuid), str]
            (required) component which has as output a text, should be uuid
        suc: SuccessorDescriptor
            (optional) component that works on single net input for prediction
        suc_2: SuccessorDescriptor
            (optional) component that works on net input data
        suc_3: SuccessorDescriptor
            (optional) component that works on desired net output data
        suc_4: SuccessorDescriptor
            (optional) component that needs net input shape
        suc_5: SuccessorDescriptor
            (optional) component that needs net output shape

        # options
        seq_length: Union[int, str]
            (required) number of characters in each sequence

        # preprocessing
        text: str
            name of the text variable where this component should work on
    """

    def __init__(self, descriptor: DivideWordsByLengthDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.suc: SuccessorDescriptor = des.suc
        self.suc_2: SuccessorDescriptor = des.suc_2
        self.suc_3: SuccessorDescriptor = des.suc_3
        self.suc_4: SuccessorDescriptor = des.suc_4
        self.suc_5: SuccessorDescriptor = des.suc_5

        # options
        self.seq_length: Union[int, str] = des.seq_length

        # preprocessing
        self.text: str = DEFAULT

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc, self.suc_2, self.suc_3, self.suc_4, self.suc_5]

    @property
    def values_for_successors(self) -> dict[str, str]:
        first = "pattern = dataX[0]"
        last = "pattern = dataX[-1]"
        random = "start = numpy.random.randint(0, len(dataX)-1)\n" \
                 "pattern = dataX[start]"
        pred_dict = {"first": first, "last": last, "random": random}
        return {self.suc.name: pred_dict, self.suc_2.name: "X", self.suc_3.name: "y",
                self.suc_4.name: "(X.shape[1], X.shape[2])", self.suc_5.name: "y.shape[1]"}

    def to_code(self) -> str:
        num_repr_code = "# creating dict for transforming chars into numerical representation\n" \
                        f"unique_words = sorted(list(set(nltk.word_tokenize({self.text}))))\n" \
                        "word_to_int = dict((c, i) for i, c in enumerate(unique_words))\n" \
                        "int_to_word = dict((i, c) for i, c in enumerate(unique_words))\n\n"

        code = f"# dividing text into sequences of {self.seq_length} words\n"\
               "dataX = []\n"\
               "dataY = []\n"\
               f"words = nltk.word_tokenize({self.text})\n"\
               f"for i in range(0, len(words) - {self.seq_length}):\n"\
               f"\tseq_in = words[i:i + {self.seq_length}]\n"\
               f"\tseq_out = words[i + {self.seq_length}]\n"\
               f"\tdataX.append([word_to_int[word] for word in seq_in])\n"\
               f"\tdataY.append(word_to_int[seq_out])\n\n"

        reshape = "# reshaping and normalizing data\n" \
                  f"{self.values_for_successors[self.suc_2.name]} = numpy.reshape(dataX, (len(dataX), " \
                  f"{self.seq_length}, 1))\n" \
                  f"{self.values_for_successors[self.suc_2.name]} = {self.values_for_successors[self.suc_2.name]} " \
                  f"/ float(len(unique_words))\n" \
                  f"{self.values_for_successors[self.suc_3.name]} = np_utils.to_categorical(dataY)"

        return num_repr_code + code + reshape

    def get_needed_imports(self) -> list[str]:
        return ["from keras.utils import np_utils", "import numpy", "import nltk"]

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_required_arguments()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if ((isinstance(self.seq_length, str) and self.seq_length != DEFAULT) or
                isinstance(self.seq_length, int) and self.seq_length < 1):
            raise SpecificationError("seq_length", self.seq_length, DivideWordsByLength.__name__,
                                     "must be int >= 1!")

    def __check_required_arguments(self) -> None:
        if self.seq_length == DEFAULT:
            raise RequiredArgumentError("seq_length", DivideWordsByLength.__name__)

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre], DivideWordsByLength.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, BASIC_TEXT_PREPROCESSING_CONNECTIONS)

    def do_preprocessing(self) -> None:
        self.text = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.DIVIDE_WORDS_BY_LENGTH

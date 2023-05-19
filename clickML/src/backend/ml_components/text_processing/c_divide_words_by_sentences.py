from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import BASIC_TEXT_PREPROCESSING_CONNECTIONS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_divide_words_by_sentences \
        import DivideWordsBySentencesDescriptor


class DivideWordsBySentences(MLComponent):
    """
    Component that divides the text into sequences of words cutting off at end of sentences.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
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
        max_seq_length: Union[int, str]
            (optional) number of characters in each sequence

        # preprocessing
        text: str
            name of the text variable where this component should work on
    """

    def __init__(self, descriptor: DivideWordsBySentencesDescriptor) -> None:
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
        self.max_seq_length: Union[int, str] = des.max_seq_length

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
                        "word_to_int = dict((c, i) for i, c in enumerate(unique_words))\n"\
                        "int_to_word = dict((i, c) for i, c in enumerate(unique_words))\n\n"

        len_seq = "for pos, sentence in enumerate(sentences):\n"\
                  f"\tif len(sentence) > {self.max_seq_length}:\n"\
                  "\t\tdel sentences[pos]\n"\
                  f"\t\tsentences.insert(pos, sentence[:{self.max_seq_length}])\n"\
                  f"\t\tsentences.insert(pos+1, sentence[{self.max_seq_length}:])\n\n"

        code = f"# dividing text into sequences of characters respecting sentences\n"\
               "dataX = []\n"\
               "dataY = []\n\n"\
               f"sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize({self.text})]\n"\
               f"{'' if self.max_seq_length == DEFAULT else len_seq}"\
               "for sentence in sentences:\n" \
               "\tfor i in range(1, len(sentence)):\n"\
               "\t\tseq_in = sentence[:i]\n"\
               "\t\tseq_out = sentence[i]\n"\
               "\t\tdataX.append([word_to_int[word] for word in seq_in])\n"\
               "\t\tdataY.append(word_to_int[seq_out])\n"\
               "dataX = pad_sequences(dataX, value=-1).tolist()\n\n"

        reshape = "# reshaping and normalizing data\n" \
                  f"X = numpy.reshape(dataX, (len(dataX), len(dataX[0]), 1))\n" \
                  "X = X / float(len(unique_words))\n" \
                  "y = np_utils.to_categorical(dataY)"
        return num_repr_code + code + reshape

    def get_needed_imports(self) -> list[str]:
        return ["from keras.utils import np_utils", "import numpy", "import nltk",
                "from keras_preprocessing.sequence import pad_sequences"]

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if ((isinstance(self.max_seq_length, str) and self.max_seq_length != DEFAULT) or
                isinstance(self.max_seq_length, int) and self.max_seq_length < 1):
            raise SpecificationError("max_seq_length", self.max_seq_length, DivideWordsBySentences.__name__,
                                     "must be int >= 1!")

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre], DivideWordsBySentences.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, BASIC_TEXT_PREPROCESSING_CONNECTIONS)

    def do_preprocessing(self) -> None:
        self.text = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.DIVIDE_WORDS_BY_SENTENCES

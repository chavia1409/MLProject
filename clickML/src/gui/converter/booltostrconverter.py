from gui.mvvm.converterbase import ConverterBase


class BoolToStrConverter(ConverterBase):
    def __init__(self, true_str: str, false_str: str):
        self.__true_str = true_str
        self.__false_str = false_str

    def convert(self, value) -> object:
        if value:
            return self.__true_str
        return self.__false_str

    def convert_back(self, value) -> object:
        return value == self.__true_str
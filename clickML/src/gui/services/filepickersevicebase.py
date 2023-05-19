from abc import abstractmethod, ABC


class FilePickerServiceBase(ABC):

    @abstractmethod
    def pick_file_name(self) -> str:
        pass

    @abstractmethod
    def save_file_name(self):
        pass

    @abstractmethod
    def pick_folder_name(self):
        pass
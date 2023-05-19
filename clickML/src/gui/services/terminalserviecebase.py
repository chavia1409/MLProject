from abc import ABC, abstractmethod


class TerminalServiceBase(ABC):

    @abstractmethod
    def create_popup(self, title: str, text: str, size_x: int, size_y: int, add_scroll_x:bool):
        pass
    @abstractmethod
    def write_line(self, text: str):
       pass
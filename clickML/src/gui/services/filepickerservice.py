from typing import List

from gui.services.filepickersevicebase import FilePickerServiceBase
from plyer import filechooser


class FilePickerService(FilePickerServiceBase):
    def pick_file_name(self, title= 'Choose a File', path = None, filters:List = None) -> str:
        path = filechooser.open_file(title=title, path= path, filters=filters)
        if path is None:
            return None
        if len(path) == 0:
            return None
        return path[0]

    def save_file_name(self, title= 'Choose a File', path =None, filters:List = None) -> str:
        path = filechooser.save_file(title=title, path= path, filters=filters)
        if path is None:
            return None
        if len(path) == 0:
            return None
        return path[0]

    def pick_folder_name(self) -> str:
        path = filechooser.choose_dir()
        if path is None:
            return None
        if len(path) == 0:
            return None
        return path[0]

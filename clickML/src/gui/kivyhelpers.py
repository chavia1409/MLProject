import os
import os.path
from kivy.lang import Builder

def load_kv(file:str):
    """Loads the .kv file

    Parameters
    ----------
    file : str
        Name of the .py file (with .py extension) of the class that belongs to the .kv file.
        Just pass __file__ as parameter.
    """
    Builder.load_file(os.path.realpath(file).replace('.py', '.kv'))
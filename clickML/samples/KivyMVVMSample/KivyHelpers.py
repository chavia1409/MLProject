import os
import os.path
from kivy.lang import Builder

def loadKv(file:str):
    Builder.load_file(os.path.realpath(file).replace('.py', '.kv'))
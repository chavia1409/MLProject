import sys
import os

sys.path.insert(0, os.path.join(os.getcwd(), 'gui'))

from gui.clickmlapp import ClickMLApp

if __name__ == '__main__':
    ClickMLApp().run()

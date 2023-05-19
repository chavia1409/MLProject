from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):  # Constructor method
        super().__init__()  # Calling the parent class (QWidget) constructor

        self.initUI()  # Calling initUI method defined in this class

    def clickme(self):
        self.myListWidget2.clear()

    def initUI(self):
        # Scaling the window
        self.setGeometry(100, 100, 900,
                         600)  # sets the geometry of layout as setGeometry(x_initial, y_initial, width, height)

        # Create List Widgets
        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()

        # create a clear Button
        self.b1 = QPushButton("Clear")

        # add action to the button
        self.b1.clicked.connect(self.clickme)

        # Adding Items in ListWidget1
        listWidgetItem1 = QListWidgetItem("Load Data")
        listWidgetItem2 = QListWidgetItem("Pre processing")
        listWidgetItem3 = QListWidgetItem("Linear Regression")
        listWidgetItem4 = QListWidgetItem("Train Model")

        self.myListWidget1.insertItem(1, listWidgetItem1)
        self.myListWidget1.insertItem(2, listWidgetItem2)
        self.myListWidget1.insertItem(3, listWidgetItem3)
        self.myListWidget1.insertItem(4, listWidgetItem4)

        # Creating a vertical box with spacing
        self.appLayout = QVBoxLayout()
        self.appLayout.setSpacing(10)  # setSpacing(pixels) method sets spacing in specified number of pixels.

        # adding  Label, list widgets and button in Layout
        self.appLayout.addWidget(QLabel("Drag from here"))
        self.appLayout.addWidget(self.myListWidget1)
        self.appLayout.addWidget(QLabel("Drop it here"))
        self.appLayout.addWidget(self.myListWidget2)
        self.appLayout.addWidget(self.b1)

        # Setting Drag and Drop for QListWidgets
        self.myListWidget1.setAcceptDrops(False)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        # Setting Window Title and Layout
        self.setWindowTitle('Simple Drag and Drop')
        self.setLayout(self.appLayout)

        # decorate with CSS
        self.setStyleSheet(open('style.css').read())

        # Displaying the final Application 
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)  # sys.argv are Command line arguments received in Python
    window = Window()
    sys.exit(App.exec())

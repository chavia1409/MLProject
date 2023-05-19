from mvvm.Command import Command
from mvvm.ViewModelBase import ViewModelBase
from varname import nameof


class CalculatorViewModel(ViewModelBase):

    def __init__(self) -> None:
        self.clickCommand = Command(self.click)
        self.changeModeCommand = Command(self.changeMode)
        self.cancelCommand = Command(self.cancel)
        super().__init__()

    __calcResult = 0.0
    __oldResults:list = list()
    __clickCommand:Command = None
    __changeModeCommand:Command = None
    __cancelCommand:Command = None
    __mode:str = ''
    __lastNum = 0

    @property
    def calcResult(self):
        return self.__calcResult

    @calcResult.setter
    def calcResult(self, value):
        if self.__calcResult == value:
            return
        self.__calcResult = value
        self.OnPropertyChanged(nameof(self.calcResult), value)

    @property
    def oldResults(self):
        return self.__oldResults

    @oldResults.setter
    def oldResults(self, value):
        if self.__oldResults == value:
            return
        self.__oldResults = value
        self.OnPropertyChanged(nameof(self.oldResults), value)

    @property
    def clickCommand(self):
        return self.__clickCommand

    @clickCommand.setter
    def clickCommand(self, value):
        if self.__clickCommand == value:
            return
        self.__clickCommand = value
        self.OnPropertyChanged(nameof(self.clickCommand), value)

    @property
    def changeModeCommand(self):
        return self.__changeModeCommand

    @changeModeCommand.setter
    def changeModeCommand(self, value):
        if self.__changeModeCommand == value:
            return
        self.__changeModeCommand = value
        self.OnPropertyChanged(nameof(self.changeModeCommand), value)

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        if self.__mode == value:
            return
        self.__mode = value
        self.OnPropertyChanged(nameof(self.mode), value)
    
    @property
    def cancelCommand(self):
        return self.__cancelCommand

    @cancelCommand.setter
    def cancelCommand(self, value):
        if self.__cancelCommand == value:
            return
        self.__cancelCommand = value
        self.OnPropertyChanged(nameof(self.cancelCommand), value)

    def click(self, args):
        if self.mode == '':
            self.calcResult = self.calcResult * 10 + args
            return
        self.__lastNum = self.calcResult
        if self.mode == '-':
            self.calcResult = -args
        if self.mode == '+':
            self.calcResult = args
        if self.mode == '=':
            self.mode = ''
            
            return
        self.mode = ''

    def changeMode(self, args):
        self.mode = args
        self.calcResult = self.__lastNum + self.calcResult
        if args == '=':
            self.oldResults.append(self.calcResult)
            self.OnPropertyChanged(nameof(self.oldResults), self.oldResults)
        self.__lastNum = 0

    def cancel(self, args):
        if args == 'C':
            self.calcResult = 0
        if args == 'AC':
            self.calcResult = 0
            self.__lastNum = 0
            self.mode = ''
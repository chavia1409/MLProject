import os
import subprocess

from common.exceptions.click_ml_exceptions import SpecificationError, ComponentCompositionError, \
    ProjectCompositionError, RequiredArgumentError, ComponentConnectionError
from common.interfaces.ProjectSerializer import ProjectSerializer
from common.interfaces.PythonCodeGenerator import CodeGenerator
from gui.mvvm.command import Command
from gui.mvvm.viewmodelbase import ViewModelBase
from gui.services.filepickersevicebase import FilePickerServiceBase


class TerminalViewModel(ViewModelBase):

    def __init__(self, terminal_service, code_generator: CodeGenerator, file_picker: FilePickerServiceBase,
                 project_serializer: ProjectSerializer, load_project, get_project_model):
        super(TerminalViewModel, self).__init__()
        self._load_project = load_project
        self._get_project_model = get_project_model
        self.__file_picker = file_picker
        self.__project_serializer = project_serializer
        self.__cwd = None
        self.__path = None
        self.__project_name = None
        self.__code_generator = code_generator
        self.__terminal_service = terminal_service
        self.__mlcomponents = None
        self.__is_runnable: bool = False
        self.__saving_dir = None

    @property
    def run_command(self):
        return Command(self.run)

    @property
    def preview_command(self):
        return Command(self.preview)

    @property
    def translate_command(self):
        return Command(self.translate)

    @property
    def save_command(self):
        return Command(self.save)

    @property
    def load_command(self):
        return Command(self.load)

    def run(self, args):
        if not self.__is_runnable:
            self.__terminal_service.create_popup('Hey!', "can not run the file", 400, 100, False)
            return

        if self.__path or self.__project_name is not None:
            if self.__path.endswith(".cmlproj"):
                self.__saving_dir = os.path.dirname(self.__path)
                os.chdir(self.__saving_dir)
            else:
                self.__terminal_service.create_popup("Error!", "Something went wrong\nPlease try again.", 400, 200,
                                                     False)
                return
            try:

                #with open(self.__saving_dir + os.sep + 'out.cmlprojout', w) as output_file:

                process = subprocess.run(["python", self.__saving_dir + os.sep + self.__project_name+".py"], shell = True, capture_output=True, text = True)

                self.__terminal_service.add_text_with_icon(text='[color=FFFF00]'+self.__saving_dir + '[/color]',
                                                           icon="folder-home",
                                                           color=(0,1,1, 1))
                self.__terminal_service.add_text_with_icon(text='[color=D3D3D3]'+ process.stdout+'[/color]',
                                                           icon="language-python",
                                                           color=(3/255, 138/255, 1, 1))
                self.__terminal_service.write_line("\n")
                if len(process.stderr) is not 0:
                    self.__terminal_service.add_text_with_icon(text="",
                                                               icon="message-alert",
                                                               color=(240 / 255, 128 / 255, 128 / 255, 1))
                    self.__terminal_service.add_text_with_icon(text= '[color=FF6347]' + process.stderr + '[/color]',
                                                               icon="",
                                                               color=(240 / 255, 128 / 255, 128 / 255, 1))




            except Exception as e:
                self.__terminal_service.add_text_with_icon(text='[color=FF6347]' + e.__str__() + '[/color]',
                                                           icon="message-alert",
                                                           color=(240 / 255, 128 / 255, 128 / 255, 1))
                self.__is_runnable = False
                return

            #os.remove("out.cmlprojout")
        else:
            self.__terminal_service.create_popup("Error!", "The project is not saved\nPlease save the project first.",
                                                 400, 200, False)

    def preview(self, args):
        if not self.__is_runnable:
            self.__terminal_service.create_popup('Hey!', "There is no Preview", 400, 100, False)
            return

        if self.__path or self.__project_name is not None:
            if self.__path.endswith(".cmlproj"):
                py_path = self.__path.replace(".cmlproj", ".py")
            else:
                return
            try:
                with open(py_path, "r") as python_code_file:
                    self.__terminal_service.create_popup(self.__project_name, python_code_file.read(), 1000, 800, True)
            except Exception as e:
                print(e)

        else:
            self.__terminal_service.create_popup("Error!", "The project is not saved\nPlease save the project first.",
                                                 400, 200)

    def translate(self, args):
        if self.__path is not None:
            try:
                self.save(None)
                if self.__path.endswith(".cmlproj"):
                    self.__saving_dir = os.path.dirname(self.__path)
                    self.__code_generator.generate_code_file(ml_components=self.__mlcomponents,
                                                             saving_dir=self.__saving_dir,
                                                             name=self.__project_name)
                else:
                    self.__terminal_service.create_popup("Error!",
                                                         "Somthing went wrong\nPlease try again.", 400, 200,
                                                         False)
                    self.__is_runnable = False


                self.__is_runnable = True
            except ComponentCompositionError as e:
                self.__terminal_service.add_text_with_icon(text='[color=FF6347]'+e.__str__()+'[/color]',
                                                           icon="message-alert",
                                                           color=(240/255,128/255,128/255,1))

                self.__is_runnable = False
            except ProjectCompositionError as e:
                self.__terminal_service.add_text_with_icon(text='[color=FF6347]' + e.__str__() + '[/color]',
                                                           icon="message-alert",
                                                           color=(240 / 255, 128 / 255, 128 / 255, 1))

                self.__is_runnable = False
            except RequiredArgumentError as e:
                self.__terminal_service.add_text_with_icon(text='[color=FF6347]' + e.__str__() + '[/color]',
                                                           icon="message-alert",
                                                           color=(240 / 255, 128 / 255, 128 / 255, 1))

                self.__is_runnable = False
            except ComponentConnectionError as e:
                self.__terminal_service.add_text_with_icon(text='[color=FF6347]' + e.__str__() + '[/color]',
                                                           icon="message-alert",
                                                           color=(240 / 255, 128 / 255, 128 / 255, 1))

                self.__is_runnable = False
            except Exception as e:
                self.__terminal_service.add_text_with_icon(text='[color=FF6347]' + e.__str__() + '[/color]',
                                                           icon="message-alert",
                                                           color=(240 / 255, 128 / 255, 128 / 255, 1))
                self.__is_runnable = False

            if self.__is_runnable:
                self.__terminal_service.add_text_with_icon(text="Successfully translated",
                                                           icon="head-check-outline", color=(0,1,0,1))

    def load(self, args):
        try:
            path = self.__file_picker.pick_file_name(title='Choose Project', path=self.__cwd, filters=['*.cmlproj'])
            if path is None:
                return

            self.__path = path
            project_model = self.__project_serializer.load_project(path)

            #get the project's name
            path_arr = os.path.split(self.__path)
            self.__project_name: str = path_arr[len(path_arr) - 1]
            self.__project_name = self.__project_name.replace(".cmlproj", "")
            project_model.name = self.__project_name
            self._load_project(project_model)

            #set the components
            self.__mlcomponents = project_model.components

        except Exception as e:
            self.__terminal_service.add_text_with_icon(text='[color=FF6347]' + e.__str__() + '[/color]',
                                                       icon="message-alert",
                                                       color=(240 / 255, 128 / 255, 128 / 255, 1))
            return

        #activate the buttons
        self.__terminal_service.enable_run()
        self.__terminal_service.enable_translate()
        self.__terminal_service.enable_preview()

    def save(self, args):
        try:
            project_model = self._get_project_model()
            #if the project is already saved
            if self.__path is not None and os.path.exists(self.__path):
                project_model.name = self.__project_name
                self.__mlcomponents = project_model.components
                self.__project_serializer.save_project(project_model, self.__path)
            else:
                path = self.__file_picker.save_file_name(path=self.__cwd, filters=['*.cmlproj'])
                if path is None:
                    return

                if path.endswith("cmlproj") == False:
                    path = path + ".cmlproj"
                self.__path = path

                #get the project's name
                path_arr = os.path.split(self.__path)
                self.__project_name:str = path_arr[len(path_arr) - 1]
                self.__project_name = self.__project_name.replace(".cmlproj", "")
                project_model.name = self.__project_name

                #set the compopnents
                self.__mlcomponents = project_model.components
                self.__project_serializer.save_project(project_model, self.__path)

        except Exception as e:
            self.__terminal_service.add_text_with_icon(text='[color=FF6347]' + e.__str__() + '[/color]',
                                                       icon="message-alert",
                                                       color=(240 / 255, 128 / 255, 128 / 255, 1))
            return

        #activate the buttons
        self.__terminal_service.enable_run()
        self.__terminal_service.enable_translate()
        self.__terminal_service.enable_preview()

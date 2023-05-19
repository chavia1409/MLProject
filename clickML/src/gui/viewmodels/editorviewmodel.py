from common.interfaces.ProjectSerializer import ProjectSerializer
from common.interfaces.PythonCodeGenerator import CodeGenerator
from common.models.ClickMLProjectModel import ClickMLProjectModel
from gui.factories.generalfactorybase import GeneralFactoryBase
from gui.mvvm.viewmodelbase import ViewModelBase
from varname import nameof

from gui.viewmodels.nodeeditorviewmodel import NodeEditorViewModel
from gui.viewmodels.terminalviewmodel import TerminalViewModel


class EditorViewModel(ViewModelBase):

    def __init__(self, general_factory: GeneralFactoryBase, project_serializer: ProjectSerializer,
                 code_generator: CodeGenerator):
        super().__init__()
        self.__project_name = 'New Project'
        self.__node_editor = None
        self.node_editor = general_factory.create(NodeEditorViewModel)
        self.__terminal = None
        self.__project_serializer = project_serializer
        self.__code_generator = code_generator
        self.terminal = general_factory.create(TerminalViewModel, get_project_model=self.create_project_model, load_project=self.load_project_model)

    @property
    def project_name(self):
        return self.__project_name

    @project_name.setter
    def project_name(self, value):
        if value == self.__project_name:
            return
        self.__project_name = value
        self._notify_property_changed('project_name', value)

    @property
    def node_editor(self):
        return self.__node_editor

    @node_editor.setter
    def node_editor(self, value):
        if value == self.__node_editor:
            return
        self.__node_editor = value
        self._notify_property_changed('node_editor', value)

    @property
    def terminal(self):
        return self.__terminal

    @terminal.setter
    def terminal(self, value):
        if value == self.__terminal:
            return
        self.__terminal = value
        self._notify_property_changed('terminal', value)


    def create_project_model(self) -> ClickMLProjectModel:
        project = ClickMLProjectModel()
        project.name = self.__project_name
        project.components = self.node_editor.generate_descriptors()
        project.designers = self.node_editor.generate_designer_descriptors()
        return project

    def load_project_model(self, project_model: ClickMLProjectModel):
        self.project_name = project_model.name
        self.node_editor.create_from_descriptors(project_model.components, project_model.designers)
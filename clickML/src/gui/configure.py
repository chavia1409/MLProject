import uuid

from backend.code_generation_components.concrete_components.code_generator \
    import CodeGenerator as CodeGeneratorComponent
from backend.code_generation_components.concrete_components.preprocessor import Preprocessor
from backend.code_generation_components.concrete_components.validator import Validator
from backend.code_generation_components.concrete_tools import code_combiner, code_styler, general_validator, \
    import_manager, linearizer, optimizer, transformer, type_categorizer, pre_data_setter, header_maker
from backend.code_generation_components.concrete_tools.image_classification_type_validator \
    import ImageClassificationTypeValidator
from backend.code_generation_components.concrete_tools.regression_type_validator import RegressionTypeValidator
from backend.code_generation_components.concrete_tools.text_generation_type_validator import TextGenerationTypeValidator
from backend.code_generator_main import CodeGeneratorMain
from backend.component_enum import Categories
from backend.project_model_serializer import ProjectModelSerializer
from common.interfaces.ProjectSerializer import ProjectSerializer
from common.interfaces.PythonCodeGenerator import CodeGenerator
from common.models.ClickMLProjectModel import ClickMLProjectModel
from common.models.component_descriptors.csv_processing.cd_csv_to_array import ReadCSVDescriptor
from common.models.component_descriptors.csv_processing.cd_save_array_csv import SaveToArrayOrCsvDescriptor
from common.models.component_descriptors.image_processing.cd_image_dataset_from_directory import ImageDatasetDescriptor
from common.models.component_descriptors.neural_networks.cd_sequential_model import SequentialModelDescriptor
from common.models.component_descriptors.neural_networks.cd_train_sequential import TrainSequentialDescriptor
from common.models.component_descriptors.text_processing.cd_delete_sequences import DeleteSequencesDescriptor
from common.models.component_descriptors.text_processing.cd_divide_chars_by_length import DivideCharsByLengthDescriptor
from common.models.component_descriptors.text_processing.cd_divide_chars_by_sentences import \
    DivideCharsBySentencesDescriptor
from common.models.component_descriptors.text_processing.cd_divide_words_by_length import DivideWordsByLengthDescriptor
from common.models.component_descriptors.text_processing.cd_divide_words_by_sentences import \
    DivideWordsBySentencesDescriptor
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.text_processing.cd_generate_words import GenerateWordsDescriptor
from common.models.component_descriptors.text_processing.cd_letter_case import LetterCaseDescriptor
from common.models.component_descriptors.text_processing.cd_replace_sequences import ReplaceSequencesDescriptor
from common.models.component_descriptors.text_processing.cd_print_text import PrintTextDescriptor
from common.models.component_descriptors.text_processing.cd_save_text import SaveTextDescriptor
from common.models.component_descriptors.text_processing.cd_text_console_input import TextConsoleInputDescriptor
from common.models.component_descriptors.text_processing.cd_text_reader import TextReaderDescriptor
from common.models.component_descriptors.regression.rd_predict_lin_log import PredictDescriptor
from common.models.component_descriptors.regression.rd_score_lin_log import scoreDescriptor
#from common.models.component_descriptors.regression.rd_train_multiple_linear_model import TrainMultipleLinearRegressionDescriptor
#from common.models.component_descriptors.regression.rd_train_multivariate_linear_model import TrainMultivariateLinearRegressionDescriptor
#from common.models.component_descriptors.regression.rd_adapter import adapterDescriptor
from common.models.component_descriptors.regression.rd_decision_function_log import DecisionFunctionDescriptor
from common.models.component_descriptors.regression.rd_densify_log import DensifyDescriptor
from common.models.component_descriptors.regression.rd_get_params_log import GetParamsDescriptor
from common.models.component_descriptors.regression.rd_plot_ling_log import plotDescriptor
from common.models.component_descriptors.regression.rd_save_logfile import SaveLogfileDescriptor
from common.models.component_descriptors.regression.rd_sparsify_log import SparsifyDescriptor
from common.models.component_descriptors.regression.rd_train_fit_lin import Train_Fit_Lin_Descriptor
from common.models.component_descriptors.regression.rd_train_fit_log import Train_Fit_Log_Descriptor
from common.models.component_descriptors.regression.rd_set_params_log import SetParamsDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.mlcomponentdesignerdescriptor import MLComponentDesignerDescriptor
from gui.factories.connectiondotnodeviewmodelfactory import InputDotViewModelFactory, OutputDotViewModelFactory
from gui.factories.generalfactory import GeneralFactory
from gui.factories.mlcomponentnodeviewmodelfactory import MLComponentNodeViewModelFactory
from gui.factories.nodebodyfactory import NodeBodyFactory
from gui.services.componentlistservice import ComponentListService
from gui.services.filepickerservice import FilePickerService
from gui.services.nodelinkerservice import NodeLinkerService
from gui.services.nodemanager import NodeManager
from gui.services.terminalservice import TerminalService
from gui.viewmodels.editorviewmodel import EditorViewModel
from gui.viewmodels.nodeeditorviewmodel import NodeEditorViewModel
from gui.viewmodels.nodeviewmodels.csvprocessing.csvtoarraynodeviewmodel import CsvToArrayNodeViewModel
from gui.viewmodels.nodeviewmodels.csvprocessing.savetoarrayorcsvnodeviewmodel import SaveToArrayOrCsvNodeViewModel
from gui.viewmodels.nodeviewmodels.imageprocessing.imagedatasetnodeviewmodel import ImageDatasetNodeViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.sequentialmodelnodeviewmodel import SequentialModelNodeViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.trainsequentialnodeviewmodel import TrainSequentialNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.deletesequencesnodeviewmodel import DeleteSequencesNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.dividecharsbylengthnodeviewmodel import DivideCharsByLengthNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.dividecharsbysentencesnodeviewmodel import \
    DivideCharsBySentencesNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.dividewordsbylengthnodeviewmodel import DivideWordsByLengthNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.dividewordsbysentencesnodeviewmodel import \
    DivideWordsBySentencesNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.generatecharsnodeviewmodel import GenerateCharsNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.generatewordsnodeviewmodel import GenerateWordsNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.lettercasenodeviewmodel import LetterCaseViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.printtextnodeviewmodel import PrintTextNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.replacesequencesnodeviewmodel import ReplaceSequencesNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.savetextnodeviewmodel import SaveTextNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.textconsoleinputnodeviewmodel import TextConsoleInputNodeViewModel
from gui.viewmodels.nodeviewmodels.textprocessing.textreadernodeviewmodel import TextReaderNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.predictnodeviewmodel import PredictNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.scorenodeviewmodel import ScoreNodeViewModel
#from gui.viewmodels.nodeviewmodels.regression.trainmultiplelinearregressionnodeviewmodel import TrainMultipleLinearRegressionNodeViewModel
#from gui.viewmodels.nodeviewmodels.regression.trainmultivariatelinearregressionnodeviewmodel import TrainMultivariateLinearRegressionNodeViewModel
#from gui.viewmodels.nodeviewmodels.regression.adapternodeviewmodel import AdapterNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.decisionfunctionnodeviewmodel import DecisionFunctionNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.densifynodeviewmodel import DensifyNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.getparamsnodeviewmodel import GetParamsNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.plotnodeviewmodel import PlotNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.savelogfilenodeviewmodel import SaveLogfileNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.sparsifynodeviewmodel import SparsifyNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.trainfitlinnodeviewmodel import TrainFitLinNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.trainfitlognodeviewmodel import TrainFitLogNodeViewModel
from gui.viewmodels.nodeviewmodels.regression.setparamsnodeviewmodel import SetParamsNodeViewModel
from gui.viewmodels.terminalviewmodel import TerminalViewModel
from gui.widgets.nodeeditor.nodebodies.csvprocessing.csvtoarraynodebody import CsvToArrayNodeBody
from gui.widgets.nodeeditor.nodebodies.csvprocessing.savetoarrayorcsvnodebody import SaveToArrayOrCsvNodeBody
from gui.widgets.nodeeditor.nodebodies.imageprocessing.imagedatasetnodebody import ImageDatasetNodeBody
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.sequentialmodelnodebody import SequentialModelNodeBody
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.trainsequentialnodebody import TrainSequentialNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.deletesequencesnodebody import DeleteSequencesNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.dividecharsbylengthnodebody import DivideCharsByLengthNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.dividecharsbysentencesnodebody import \
    DivideCharsBySentencesNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.dividewordsbysentencesnodebody import \
    DivideWordsBySentencesNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.dividewordsbylengthnodebody import DivideWordsByLengthNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.generatecharsnodebody import GenerateCharsNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.generatewordsnodebody import GenerateWordsNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.lettercasenodebody import LetterCaseNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.printtextnodebody import PrintTextNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.replacesequences import ReplaceSequencesNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.savetextnodebody import SaveTextNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.textconsoleinputnodebody import TextConsoleInputNodeBody
from gui.widgets.nodeeditor.nodebodies.textprocessing.textreadernodebody import TextReaderNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.predictnodebody import PredictNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.scorenodebody import ScoreNodeBody
#from gui.widgets.nodeeditor.nodebodies.regression.trainmultiplelinearregressionnodebody import TrainMultipleLinearRegressionNodeBody
#from gui.widgets.nodeeditor.nodebodies.regression.trainmultivariatelinearregressionnodebody import TrainMultivariateLinearRegressionNodeBody
#from gui.widgets.nodeeditor.nodebodies.regression.adapternodebody import AdapterNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.decisionfunctionnodebody import DecisionFunctionNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.densifynodebody import DensifyNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.getparamsnodebody import GetParamsNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.plotnodebody import PlotNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.savelogfilenodebody import SaveLogfileNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.sparsifynodebody import SparsifyNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.trainfitlinnodebody import TrainFitLinNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.trainfitlognodebody import TrainFitLogNodeBody
from gui.widgets.nodeeditor.nodebodies.regression.setparamsnodebody import SetParamsNodeBody
from gui.widgets.nodeeditor.nodecontainerwidget import NodeContainerWidget


def configure(node_editor_widget, terminal_widget, componentList):

    # constructing CodeGenerator tools
    t_code_combiner = code_combiner.CodeCombiner()
    t_code_styler = code_styler.CodeStyler()
    t_general_validator = general_validator.GeneralValidator()
    t_import_manager = import_manager.ImportManager()
    t_linearizer = linearizer.Linearizer()
    t_optimizer = optimizer.Optimizer()
    t_transformer = transformer.Transformer()
    t_categorizer = type_categorizer.TypeCategorizer()
    t_pre_data_setter = pre_data_setter.PreDataSetter()
    t_header_maker = header_maker.HeaderMaker()

    used_type_validators = {
        Categories.REGRESSION: lambda: RegressionTypeValidator(),
        Categories.IMAGE_CLASSIFICATION: lambda: ImageClassificationTypeValidator(),
        Categories.TEXT_GENERATION: lambda: TextGenerationTypeValidator()
    }

    # constructing CodeGenerator components
    c_preprocessor = Preprocessor(t_transformer, t_pre_data_setter, t_optimizer)
    c_validator = Validator(t_general_validator, t_categorizer, used_type_validators)
    c_code_generator = CodeGeneratorComponent(t_linearizer, t_header_maker, t_import_manager, t_code_combiner,
                                              t_code_styler)

    # Creation of Singleton Instances
    node_linker_service = NodeLinkerService(node_editor_widget)
    node_body_provider = NodeBodyFactory()
    mlcomponent_nodeviewmodel_factory = MLComponentNodeViewModelFactory()
    input_dot_factory = InputDotViewModelFactory(node_linker_service)
    output_dot_factory = OutputDotViewModelFactory(node_linker_service)
    general_factory = GeneralFactory()
    project_serializer = ProjectModelSerializer()
    code_generator = CodeGeneratorMain(c_preprocessor, c_validator, c_code_generator)
    node_manager = NodeManager(general_factory, node_editor_widget)
    file_picker = FilePickerService()
    terminal_service = TerminalService(terminal_widget)
    component_list_service = ComponentListService()


    # Registration of NodeBodys
    node_body_provider.register(LetterCaseDescriptor(uuid.uuid4()).component_type, lambda: LetterCaseNodeBody())
    node_body_provider.register(TextConsoleInputDescriptor(uuid.uuid4()).component_type, lambda: TextConsoleInputNodeBody())
    node_body_provider.register(SaveTextDescriptor(uuid.uuid4()).component_type, lambda: SaveTextNodeBody())
    node_body_provider.register(GenerateCharsDescriptor(uuid.uuid4()).component_type, lambda: GenerateCharsNodeBody())
    node_body_provider.register(GenerateWordsDescriptor(uuid.uuid4()).component_type, lambda: GenerateWordsNodeBody())
    node_body_provider.register(DivideWordsByLengthDescriptor(uuid.uuid4()).component_type, lambda: DivideWordsByLengthNodeBody())
    node_body_provider.register(DivideWordsBySentencesDescriptor(uuid.uuid4()).component_type, lambda: DivideWordsBySentencesNodeBody())
    node_body_provider.register(PrintTextDescriptor(uuid.uuid4()).component_type, lambda: PrintTextNodeBody() )
    node_body_provider.register(ReplaceSequencesDescriptor(uuid.uuid4()).component_type, lambda: ReplaceSequencesNodeBody())
    node_body_provider.register(TextReaderDescriptor(uuid.uuid4()).component_type, lambda: TextReaderNodeBody())
    node_body_provider.register(PredictDescriptor(uuid.uuid4()).component_type, lambda: PredictNodeBody())
    node_body_provider.register(scoreDescriptor(uuid.uuid4()).component_type, lambda: ScoreNodeBody())
    #node_body_provider.register(TrainMultipleLinearRegressionDescriptor(uuid.uuid4()).component_type, lambda: TrainMultipleLinearRegressionNodeBody())
    #node_body_provider.register(TrainMultivariateLinearRegressionDescriptor(uuid.uuid4()).component_type, lambda: TrainMultivariateLinearRegressionNodeBody())
    #node_body_provider.register(adapterDescriptor(uuid.uuid4()).component_type, lambda: AdapterNodeBody())
    node_body_provider.register(DecisionFunctionDescriptor(uuid.uuid4()).component_type, lambda: DecisionFunctionNodeBody())
    node_body_provider.register(DensifyDescriptor(uuid.uuid4()).component_type, lambda: DensifyNodeBody())
    node_body_provider.register(GetParamsDescriptor(uuid.uuid4()).component_type, lambda: GetParamsNodeBody())
    node_body_provider.register(SaveLogfileDescriptor(uuid.uuid4()).component_type, lambda: SaveLogfileNodeBody())
    node_body_provider.register(SparsifyDescriptor(uuid.uuid4()).component_type, lambda: SparsifyNodeBody())
    node_body_provider.register(Train_Fit_Lin_Descriptor(uuid.uuid4()).component_type, lambda: TrainFitLinNodeBody())
    node_body_provider.register(Train_Fit_Log_Descriptor(uuid.uuid4()).component_type, lambda: TrainFitLogNodeBody())
    node_body_provider.register(SetParamsDescriptor(uuid.uuid4()).component_type, lambda: SetParamsNodeBody())
    node_body_provider.register(plotDescriptor(uuid.uuid4()).component_type, lambda: PlotNodeBody())
    node_body_provider.register(DeleteSequencesDescriptor(uuid.uuid4()).component_type, lambda: DeleteSequencesNodeBody())
    node_body_provider.register(SequentialModelDescriptor(uuid.uuid4()).component_type, lambda: SequentialModelNodeBody())
    node_body_provider.register(TrainSequentialDescriptor(uuid.uuid4()).component_type, lambda: TrainSequentialNodeBody())
    node_body_provider.register(ImageDatasetDescriptor(uuid.uuid4()).component_type, lambda: ImageDatasetNodeBody())
    node_body_provider.register(ReadCSVDescriptor(uuid.uuid4()).component_type, lambda: CsvToArrayNodeBody())
    node_body_provider.register(SaveToArrayOrCsvDescriptor(uuid.uuid4()).component_type, lambda: SaveToArrayOrCsvNodeBody())
    node_body_provider.register(DivideCharsByLengthDescriptor(uuid.uuid4()).component_type, lambda: DivideCharsByLengthNodeBody())
    node_body_provider.register(DivideCharsBySentencesDescriptor(uuid.uuid4()).component_type, lambda: DivideCharsBySentencesNodeBody())

    # Register MLComponentNodeViewModels
    mlcomponent_nodeviewmodel_factory.register(LetterCaseDescriptor(uuid.uuid4()).component_type,
                                               lambda: LetterCaseViewModel(LetterCaseDescriptor(uuid.uuid4()), input_dot_factory,
                                                                           output_dot_factory),
                                               lambda descriptor: LetterCaseViewModel(descriptor, input_dot_factory,
                                                                                        output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(TextConsoleInputDescriptor(uuid.uuid4()).component_type,
                                               lambda: TextConsoleInputNodeViewModel(TextConsoleInputDescriptor(uuid.uuid4()), output_dot_factory),
                                               lambda descriptor: TextConsoleInputNodeViewModel(descriptor, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(SaveTextDescriptor(uuid.uuid4()).component_type,
                                                lambda: SaveTextNodeViewModel(SaveTextDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory, file_picker),
                                                lambda descriptor: SaveTextNodeViewModel(descriptor, input_dot_factory, output_dot_factory, file_picker))
    mlcomponent_nodeviewmodel_factory.register(GenerateCharsDescriptor(uuid.uuid4()).component_type,
                                               lambda: GenerateCharsNodeViewModel(GenerateCharsDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: GenerateCharsNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(GenerateWordsDescriptor(uuid.uuid4()).component_type,
                                               lambda: GenerateWordsNodeViewModel(GenerateWordsDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: GenerateWordsNodeViewModel(descriptor, input_dot_factory,  output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(DivideWordsByLengthDescriptor(uuid.uuid4()).component_type,
                                                lambda: DivideWordsByLengthNodeViewModel(DivideWordsByLengthDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                                lambda descriptor: DivideWordsByLengthNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(DivideWordsBySentencesDescriptor(uuid.uuid4()).component_type,
                                                lambda: DivideWordsBySentencesNodeViewModel(DivideWordsBySentencesDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                                lambda descriptor: DivideWordsBySentencesNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(PrintTextDescriptor(uuid.uuid4()).component_type,
                                               lambda: PrintTextNodeViewModel(PrintTextDescriptor(uuid.uuid4()), input_dot_factory,output_dot_factory),
                                               lambda descriptor: PrintTextNodeViewModel(descriptor,input_dot_factory,output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(ReplaceSequencesDescriptor(uuid.uuid4()).component_type,
                                               lambda: ReplaceSequencesNodeViewModel(ReplaceSequencesDescriptor(uuid.uuid4()), input_dot_factory,output_dot_factory),
                                               lambda descriptor: ReplaceSequencesNodeViewModel(descriptor,input_dot_factory,output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(TextReaderDescriptor(uuid.uuid4()).component_type,
                                               lambda: TextReaderNodeViewModel(TextReaderDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory,file_picker),
                                               lambda descriptor: TextReaderNodeViewModel(descriptor, input_dot_factory, output_dot_factory,file_picker))
    mlcomponent_nodeviewmodel_factory.register(PredictDescriptor(uuid.uuid4()).component_type,
                                               lambda: PredictNodeViewModel(PredictDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: PredictNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(scoreDescriptor(uuid.uuid4()).component_type,
                                               lambda: ScoreNodeViewModel(scoreDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: ScoreNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    #mlcomponent_nodeviewmodel_factory.register(TrainMultipleLinearRegressionDescriptor(uuid.uuid4()).component_type,
    #                                           lambda: TrainMultipleLinearRegressionNodeBody(TrainMultipleLinearRegressionDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
    #                                           lambda descriptor: TrainMultipleLinearRegressionNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    #mlcomponent_nodeviewmodel_factory.register(TrainMultivariateLinearRegressionDescriptor(uuid.uuid4()).component_type,
    #                                           lambda: TrainMultivariateLinearRegressionNodeViewModel(TrainMultivariateLinearRegressionDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
    #                                           lambda descriptor: TrainMultivariateLinearRegressionNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    #mlcomponent_nodeviewmodel_factory.register(adapterDescriptor(uuid.uuid4()).component_type,
    #                                           lambda: AdapterNodeViewModel(adapterDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
    #                                           lambda descriptor: AdapterNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(DecisionFunctionDescriptor(uuid.uuid4()).component_type,
                                               lambda: DecisionFunctionNodeViewModel(DecisionFunctionDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: DecisionFunctionNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(DensifyDescriptor(uuid.uuid4()).component_type,
                                               lambda: DensifyNodeViewModel(DensifyDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: DensifyNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(GetParamsDescriptor(uuid.uuid4()).component_type,
                                               lambda: GetParamsNodeViewModel(GetParamsDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: GetParamsNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(plotDescriptor(uuid.uuid4()).component_type,
                                               lambda: PlotNodeViewModel(plotDescriptor(uuid.uuid4()), input_dot_factory),
                                               lambda descriptor: PlotNodeViewModel(descriptor, input_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(SaveLogfileDescriptor(uuid.uuid4()).component_type,
                                               lambda: SaveLogfileNodeViewModel(SaveLogfileDescriptor(uuid.uuid4()), input_dot_factory, file_picker),
                                               lambda descriptor: SaveLogfileNodeViewModel(descriptor, input_dot_factory, file_picker))
    mlcomponent_nodeviewmodel_factory.register(SparsifyDescriptor(uuid.uuid4()).component_type,
                                               lambda: SparsifyNodeViewModel(SparsifyDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: SparsifyNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(Train_Fit_Lin_Descriptor(uuid.uuid4()).component_type,
                                               lambda: TrainFitLinNodeViewModel(Train_Fit_Lin_Descriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: TrainFitLinNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(Train_Fit_Log_Descriptor(uuid.uuid4()).component_type,
                                               lambda: TrainFitLogNodeViewModel(Train_Fit_Log_Descriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: TrainFitLogNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(SetParamsDescriptor(uuid.uuid4()).component_type,
                                               lambda: SetParamsNodeViewModel(SetParamsDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory),
                                               lambda descriptor: SetParamsNodeViewModel(descriptor, input_dot_factory, output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(DeleteSequencesDescriptor(uuid.uuid4()).component_type,
                                               lambda: DeleteSequencesNodeViewModel(DeleteSequencesDescriptor(uuid.uuid4()),input_dot_factory, output_dot_factory),
                                               lambda descriptor: DeleteSequencesNodeViewModel(descriptor, input_dot_factory,output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(SequentialModelDescriptor(uuid.uuid4()).component_type,
                                               lambda: SequentialModelNodeViewModel(SequentialModelDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory, file_picker),
                                               lambda descriptor: SequentialModelNodeViewModel(descriptor, input_dot_factory, output_dot_factory, file_picker))
    mlcomponent_nodeviewmodel_factory.register(TrainSequentialDescriptor(uuid.uuid4()).component_type,
                                               lambda: TrainSequentialNodeViewModel(TrainSequentialDescriptor(uuid.uuid4()),input_dot_factory, output_dot_factory),
                                               lambda descriptor: TrainSequentialNodeViewModel(descriptor, input_dot_factory, output_dot_factory), )
    mlcomponent_nodeviewmodel_factory.register(ImageDatasetDescriptor(uuid.uuid4()).component_type,
                                               lambda: ImageDatasetNodeViewModel(ImageDatasetDescriptor(uuid.uuid4()), input_dot_factory, output_dot_factory, file_picker),
                                               lambda descriptor: ImageDatasetNodeViewModel(descriptor, input_dot_factory, output_dot_factory, file_picker))
    mlcomponent_nodeviewmodel_factory.register(ReadCSVDescriptor(uuid.uuid4()).component_type,
                                               lambda: CsvToArrayNodeViewModel(ReadCSVDescriptor(uuid.uuid4()),output_dot_factory,file_picker),
                                               lambda descriptor: CsvToArrayNodeViewModel(descriptor,output_dot_factory,file_picker))

    mlcomponent_nodeviewmodel_factory.register(SaveToArrayOrCsvDescriptor(uuid.uuid4()).component_type,
                                               lambda: SaveToArrayOrCsvNodeViewModel(SaveToArrayOrCsvDescriptor(uuid.uuid4()),input_dot_factory,output_dot_factory, file_picker),
                                               lambda descriptor: SaveToArrayOrCsvNodeViewModel(descriptor,input_dot_factory,output_dot_factory,file_picker))
    mlcomponent_nodeviewmodel_factory.register(DivideCharsByLengthDescriptor(uuid.uuid4()).component_type,
                                               lambda: DivideCharsByLengthNodeViewModel(
                                                   DivideCharsByLengthDescriptor(uuid.uuid4()), input_dot_factory,
                                                   output_dot_factory),
                                               lambda descriptor: DivideCharsByLengthNodeViewModel(descriptor,
                                                                                                   input_dot_factory,
                                                                                                   output_dot_factory))
    mlcomponent_nodeviewmodel_factory.register(DivideCharsBySentencesDescriptor(uuid.uuid4()).component_type,
                                               lambda: DivideCharsBySentencesNodeViewModel(
                                                   DivideCharsBySentencesDescriptor(uuid.uuid4()), input_dot_factory,
                                                   output_dot_factory),
                                               lambda descriptor: DivideCharsBySentencesNodeViewModel(descriptor,
                                                                                                      input_dot_factory,
                                                                                                      output_dot_factory))

    # Register some others to the GeneralFactoy
    general_factory.register(EditorViewModel, lambda kwargs: EditorViewModel(general_factory, project_serializer, code_generator))
    general_factory.register(NodeEditorViewModel, lambda kwargs: NodeEditorViewModel(mlcomponent_nodeviewmodel_factory, node_manager, node_linker_service))
    general_factory.register(NodeContainerWidget, lambda kwargs: NodeContainerWidget(node_body_provider))
    general_factory.register(TerminalViewModel, lambda kwargs: TerminalViewModel(terminal_service, code_generator, file_picker, project_serializer, kwargs['load_project'], kwargs['get_project_model']))

    # add ML Component to ComponentList pls order alphabetical
    text_processing_category = 'Text Processing'
    component_list_service.set('Console Input', TextConsoleInputDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Delete Sequences', DeleteSequencesDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Divide Chars By Length', DivideCharsByLengthDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Divide Chars By Sentences', DivideCharsBySentencesDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Divide Words By Length', DivideWordsByLengthDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Divide Words By Sentences', DivideWordsBySentencesDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Generate Chars', GenerateCharsDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Generate Words', GenerateWordsDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Letter Case', LetterCaseDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Print Text', PrintTextDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Replace Sequences', ReplaceSequencesDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Save Text', SaveTextDescriptor(uuid.uuid4()).component_type, text_processing_category)
    component_list_service.set('Text Reader', TextReaderDescriptor(uuid.uuid4()).component_type,text_processing_category)




    regression_category = 'Regression'
    #component_list_service.set('Adapter', adapterDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Decision Function', DecisionFunctionDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Densify', DensifyDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Get Params', GetParamsDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Plot', plotDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Prediction', PredictDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Save Logfile', SaveLogfileDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('ScoreLinLog', scoreDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Set Params', SetParamsDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Sparsify', SparsifyDescriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Training Fit Lin', Train_Fit_Lin_Descriptor(uuid.uuid4()).component_type, regression_category)
    component_list_service.set('Training Fit Log', Train_Fit_Log_Descriptor(uuid.uuid4()).component_type, regression_category)
    #component_list_service.set('TrainLinearModel', scoreDescriptor(uuid.uuid4()).component_type, regression_category)
    #component_list_service.set('TrainLogisticModel', scoreDescriptor(uuid.uuid4()).component_type, regression_category)

    neural_network_category = 'Neural Network'
    component_list_service.set('Sequential Model', SequentialModelDescriptor(uuid.uuid4()).component_type, neural_network_category)
    component_list_service.set('Train Sequential Model', TrainSequentialDescriptor(uuid.uuid4()).component_type, neural_network_category)

    image_processing_category = 'Image Processing'
    component_list_service.set('Image Dataset', ImageDatasetDescriptor(uuid.uuid4()).component_type, image_processing_category)

    csv_processing_category = 'CSV Processing'
    component_list_service.set('CSV To Array', ReadCSVDescriptor(uuid.uuid4()).component_type,csv_processing_category)
    component_list_service.set('Save To Array Or CSV', SaveToArrayOrCsvDescriptor(uuid.uuid4()).component_type,csv_processing_category)

    componentList.buildTreeView(component_list_service)
    return general_factory.create(EditorViewModel)


class DummyProjectSerializer(ProjectSerializer):

    def save_project(self, project_model: ClickMLProjectModel, file_path: str)  ->None:
        pass

    def load_project(self, file_path: str) -> ClickMLProjectModel:
        #Creating a mocked Project
        projectModel = ClickMLProjectModel()
        projectModel.name = 'Dummy Project'

        letterCase = LetterCaseDescriptor(uuid.uuid4())
        letterCaseDesigner = MLComponentDesignerDescriptor(letterCase.component_id, 200, 300)
        projectModel.components.append(letterCase)
        projectModel.designers.append(letterCaseDesigner)

        textConsoleInput = TextConsoleInputDescriptor(uuid.uuid4())
        textConsoleInputDesigner = MLComponentDesignerDescriptor(textConsoleInput.component_id, 0, 0)
        projectModel.components.append(textConsoleInput)
        projectModel.designers.append(textConsoleInputDesigner)

        textConsoleInput.suc.id_next = letterCase.component_id
        textConsoleInput.suc.name_next = letterCase.pre.name

        letterCase.pre.id_prev = textConsoleInput.component_id
        letterCase.pre.name_prev = textConsoleInput.suc.name

        return projectModel


"""At the moment just for testing purposes. Will be deleted later"""

from backend.code_generation_components.concrete_components.code_generator import CodeGenerator
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

used_type_validators = {
    Categories.REGRESSION: lambda: RegressionTypeValidator(),
    Categories.IMAGE_CLASSIFICATION: lambda: ImageClassificationTypeValidator(),
    Categories.TEXT_GENERATION: lambda: TextGenerationTypeValidator()
}


def config() -> CodeGeneratorMain:

    # init code generator tools
    combiner = code_combiner.CodeCombiner()
    styler = code_styler.CodeStyler()
    gen_validator = general_validator.GeneralValidator()
    imp_manager = import_manager.ImportManager()
    lin = linearizer.Linearizer()
    opt = optimizer.Optimizer()
    trans = transformer.Transformer()
    categ = type_categorizer.TypeCategorizer()
    pre_setter = pre_data_setter.PreDataSetter()
    h_maker = header_maker.HeaderMaker()

    # init code generator components
    preprocessor = Preprocessor(trans, pre_setter, opt)
    validator = Validator(gen_validator, categ, used_type_validators)
    code_generator = CodeGenerator(lin, h_maker, imp_manager, combiner, styler)

    return CodeGeneratorMain(preprocessor, validator, code_generator)

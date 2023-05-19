from enum import Enum


class Categories(Enum):
    REGRESSION = "Regression"
    IMAGE_CLASSIFICATION = "Image classification"
    TEXT_GENERATION = "Text generation"


class Components(Enum):
    """Enum for all existing components. Add new components here"""

    # Neural Networks
    SEQUENTIAL_MODEL = "SequentialModel"
    TRAIN_SEQUENTIAL = "TrainSequential"

    # Keras layers
    DENSE = "Dense"
    DROPOUT = "Dropout"
    GRU = "Gru"
    LSTM = "LSTM"
    CENTERCROP = "CenterCrop"
    CONV2D = "conv2D"
    FLATTEN = "flatten"
    MAXPOOL2D = "MaxPool2D"
    RESCALING = " rescaling"
    RESIZING = "resizing"

    # Regression
    Read_CSV = "CSV_to_array"
    CREATE_CSV = "Create_Array_CSV"
    TRAIN_FIT_LINEAR = "Train_Fit_Linear"
    TRAIN_FIT_MULTIVARIATE_LINEAR = "Train_Fit_Multiple_Linear"
    TRAIN_FIT_MULTIPLE_LINEAR = "Train_Fit_Multivariate_Linear"
    TRAIN_FIT_LOGISTIC = "Train_Fit_Log"
    SPARSIFY = "Sparsify"
    SET_PARAMS = "SetParams"
    SCORE_LIN_LOG = "ScoreLinLog"
    PREDICT_LIN_LOG = "Predict"
    PLOT_LIN_LOG = "Plotter"
    GET_PARAMS_LOG = "GetParams"
    DENSIFY_LOG = "Densify"
    DECISION_FUNCTION_LOG = "DecisionFunction"
    ADAPTER = "Adapter"

    # Text processing
    DELETE_SEQUENCES = "DeleteSequences"
    DIVIDE_CHARS_BY_LENGTH = "DivideCharsByLength"
    DIVIDE_CHARS_BY_SENTENCES = "DivideCharsBySentences"
    DIVIDE_WORDS_BY_LENGTH = "DivideWordsByLength"
    DIVIDE_WORDS_BY_SENTENCES = "DivideWordsBySentences"
    GENERATE_CHARS = "GenerateChars"
    GENERATE_WORDS = "GenerateWords"
    LETTER_CASE = "LetterCase"
    PRINT_TEXT = "PrintText"
    REPLACE_SEQUENCES = "ReplaceSequences"
    SAVE_TEXT = "SaveText"
    TEXT_CONSOLE_INPUT = "TextConsoleInput"
    TEXT_READER = "TextReader"

    # Image Processing
    IMAGE_DATASET = "ImageDataset"

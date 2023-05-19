from backend.component_enum import Components

"""Groups of valid connections for some MLComponents"""

BASIC_TEXT_PREPROCESSING_CONNECTIONS = {
    (Components.TEXT_READER, "input_text"), (Components.TEXT_CONSOLE_INPUT, "input_text"),
    (Components.SAVE_TEXT, "text"),
    (Components.REPLACE_SEQUENCES, "text"), (Components.PRINT_TEXT, "text"), (Components.LETTER_CASE, "cased_text"),
    (Components.GENERATE_WORDS, "generated_text"), (Components.GENERATE_CHARS, "generated_text"),
    (Components.DELETE_SEQUENCES, "deleted_text")}

MODEL_PROVIDERS = {
    (Components.SEQUENTIAL_MODEL, "model"), (Components.TRAIN_SEQUENTIAL, "model")
}

CHAR_GENERATION_INPUT = {
    (Components.DIVIDE_CHARS_BY_LENGTH, "prediction_input"), (Components.DIVIDE_CHARS_BY_SENTENCES, "prediction_input")
}

WORD_GENERATION_INPUT = {
    (Components.DIVIDE_WORDS_BY_LENGTH, "prediction_input"), (Components.DIVIDE_WORDS_BY_SENTENCES, "prediction_input")
}

INPUT_SHAPE_PROVIDERS = {
    (Components.DIVIDE_CHARS_BY_LENGTH, "input_shape"), (Components.DIVIDE_CHARS_BY_SENTENCES, "input_shape"),
    (Components.DIVIDE_WORDS_BY_LENGTH, "input_shape"), (Components.DIVIDE_WORDS_BY_SENTENCES, "input_shape"),
    (Components.IMAGE_DATASET, "input_shape")
}

OUTPUT_SHAPE_PROVIDERS = {
    (Components.DIVIDE_CHARS_BY_LENGTH, "output_shape"), (Components.DIVIDE_CHARS_BY_SENTENCES, "output_shape"),
    (Components.DIVIDE_WORDS_BY_LENGTH, "output_shape"), (Components.DIVIDE_WORDS_BY_SENTENCES, "output_shape"),
    (Components.IMAGE_DATASET, "output_shape")
}

NET_INPUT_PROVIDERS = {
    (Components.DIVIDE_CHARS_BY_LENGTH, "net_input"), (Components.DIVIDE_CHARS_BY_SENTENCES, "net_input"),
    (Components.DIVIDE_WORDS_BY_LENGTH, "net_input"), (Components.DIVIDE_WORDS_BY_SENTENCES, "net_input"),
    (Components.IMAGE_DATASET, "training_data")
}

NET_OUTPUT_PROVIDERS = {
    (Components.DIVIDE_CHARS_BY_LENGTH, "net_output"), (Components.DIVIDE_CHARS_BY_SENTENCES, "net_output"),
    (Components.DIVIDE_WORDS_BY_LENGTH, "net_output"), (Components.DIVIDE_WORDS_BY_SENTENCES, "net_output"),
    (Components.IMAGE_DATASET, "validation_data")
}

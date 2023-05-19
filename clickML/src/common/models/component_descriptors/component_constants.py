"""Collection of constants that are used within components and component descriptors."""

# Default value for component parameters
DEFAULT: str = "clickMLDefault"

# Set of keras layer activations
KERAS_LAYERS_ACTIVATIONS: set[str] = {"relu", "sigmoid", "softmax", "softplus", "softsign", "tanh", "selu", "elu",
                                      "exponential"}

# Set of keras layer weight initializers
KERAS_LAYERS_INITIALIZERS: set[str] = {"random_normal", "random_uniform", "truncated_normal", "zeros", "ones",
                                       "glorot_normal", "glorot_uniform", "he_normal", "he_uniform", "identity",
                                       "orthogonal", "constant", "variance_scaling"}

# Set of keras layer weight regularizers
KERAS_LAYERS_REGULARIZERS: set[str] = {"l1", "l2", "l1_l2", "orthogonal"}

# Set of interpolation parameters
KERAS_LAYERS_POL: set[str] = {"bilinear", "nearest", "bicubic", "area", "lanczos3", "lanczos5", "gaussian",
                              "mitchellcubic"}

# Set of constraint parameters
KERAS_LAYERS_CONSTRAINTS: set[str] = {"max_norm", "min_max_norm", "non_neg", "unit_norm", "radial_constraint"}

# Set of keras optimizers
KERAS_OPTIMIZERS: set[str] = {"Adadelta", "Adagrad", "Adam", "Adamax", "Ftrl", "Nadam", "Optimizer", "RMSprop", "SGD"}

# Set of keras losses
KERAS_LOSSES: set[str] = {"binary_crossentropy", "binary_focal_crossentropy", "categorical_crossentropy",
                          "categorical_hinge", "cosine_similarity", "hinge", "huber_loss", "kl_divergence",
                          "log_cosh", "mean_absolute_error", "mean_squared_error", "mean_squared_logarithmic_error",
                          "poisson", "reduction", "sparse_categorical_crossentropy", "squared_hinge"}

# Set of keras metrics
KERAS_METRICS: set[str] = {"accuracy", "binary_accuracy", "binary_crossentropy", "categorical_accuracy",
                           "categorical_crossentropy", "categorical_hinge", "cosine_similarity", "hinge",
                           "kullback_leibler_divergence", "logcosh", "mean", "mean_absolute_error",
                           "mean_squared_error", "mean_squared_error", "mean_squared_logarithmic_error",
                           "mean_tensor", "poisson", "root_mean_squared_error", "sparse_categorical_accuracy",
                           "sparse_categorical_crossentropy", "sparse_top_k_categorical_accuracy", "squared_hinge",
                           "sum", "top_k_categorical_accuracy"}

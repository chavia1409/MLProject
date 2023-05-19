# Collaborators: Julian Klitzke \\
from __future__ import annotations


class r_methods:
    pdt_value = "pdt"

    # Methods for linear and logistic Regression:
    @staticmethod
    def fit(model: str, set_X: str, set_y: str) -> str:
        code = model + ".fit(" + set_X + ", " + set_y + ") \n"

        return code

    @staticmethod
    def predict(constraint, model, testset: str) -> str:
        code = f"{constraint} = "
        code += model + ".PredictDescriptor(" + testset + ")\n"

        return code

    @staticmethod
    def score(model, X, y) -> str:
        code = model + ".score(" + X + "," + y + ")\n"

        return code

    @staticmethod
    def get_params(model, deep: bool):
        code = model + ".get_params(deep=" + deep + ") \n"

        return code

        # Methods ONLY for Linear Regression:
        """---none---"""

    # Methods ONLY for Logistic Regression:
    @staticmethod
    def decision_function(model, X) -> str:
        code = model + ".decision_function(" + X + ") \n"

        return code

        """
        Parameter X: The data matrix for which we want to get the confidence scores.
        Return value: Confidence scores per (n_samples, n_classes) combination. In the binary case, 
        confidence ScoreLinLog for self.classes_[1] where >0 means this class would be predicted.
        """

    @staticmethod
    def densify(model) -> str:
        code = model + ".densify()"

        """Converts the coef_ member (back) to a numpy.ndarray. This is the default format of coef_ 
        and is required for fitting, so calling this method is only required on models that have previously 
        been sparsified; otherwise, it is a no-op."""

        return code

    @staticmethod
    def predict_log_proba(model, X) -> str:
        code = model + ".predict_log_proba(" + X + ") \n"

        return code

    @staticmethod
    def predict_proba(model, X) -> str:
        code = model + ".predict_proba(" + X + ") \n"

        return code

    @staticmethod
    def sparsify(model, X) -> str:
        code = model + ".sparsify() \n"

        return code

    @staticmethod
    def set_params() -> str:  # TODO
        return ""

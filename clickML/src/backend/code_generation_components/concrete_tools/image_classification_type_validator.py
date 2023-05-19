from backend.code_generation_components.abstract_tools.project_type_validator import ProjectTypeValidator
from backend.ml_components.ml_component import MLComponent
from backend.ml_components.ml_layer_component import MLLayerComponent
from backend.ml_components.image_processing.image_dataset_from_directory import ImageDataset
from common.exceptions.click_ml_exceptions import ProjectCompositionError
from backend.component_enum import Components
from common.exceptions.click_ml_exceptions import SpecificationError


class ImageClassificationTypeValidator(ProjectTypeValidator):

    def check_if_valid(self, components: list[MLComponent]) -> None:
        """
        raises exception if something specific to regression projects is wrong,
        (general validity of project is provided (means check_if_valid is already called for all components and the
        project is connected))

        Points that need to be checked:
        - are the components combined in a way that is invalid for a project of this type (just look at combinations of
            components that are not adjacent, because everything else is already checked in the MLComponents)
        - are there special constraints for the domain of some user inputs in components (e.g. the sequential model
        for text processing projects may only have special types of layers)?
        """
        self.check_loading(components)
        self.check_component_domain_constraints(components)

    @staticmethod
    def check_loading(components: list[MLComponent]) -> None:
        if not isinstance(components[0], ImageDataset):
            raise ProjectCompositionError("An Image Dataset must be loaded at the start of building an Image_NN")

    @staticmethod
    def check_component_domain_constraints(components: list[MLComponent]) -> None:
        valid_layers = {Components.CENTERCROP, Components.CONV2D, Components.DENSE, Components.DROPOUT, Components.FLATTEN, Components.MAXPOOL2D, Components.RESIZING, Components.RESCALING}
        for component in components:
            if isinstance(component, MLLayerComponent):
                if not {layer.type() for layer in component.layers}.issubset(valid_layers):
                    raise SpecificationError("layers", component.layers, component.type().value,
                                             "Sequential Image model can only contain Dense, Dropout, conv2D, Flatten and Preprocessing layers.")

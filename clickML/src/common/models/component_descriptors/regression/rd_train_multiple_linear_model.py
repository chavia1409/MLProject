import uuid
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from backend.ml_components.regression.r_train_fit_multiple_lin import Train_Fit_Multiple_Linear
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class TrainMultipleLinearRegressionDescriptor(MLComponentDescriptor):
    """
    Descriptor multiple linear regression
    
    pre: PredecessorDescriptor
        (required)
    pre2: PredecessorDescriptor2
        (required - Array containing the dataset/values for which values (e.g. prices, whatsoever) shall be predicted
        using pre/Dataset/Array [X])
    suc: SuccessorDescriptor
        (required)
        
    #Attributes
    test_size: float, default=None
    If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split.
    If None, the value is set to the complement of the train size. If train_size is also None, it will be set to 0.25.

    train_size: float, default=None
    If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split. 
    If None, the value is automatically set to the complement of the test size.

    random_state: int, default=None
    Controls the shuffling applied to the data before applying the split. Pass an int for reproducible output across multiple function calls.
       
    """

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor("Input training data [Read_CSV]")  # required
        self.pre_2 = PredecessorDescriptor("Input target values [Read_CSV]")
        self.suc = SuccessorDescriptor("Regression output")  # optional
        self.suc_2 = SuccessorDescriptor('Save to Read_CSV output')  # optional
        self.suc_3 = SuccessorDescriptor('Plot output')  # optional

        self.independentValues: list 
        self.dependentValue : list
        self.test_size: float
        self.train_size: float
        self.random: int

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Train_Fit_Multiple_Linear.__name__

    def restore_component(self) -> Train_Fit_Multiple_Linear:
        return Train_Fit_Multiple_Linear(self)
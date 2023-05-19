"""Ready for implementation - need for extension might arise later"""
import uuid
from typing import Union

from backend.ml_components.regression.r_train_fit_lin import Train_Fit_Linear
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT


class Train_Fit_Lin_Descriptor(MLComponentDescriptor):
    """
    Descriptor for standardized, precasted linear regression
    
    pre: PredecessorDescriptor
        (required)
    pre2: PredecessorDescriptor2
        (required - Array containing the dataset/values for which values (e.g. prices, whatsoever) shall be predicted
        using pre/Dataset/Array [X])
    suc: SuccessorDescriptor
        (required
        
    #Attributes
    prediction_range:
    
    test_size: Union
        (optional) - percentage of the whole dataset used for testing
    train_size: float
        (optional - % of the whole dataset to train the model with)
    random: int
        (optional - Controls shuffling of the data. No shuffling if Value = Null)
    shuffle: bool:
        (optional, default: No - Controls wether to shuffle before splitting or not)
        
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id = component_id

        self.pre = PredecessorDescriptor("Input training data [Read_CSV]")  # required
        self.pre_2 = PredecessorDescriptor("Input target values [Read_CSV]")
        self.suc = SuccessorDescriptor("Regression output")  # optional
        self.suc_2 = SuccessorDescriptor('Save to Read_CSV output')  # optional
        self.suc_3 = SuccessorDescriptor('Plot output')  # optional

        self.test_size: Union[float, None] = None
        self.train_size: Union[float, None] = None
        self.random: Union[int, None] = None
        self.shuffle: Union[bool, None] = None

        """Plot values - both optional - Choices: 'CSV_1 Input', 'CSV_2 Input', 'CSV_1_Train Values', 
        'CSV_2_Train Values', 'CSV_1_Test Values', 'CSV_2_Test Values' for both Attributes (user's choice on wether to have
        which plotted on x or y axes """
        self.X_Plot_value: str = DEFAULT
        self.Y_Plot_value: str = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Train_Fit_Linear.__name__

    def restore_component(self) -> Train_Fit_Linear:
        return Train_Fit_Linear(self)

import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.keras_layers.ld_gru import GRUDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class GRULayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__units = descriptor.units
        self.__activation = descriptor.activation
        self.__recurrent_activation = descriptor.recurrent_activation
        self.__use_bias = descriptor.use_bias
        self.__kernel_initializer = descriptor.kernel_initializer
        self.__recurrent_initializer = descriptor.recurrent_initializer
        self.__bias_initializer = descriptor.bias_initializer
        self.__kernel_regularizer = descriptor.kernel_regularizer
        self.__recurrent_regularizer = descriptor.recurrent_regularizer
        self.__bias_regularizer = descriptor.bias_regularizer
        self.__activity_regularizer = descriptor.activity_regularizer
        self.__kernel_constraint = descriptor.kernel_constraint
        self.__recurrent_constraint = descriptor.recurrent_constraint
        self.__bias_constraint = descriptor.bias_constraint
        self.__dropout = descriptor.dropout
        self.__recurrent_dropout = descriptor.recurrent_dropout

        self.__units = 0
        if self.__activation is DEFAULT:
            self.__activation = ''
        self.__recurrent_activation = ''
        self.__use_bias = 0
        self.__kernel_initializer = ''
        self.__recurrent_initializer = ''
        self.__bias_initializer = ''
        self.__kernel_regularizer = ''
        self.__recurrent_regularizer = ''
        self.__bias_regularizer = ''
        self.__activity_regularizer = ''
        self.__kernel_constraint  = ''
        self.__recurrent_constraint = ''
        self.__bias_constraint = ''
        self.__dropout = 0
        self.__recurrent_dropout = 0

    @property
    def units(self):
        return self.__units

    @property
    def activation(self):
        return self.__activation
    @property
    def recurrent_activation(self):
        return self.__recurrent_activation
    @property
    def use_bias(self):
        return self.__use_bias
    @property
    def kernel_initializer(self):
        return self.__kernel_initializer
    @property
    def recurrent_initializer(self):
        return self.__recurrent_initializer
    @property
    def bias_initializer(self):
        return self.__bias_initializer
    @property
    def kernel_regularizer(self):
        return self.__kernel_regularizer
    @property
    def recurrent_regularizer(self):
        return self.__recurrent_regularizer
    @property
    def bias_regularizer(self):
        return self.__bias_regularizer
    @property
    def activity_regularizer(self):
       return self.__activity_regularizer
    @property
    def kernel_constraint (self):
        return self.__kernel_constraint
    @property
    def recurrent_constraint(self):
        return self.__recurrent_constraint

    @property
    def bias_constraint (self):
        return self.__bias_constraint
    @property
    def dropout(self):
        return self.__dropout
    @property
    def recurrent_dropout(self):
        return self.__recurrent_dropout


    @units.setter
    def units(self, value):
        self.__units = value
        self._notify_property_changed('units', str(self.__units))

    @activation.setter
    def activation(self, value):
        self.__activation = value
        self._notify_property_changed('activation', str(self.__activation))
    @recurrent_activation.setter
    def recurrent_activation(self,value):
        self.__recurrent_activation = value
        self._notify_property_changed('recurrent_activation', str(self.__recurrent_activation))

    @use_bias.setter
    def use_bias(self, value):
        self.__use_bias = value
        self._notify_property_changed('use_bias', str(self.__use_bias))
    @kernel_initializer.setter
    def kernel_initializer(self, value):
        self.__kernel_initializer = value
        self._notify_property_changed('kernel_initializer', str(self.__kernel_initializer))
    @recurrent_initializer.setter
    def recurrent_initializer(self, value):
        self.__recurrent_initializer = value
        self._notify_property_changed('recurrent_initializer', str(self.__recurrent_initializer))
    @bias_initializer.setter
    def bias_initializer(self, value):
        self.__bias_initializer = value
        self._notify_property_changed('bias_initializer', str(self.__bias_initializer))
    @kernel_regularizer.setter
    def kernel_regularizer(self, value):
        self.__kernel_regularizer = value
        self._notify_property_changed('kernel_regularizer', str(self.__kernel_regularizer))
    @recurrent_regularizer.setter
    def recurrent_regularizer(self, value):
        self.__recurrent_regularizer = value
        self._notify_property_changed('recurrent_regularizer', str(self.__recurrent_regularizer))
    @bias_regularizer.setter
    def bias_regularizer(self, value):
        self.__bias_regularizer = value
        self._notify_property_changed('bias_regularizer', str(self.__bias_regularizer))

    @activity_regularizer.setter
    def activity_regularizer(self, value):
       self.__activity_regularizer = value
       self._notify_property_changed('activity_regularizer', str(self.__activity_regularizer))

    @kernel_constraint.setter
    def kernel_constraint (self, value):
        self.__kernel_constraint = value
        self._notify_property_changed('kernel_constraint', str(self.__kernel_constraint))

    @recurrent_constraint.setter
    def recurrent_constraint(self, value):
        self.__recurrent_constraint = value
        self._notify_property_changed('recurrent_constraint', str(self.__recurrent_constraint))

    @bias_constraint.setter
    def bias_constraint (self, value):
        self.__bias_constraint = value
        self._notify_property_changed('bias_constraint', str(self.__bias_constraint))

    @dropout.setter
    def dropout(self, value):
        self.__dropout = value
        self._notify_property_changed('dropout', str(self.__dropout))

    @recurrent_dropout.setter
    def recurrent_dropout(self, value):
        self.__recurrent_dropout = value
        self._notify_property_changed('recurrent_dropout', str(self.__recurrent_dropout))

    @property
    def name(self):
        return 'GRU'

    @property
    def layer_descriptor(self):
        descriptor = GRUDescriptor(uuid.uuid4())
        descriptor.units =self.__units
        descriptor.activation =self.__activation
        descriptor.recurrent_activation =self.__recurrent_activation
        descriptor.use_bias =self.__use_bias
        descriptor.kernel_initializer =self.__kernel_initializer
        descriptor.recurrent_initializer =self.__recurrent_initializer
        descriptor.bias_initializera =self.__bias_initializer
        descriptor.kernel_initializer =self.__kernel_regularizer
        descriptor.recurrent_regularizer =self.__recurrent_regularizer
        descriptor.bias_regularizer =self.__bias_regularizer
        descriptor.activity_regularizer =self.__activity_regularizer
        descriptor.kernel_constraint =self.__kernel_constraint
        descriptor.recurrent_constrainte =self.__recurrent_constraint
        descriptor.bias_constraint =self.__bias_constraint
        descriptor.dropout =self.__dropout
        descriptor.recurrent_dropout =self.__recurrent_dropout
        return descriptor

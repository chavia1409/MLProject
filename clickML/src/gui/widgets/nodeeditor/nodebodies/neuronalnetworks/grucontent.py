from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout

from gui.kivyhelpers import load_kv
from gui.mvvm.contextview import ContextView

load_kv(__file__)
class GRUContent(StackLayout, ContextView):

    units = NumericProperty(0)
    activation = StringProperty()
    recurrent_activation = StringProperty()
    use_bias= ObjectProperty()
    kernel_initializer = StringProperty()
    recurrent_initializer = StringProperty()
    bias_initializer= StringProperty()
    kernel_regularizer = StringProperty()
    recurrent_regularizer = StringProperty()
    bias_regularizer = StringProperty()
    activity_regularizer = StringProperty()
    kernel_constraint = StringProperty()
    recurrent_constraint = StringProperty()
    bias_constraint = StringProperty()
    dropout = NumericProperty(0)
    recurrent_dropout = NumericProperty(0)

    def set_units(self):
        try:
            float(self.ids.units_input.text)
            self.units = float(self.ids.units_input.text)
        except:
            self.scale = 0.0

    def set_activation(self):
        self.activation = self.ids.activation_intput.text
    def set_recurrent_activation(self):
        self.recurrent_activation = self.ids.recurrent_activation_intput.text

    def set_kernel_initializer(self):
        self.kernel_initializer = self.ids.kernel_initializer_intput.text

    def set_recurrent_initializer(self):
        self.recurrent_initializer = self.ids.recurrent_initializer_intput.text

    def set_bias_initializer(self):
        self.bias_initializer = self.ids.bias_initializer_intput.text


    def set_kernel_regularizer(self):
        self.kernel_regularizer = self.ids.kernel_regularizer_intput.text

    def set_recurrent_regularizer(self):
        self.recurrent_regularizer = self.ids.recurrent_regularizer_intput.text

    def set_bias_regularizer(self):
        self.bias_regularizer = self.ids.bias_regularizer_intput.text

    def set_activity_regularizer(self):
        self.activity_regularizer = self.ids.activity_regularizer.text

    def set_kernel_constraint(self):
        self.kernel_constraint = self.ids.kernel_constraint_intput.text

    def set_recurrent_constraint(self):
        self.recurrent_constraint = self.ids.recurrent_constraint_intput.text

    def set_bias_constraint(self):
        self.bias_regularizer = self.ids.bias_regularizer_intput.text

    def set_activity_constraint(self):
        self.activity_constraint = self.ids.activity_constraint.text

    def set_dropout(self):
        try:
            float(self.ids.dropout_intput.text)
            self.dropout = float(self.ids.dropout_intput.text)
        except:
            self.dropout = 0

    def set_recurrent_dropout(self):
        try:
            float(self.ids.activity_constraint.text)
            self.activity_constraint = float(self.ids.activity_constraint.text)
        except:
            self.activity_constraint =0

    def _define_bindings(self):
        self._bind_to_context('units', 'units')
        self._bind_to_context('activation', 'activation')
        self._bind_to_context('recurrent_activation', 'recurrent_activation')
        self._bind_to_context('use_bias', 'use_bias')
        self._bind_to_context('kernel_initializer', 'kernel_initializer')
        self._bind_to_context('recurrent_initializer', 'recurrent_initializer')
        self._bind_to_context('bias_initializer', 'bias_initializer')
        self._bind_to_context('kernel_regularizer', 'kernel_regularizer')
        self._bind_to_context('recurrent_regularizer', 'recurrent_regularizer')
        self._bind_to_context('bias_regularizer', 'bias_regularizer')
        self._bind_to_context('activity_regularizer', 'activity_regularizer')
        self._bind_to_context('kernel_constraint', 'kernel_constraint')
        self._bind_to_context('recurrent_constraint', 'recurrent_constraint')
        self._bind_to_context('bias_constraint', 'bias_constraint')
        self._bind_to_context('dropout', 'dropout')
        self._bind_to_context('recurrent_dropout', 'recurrent_dropout')


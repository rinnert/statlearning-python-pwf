#  Copyright (c) 2019 Kurt Rinnert <kurt.rinnert@cern.ch>
#
#  neuro.py (this file) is part of  PWFML.
#
#  PWFML is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PWFML is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with PWFML.  If not, see <https://www.gnu.org/licenses/>.
#

import torch
import torch.nn as nn
import torch.utils.data as utils_data
import torch.nn.functional as fun
import os.path
from datetime import datetime


class LabeledDataset(utils_data.Dataset):
    """
    Provide a labeled data set.

    Provide a labeled data set from event data read from a file using the
    dataprovider module.

    Clients can provide custom functions to generate input variables and truth
    labels from potentially complicated event structures.  This involves
    implementing the corresponding callables.
    """
    def __init__(self, events, var_generator, label_generator):

        self.events = events

        xs = []
        ys = []

        for event in events:
            xs.append(var_generator(event))
            ys.append(label_generator(event))

        self.xs = torch.tensor(xs)
        self.ys = torch.tensor(ys)

    def __len__(self):
        return len(self.xs)

    def __getitem__(self, item):
        return self.xs[item], self.ys[item]


class ClassifierNN(nn.Module):
    """
    Provide a neural network model for classification.

    Provide a neural network (NN) model for classification.  The NN is a
    simple, fully connected feed-forward network.  The layout of the NN is
    specified at construction time by providing a tuple.  The length of the
    tuple corresponds to the number of network layers (including input and
    output layers).  Each tuple entry specifies the number of nodes in the
    corresponding layer.  The width of the input and output layer must
    correspond to the number of input variables and classes, respectively.

    The non-linear activation function for the hidden layers is relu.  The
    output activation is linear during training and sigmoid in inference mode.
    This is necessary in torch when using nn.BCEWithLogitsLoss() as the loss
    function during training, as is recommended for multi-class classifiers.
    The default mode is inference mode (trainers are more likely to be
    experts).  Make sure you change the inference_mode attribute to False for
    training.

    The recommended optimizer is Adam.

    In case you move the classifier to an accelerator (such as a GPU) make sure
    you construct the optimizer after.  Of course, different optimizers and
    loss functions can be used; make sure the implications are understood, in
    particular for the output layer activation (see above).
    """
    def __init__(self,
                 layout=(2, 16, 16, 3),
                 activation=fun.relu):
        super().__init__()
        self.layout = layout
        self.inference_mode = True  # training clients: change this attribute to False
        self.activation = activation
        self.layers = nn.ModuleList()
        for num_nodes, num_nodes_next in zip(self.layout[:-1], self.layout[1:]):
            self.layers.append(nn.Linear(num_nodes, num_nodes_next))

    def forward(self, x):
        for layer in self.layers[:-1]:
            x = self.activation(layer(x))

        if self.inference_mode:
            x = torch.sigmoid(self.layers[-1](x))
        else:
            x = self.layers[-1](x)

        return x

    def train(self, mode=True):
        super(ClassifierNN, self).train()
        self.inference_mode = False

    def eval(self):
        super(ClassifierNN, self).eval()
        self.inference_mode = True

    def save_weights(self, tag=None, time_stamp=True, directory=None):
        weight_file_path = 'classifier_weights_'
        if tag is not None:
            weight_file_path += '{}_'.format(tag)
        for width in self.layout[:-1]:
            weight_file_path += '{}x'.format(width)
        weight_file_path += '{}'.format(self.layout[-1])
        if time_stamp:
            weight_file_path += '_{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
        weight_file_path += '.pt'
        if directory is not None:
            weight_file_path = os.path.join(directory, weight_file_path)

        torch.save(self.state_dict(), weight_file_path)

        return weight_file_path


class FCNN(nn.Module):
    """
    Provide a generic FCNN neural network model.

    The layout of the NN is specified at construction time by providing a
    tuple.  The length of the tuple corresponds to the number of network layers
    (including input and output layers).  Each tuple entry specifies the number
    of nodes in the corresponding layer.  The width of the input and output
    layer must correspond to the number of input variables and classes,
    respectively.

    The default non-linear activation function for the hidden layers is relu.  The
    output activation is specified via the out_activation keyword argument.

    In case you move the classifier to an accelerator (such as a GPU) make sure
    you construct the optimizer after.  Of course, different optimizers and
    loss functions can be used; make sure the implications are understood, in
    particular for the output layer activation (see above).
    """
    def __init__(self,
                 layout=(2, 16, 16, 3),
                 activation=fun.relu,
                 out_activation=None):
        super().__init__()
        self.layout = layout
        self.inference_mode = True  # training clients: change this attribute to False
        self.activation = activation
        self.out_activation = out_activation
        self.layers = nn.ModuleList()
        for num_nodes, num_nodes_next in zip(self.layout[:-1], self.layout[1:]):
            self.layers.append(nn.Linear(num_nodes, num_nodes_next))

    def forward(self, x):
        if self.activation is not None: 
            for layer in self.layers[:-1]:
                x = self.activation(layer(x))
        else:
            for layer in self.layers[:-1]:
                x = layer(x)

        if self.out_activation is not None:
            x = self.out_activation(layer(x))
        else:
            x = self.layers[-1](x)

        return x

    def train(self, mode=True):
        super(ClassifierNN, self).train()
        self.inference_mode = False

    def eval(self):
        super(ClassifierNN, self).eval()
        self.inference_mode = True

    def save_weights(self, tag=None, time_stamp=True, directory=None):
        weight_file_path = 'classifier_weights_'
        if tag is not None:
            weight_file_path += '{}_'.format(tag)
        for width in self.layout[:-1]:
            weight_file_path += '{}x'.format(width)
        weight_file_path += '{}'.format(self.layout[-1])
        if time_stamp:
            weight_file_path += '_{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
        weight_file_path += '.pt'
        if directory is not None:
            weight_file_path = os.path.join(directory, weight_file_path)

        torch.save(self.state_dict(), weight_file_path)

        return weight_file_path

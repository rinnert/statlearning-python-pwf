#!/usr/bin/env python3

#  Copyright (c) 2019 Kurt Rinnert <kurt.rinnert@cern.ch>
#
#  dataprovider.py (this file) is part of  LIVHEP ML Resources.
#
#  LIVHEP ML Resources is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  LIVHEP ML Resources is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with LIVHEP ML Resources.  If not, see <https://www.gnu.org/licenses/>.
#

import numpy as np
import math
import os.path


event_dtype = np.dtype([('x1', np.float32), ('x2', np.float32)])


def generate_data(data_file_path='./data.bin', force=False, num_values=840000):
    """
    Generate random event data.

    Generate random event data and write it to the specified file.  Do nothing if the file already exists.

    The event data is simply a numpy array of type np.float32 in the interval [-1, 1). The interpretation of the data
    is left to the events() function.

    :param data_file_path: The path to the output file (default './data.bin').
    :param num_values: Number of floats to generate (default 840000).
    :param force: if True, overwrite data file if it exists
    :return: True if data has been generated, False otherwise.
    """
    if not force and os.path.isfile(data_file_path):
        print("The file '{}' already exists, no data generated. Use force=True to regenerate.".format(data_file_path))
        return False

    ds = 2.0 * np.random.sample(num_values).astype(np.float32) - 1.0
    ds.tofile(data_file_path)
    print("Generated binary file '{}' with {} float32 values.".format(data_file_path, num_values))
    return True


def events(data_file_path='./data.bin', evt_max=-1, evt_skip=0):
    """
    Return an object that produces a sequence of events.

    An event is a collection of values as defined by data_provider.event_dtype.

    The sequence ends when the data file is exhausted (default) or the maximum number of events specified by evt_max
    has been produced (what ever happens earlier).
    """
    num_evt = 0
    with open(data_file_path, 'rb') as data_file:
        if evt_skip > 0:
            data_file.seek(event_dtype.itemsize * evt_skip, 1)
        while True:
            if num_evt == evt_max:
                return
            event = np.fromfile(data_file, dtype=event_dtype, count=1)
            if event.size == 0:  # EOF
                break
            yield event[0]
            num_evt += 1

    return


def event_to_values(event):
    """ Return point coordinates as flat np.array.

    Return point coordinates as flat np.array of type np.float32.

    Requirements:

        The input event can be unpacked to two numbers.

    Examples:

        >>> list(event_to_values((0.0, 0.0)))
        [0.0, 0.0]
        >>> list(event_to_values((-0.5, 0.75)))
        [-0.5, 0.75]
    """
    return np.array([*event], dtype=np.float32)


def truth_labels_unit_circle(event):
    """ Return one-hot truth vector.

    Return one-hot truth vector for three classes, assuming event is a cartesian (x1, x2) coordinate tuple:

        1. outside unit circle (soft ball, r >= 1), index 0
        2. inside unit circle, x2 <= 0, index 1
        3. inside unit circle, x2 > 0, index 2

    Where r = sqrt(x1 * x1 + x2 * x2).

    Requirements:

        The event can be unpacked to two numbers.

    Examples:

        >>> list(truth_labels_unit_circle((1.0, 0.0)))
        [1.0, 0.0, 0.0]
        >>> list(truth_labels_unit_circle((0.0, 1.0)))
        [1.0, 0.0, 0.0]
        >>> list(truth_labels_unit_circle((0.0, 0.0)))
        [0.0, 1.0, 0.0]
        >>> list(truth_labels_unit_circle((0.0, -0.8)))
        [0.0, 1.0, 0.0]
        >>> list(truth_labels_unit_circle((0.0, 0.8)))
        [0.0, 0.0, 1.0]

    """
    labels = np.zeros(3, dtype=np.float32)
    x1, x2 = event
    r = math.sqrt(x1*x1 + x2*x2)
    if r >= 1.0:
        labels[0] = 1.0
    else:
        if x2 <= 0.0:
            labels[1] = 1.0
        else:
            labels[2] = 1.0

    return labels


if __name__ == '__main__':
    import sys
    import doctest
    if len(sys.argv) > 2:  # show us some data: <data file> <num events>
        data_file_path = sys.argv[1]
        evt_max = 10
        if len(sys.argv) > 2:
            evt_max = int(sys.argv[2])
        es = events(data_file_path=data_file_path, evt_max=10)
        for e in es:
            x, y = e['x'], e['y']
            print('({}, {})'.format(x, y))
    else:  # run the doctests.
        doctest.testmod()

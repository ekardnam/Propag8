'''
 *   Propag8
 *   Copyright (C) 2019 Luca "ekardnam" Bertozzi <luca.bertozzi11@studio.unibo.it>
 *
 *   This program is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# adapter functions for numpy

import numpy as np

from .measure import Measure, StatisticalMeasure

to_string = np.vectorize(str)

def print_array(array):
    print(to_string(array))

values = np.vectorize(lambda x: x.val)
errors = np.vectorize(lambda x: x.err)
variances = np.vectorize(lambda x: x.variance)
deviations = np.vectorize(lambda x: x.get_standard_deviation())


def to_measure(k):
    return np.vectorize(lambda x: x.to_measure(k))

def unpack_value_error(data):
    data_values = values(data)
    data_errors = errors(data)
    return data_values, data_errors

def unpack_value_variance(data):
    data_values = values(data)
    data_variances = variances(data)
    return data_values, data_variances

def pack_value_error(values, errors):
    return np.array([Measure(val, err) for val, err in zip(values, errors)])

def pack_value_variance(values, variances):
    return np.array([StatisticalMeasure(val, variances) for val, variance in zip(values, variances)])

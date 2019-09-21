#    Data sets an helper functions for Introduction to Statistical Learning.
#    Copyright (C) 2019  Kurt Rinnert <kurt.rinnert@liverpool.ac.uk>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import pandas as pd
import os

print(os.path.dirname(__file__))
_datadir = 'datasets'

_auto_ds = None
def Auto():
    global _auto_ds
    if _auto_ds is None:
        _auto_ds = pd.read_csv(os.path.join(_datadir, 'Auto.csv'))
    return _auto_ds

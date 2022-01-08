#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements tools to build python package and tools.
#    Copyright (C) 2022  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This package implements tools to build python package and tools.

>>> from cleandict import *
>>> a = {"a": 0, 0: "a", (0, "a"): ("a", 0)}
>>> b = a.copy()
>>> cleandict(b, ["a"])
{'a': 0}
>>> cleandict(a, ["a"], invers=True)
{0: 'a', (0, 'a'): ('a', 0)}
>>>
"""

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This package implements tools to build python package and tools.
"""
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/PythonToolsKit"

copyright = """
PythonToolsKit  Copyright (C) 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["cleandict"]

from collections.abc import Hashable
from typing import List


def cleandict(dict_: dict, keys: List[Hashable], invers: bool = False) -> dict:

    """
    This function clean a dictionary.
    """

    if invers:
        for key in keys:
            del dict_[key]
        return dict_

    to_delete = []
    for key in dict_.keys():
        if key not in keys:
            to_delete.append(key)

    for key in to_delete:
        del dict_[key]
    return dict_

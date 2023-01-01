#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements tools to build python package and tools.
#    Copyright (C) 2020  Maurice Lambert

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

>>> my_ord_dict = OrdDict({"key1": "value1", "key2": "value2"}, {"key3": "value3"}, key4="value4")
>>> my_ord_dict["key6"] = "value6"
>>> my_ord_dict.insert(4, "key5", "value5")
>>> len(my_ord_dict)
6
>>> my_ord_dict["key1"]
'value1'
>>> my_ord_dict["key2"]
'value2'
>>> my_ord_dict["key3"]
'value3'
>>> my_ord_dict["key4"]
'value4'
>>> my_ord_dict["key5"]
'value5'
>>> my_ord_dict["key6"]
'value6'
>>> my_ord_dict.index_value(1)
'value2'
>>> my_ord_dict.index_value(2)
'value3'
>>> my_ord_dict.index_value(3)
'value4'
>>> my_ord_dict.index_value(4)
'value5'
>>> my_ord_dict.index_value(5)
'value6'
>>> my_ord_dict.to_dict()
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}
>>> my_ord_dict.move(1, "key3")
>>> my_ord_dict.index_value(1)
'value3'
>>> my_ord_dict.index_value(2)
'value2'
>>> my_ord_dict.delete("key3")
>>> my_ord_dict.index_value(1)
'value2'
>>> len(my_ord_dict)
5
>>> my_ord_dict["key2"] = "new value"
>>> my_ord_dict["key2"]
'new value'
>>> my_ord_dict.insert(0, "new key", "new value")
>>> my_ord_dict["new key"]
'new value'
>>> my_ord_dict.index_value(0)
'new value'
>>> my_ord_dict.index_value(1)
'value1'
>>> my_ord_dict.insert(1, "new key", "new value")
Traceback (most recent call last):
    ...
ValueError: Can't insert 'new key', item exists.
>>> my_ord_dict.insert(1, "new key", "new value", error=False)
>>> my_ord_dict.index_value(1)
'new value'
>>> my_ord_dict.index_value(0)
'value1'
>>> del my_ord_dict["new key"]
>>> my_ord_dict.index_key(1)
'key2'
>>> my_ord_dict.update({"update1": "update", "key2": "value2"})
>>> my_ord_dict["update1"]
'update'
>>> my_ord_dict["key2"]
'value2'
>>> my_ord_dict.index_key(1)
'key2'
>>> my_ord_dict.index_key(-1)
'update1'
>>> my_ord_dict.clear()
>>> len(my_ord_dict)
0
>>> my_ord_dict.to_dict()
{}
>>> my_ord_dict.update({"key1": "value1", "key2": "value2"})
>>> next(my_ord_dict)
('key1', 'value1')
>>> next(my_ord_dict)
('key2', 'value2')
>>> next(my_ord_dict)
Traceback (most recent call last):
    ...
StopIteration
>>> str(my_ord_dict)
"OrdDict({'key1': 'value1', 'key2': 'value2'})"
>>> print(repr(my_ord_dict))
OrdDict({'key1': 'value1', 'key2': 'value2'})
>>> my_ord_dict == {'key1': 'value1', 'key2': 'value2'}
True
>>> my_ord_dict == OrdDict({'key1': 'value1', 'key2': 'value2'})
True
>>> my_ord_dict == {'key2': 'value2', 'key1': 'value1'}
False
>>> my_ord_dict == {'key1': 'value1', 'key2': 'value3'}
False
>>> 'key1' in my_ord_dict
True
>>> 'value1' in my_ord_dict
False
>>> my_ord_dict + {'key1': 'new value', 'key3': 'value3'}
{'key1': 'new value', 'key2': 'value2', 'key3': 'value3'}
>>> my_ord_dict += {'key1': 'new value', 'key3': 'value3'}
>>> my_ord_dict
OrdDict({'key1': 'new value', 'key2': 'value2', 'key3': 'value3'})
>>> my_ord_dict != {'key1': 'new value', 'key2': 'value2', 'key3': 'value3'}
False
>>> my_ord_dict != OrdDict({'key': 'value'})
True
>>> list(reversed(my_ord_dict))
[('key3', 'value3'), ('key2', 'value2'), ('key1', 'new value')]
>>> OrdDict() | {"abc": "def"}
OrdDict({'abc': 'def'})
>>> my_ord_dict | OrdDict({'key1': 'value1', 'abc': 'def'})
OrdDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'abc': 'def'})
>>> my_ord_dict.add('new key', 'value4')
>>> my_ord_dict.add('key1', 'value1')
>>> my_ord_dict['key1']
'value1'
>>> my_ord_dict.get_key_value(0)
('key1', 'value1')
>>> my_ord_dict.get_key_value(-1)
('new key', 'value4')
>>> my_ord_dict.modify('new key', 'new value')
>>> my_ord_dict.get_key_value(-1)
('new key', 'new value')
>>> my_ord_dict.modify('not exists', None)
Traceback (most recent call last):
    ...
ValueError: Can't modify 'not exists', item doesn't exists.
>>> my_ord_dict.modify('not exists', 'value', error=False)
>>> my_ord_dict.get_key_value(-1)
('not exists', 'value')
>>> list(my_ord_dict.values())
['value1', 'value2', 'value3', 'new value', 'value']
>>> list(my_ord_dict.keys())
['key1', 'key2', 'key3', 'new key', 'not exists']
>>> my_ord_dict.popitem()
('not exists', 'value')
>>> my_ord_dict.pop('new key')
'new value'
>>> my_ord_dict.pop_index(1)
('key2', 'value2')
>>> my_ord_dict
OrdDict({'key1': 'value1', 'key3': 'value3'})
>>> list(my_ord_dict.items())
[('key1', 'value1'), ('key3', 'value3')]
>>> list(iter(my_ord_dict))
[('key1', 'value1'), ('key3', 'value3')]
>>> my_ord_dict.extend({'key1': 'new value', 'key2': 'value2'})
>>> my_ord_dict
OrdDict({'key1': 'value1', 'key3': 'value3', 'key2': 'value2'})
>>> my_ord_dict.sort()
>>> my_ord_dict
OrdDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
>>> my_ord_dict |= {'key1': 'new value', 'key4': 'value4'}
>>> my_ord_dict
OrdDict({'key1': 'new value', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'})
>>> my_ord_dict |= OrdDict({'key4': 'new value', 'key5': 'value5'})
>>> my_ord_dict
OrdDict({'key1': 'new value', 'key2': 'value2', 'key3': 'value3', 'key4': 'new value', 'key5': 'value5'})
>>> my_ord_dict.remove(0)
>>> my_ord_dict
OrdDict({'key2': 'value2', 'key3': 'value3', 'key4': 'new value', 'key5': 'value5'})
>>> my_ord_dict.get('key2')
'value2'
>>> my_ord_dict.setdefault('key2', 'new value')
'value2'
>>> my_ord_dict.setdefault('key6', 'value6')
'value6'
>>> my_ord_dict
OrdDict({'key2': 'value2', 'key3': 'value3', 'key4': 'new value', 'key5': 'value5', 'key6': 'value6'})
>>> my_ord_dict.reverse()
>>> my_ord_dict
OrdDict({'key6': 'value6', 'key5': 'value5', 'key4': 'new value', 'key3': 'value3', 'key2': 'value2'})
>>> my_ord_dict.index('key6')
0
>>> 

Tests:
~# python3 -m doctest -v OrdDict.py
97 tests in 44 items.
97 passed and 0 failed.
Test passed.
~# coverage run -m doctest OrdDict.py
~# coverage run OrdDict.py
~# coverage report
Name         Stmts   Miss  Cover
--------------------------------
OrdDict.py     172      0   100%
--------------------------------
TOTAL          172      0   100%
~# 
"""

__version__ = "1.0.0"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This package implements tools to build python package and tools.if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
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

__all__ = ["OrdDict"]

from typing import Any, Tuple, Dict, Iterable, TypeVar
from collections.abc import Hashable
from contextlib import suppress

OrdDict = TypeVar("OrdDict")


class OrdDict:

    """
    This class implements fast and powerful ordered dict.
    """

    def __init__(self, *args, **kwargs):
        dict_ = self.dict = {}
        list_ = self.list = []
        self.position = 0

        for arg in args:
            dict_.update(arg)
            list_.extend(arg.keys())

        dict_.update(kwargs)
        list_.extend(kwargs.keys())

    def __setitem__(self, item: Hashable, value: Any) -> None:
        try:
            self.dict[item]
        except KeyError:
            self.dict[item] = value
            self.list.append(item)
        self.dict[item] = value

    def __getitem__(self, item: Hashable) -> Any:
        return self.dict[item]

    def __len__(self) -> int:
        return len(self.list)

    def __str__(self) -> Dict[Hashable, Any]:
        return "OrdDict(" + str(self.to_dict()) + ")"

    def __repr__(self) -> Dict[Hashable, Any]:
        return "OrdDict(" + repr(self.to_dict()) + ")"

    def __eq__(self, other: Dict[Hashable, Any]) -> Any:
        dict_ = self.dict
        list_ = self.list

        for index, (key, value) in enumerate(other.items()):
            if list_[index] != key or dict_[key] != value:
                return False

        return True

    def __contains__(self, item: Hashable) -> bool:
        return item in self.list

    def __add__(self, dict_: Dict[Hashable, Any]) -> Dict[Hashable, Any]:
        copy = self.to_dict()
        copy.update(dict_)
        return copy

    def __delitem__(self, item: Hashable) -> None:
        del self.dict[item]
        self.list.remove(item)

    def __iadd__(self, dict_: Dict[Hashable, Any]) -> OrdDict:
        self.update(dict_)
        return self

    def __ne__(self, other: Dict[Hashable, Any]) -> bool:
        return not self == other

    def __reversed__(self) -> Iterable[Tuple[Hashable, Any]]:
        yield from ((key, self.dict[key]) for key in self.list[::-1])

    def __or__(self, dict_: OrdDict) -> OrdDict:
        copy = self.copy()
        copy.update(dict_)
        return copy

    def __ior__(self, dict_: OrdDict) -> OrdDict:
        self.update(dict_)
        return self

    #     def __ror__(self, dict_: Dict[Hashable, Any]) -> OrdDict:
    #         copy = self.copy()
    #         copy.update(dict_)
    #         return copy

    #     def __iror__(self, dict_: Dict[Hashable, Any]) -> OrdDict:
    #         self.update(dict_)
    #         return self

    def __next__(self) -> Tuple[Hashable, Any]:
        with suppress(IndexError):
            key = self.list[self.position]
            value = self.dict[key]
            self.position += 1
            return key, value

        raise StopIteration

    def __iter__(self) -> Iterable[Tuple[Hashable, Any]]:
        yield from ((key, self.dict[key]) for key in self.list)

    def to_dict(self) -> Dict[Hashable, Any]:

        """
        This method returns a dict from OrdDict instance.
        """

        return {key: self.dict[key] for key in self.list}

    def add(self, item: Hashable, value: Any) -> None:

        """
        This method adds an item to OrdDict instance.
        """

        self[item] = value

    def insert(
        self, index: int, item: Hashable, value: Any, error: bool = True
    ) -> None:

        """
        This method inserts an item in 'index' position.
        """

        try:
            self.dict[item]
        except KeyError:
            self.list.insert(index, item)
            self.dict[item] = value
        else:
            if error:
                raise ValueError(f"Can't insert {item!r}, item exists.")
            self.list.remove(item)
            self.list.insert(index, item)
            self.dict[item] = value

    def modify(self, item: Hashable, value: Any, error: bool = True) -> None:

        """
        This method updates value for an item.
        """

        try:
            self.dict[item]
        except KeyError:
            if error:
                raise ValueError(
                    f"Can't modify {item!r}, item doesn't exists."
                )
            self.list.append(item)

        self.dict[item] = value

    def move(self, index: int, item: Hashable) -> None:

        """
        This method moves an item.
        """

        self.list.remove(item)
        self.list.insert(index, item)

    def delete(self, item: Hashable) -> None:

        """
        This method deletes an item.
        """

        del self.dict[item]
        self.list.remove(item)

    def values(self) -> Iterable[Any]:

        """
        This method yields values.
        """

        yield from (self.dict[key] for key in self.list)

    def keys(self) -> Iterable[Hashable]:

        """
        This method yields keys.
        """

        yield from (key for key in self.list)

    def items(self) -> Iterable[Tuple[Hashable, Any]]:

        """
        This method yields keys and values.
        """

        yield from ((key, self.dict[key]) for key in self.list)

    def get(self, item: Hashable) -> Any:

        """
        This method returns the value from item
        """

        return self.dict[item]

    def setdefault(self, item: Hashable, value: Any) -> Any:

        """
        This method sets the value and returns it or returns the value.
        """

        try:
            value = self.dict[item]
        except KeyError:
            self.dict[item] = value
            self.list.append(item)

        return value

    def index(self, item: Hashable) -> int:

        """
        This method returns the position's key.
        """

        return self.list.index(item)

    def index_value(self, index: int) -> Any:

        """
        This method returns the value's position.
        """

        return self.dict[self.list[index]]

    def index_key(self, index: int) -> Hashable:

        """
        This method returns the item's position.
        """

        return self.list[index]

    def get_key_value(self, index: int) -> Tuple[Hashable, Any]:

        """
        This method returns item and value from index.
        """

        key = self.list[index]
        return key, self.dict[key]

    def remove(self, index: int) -> None:

        """
        This method deletes items from index.
        """

        key = self.list.pop(index)
        del self.dict[key]

    def reverse(self) -> None:

        """
        This method deletes items from index.
        """

        self.list.reverse()

    def copy(self) -> OrdDict:

        """
        This method returns an OrdDict with
        same postions, keys and values.
        """

        return OrdDict(self.to_dict())

    def update(self, dict_: Dict[Hashable, Any]) -> Any:

        """
        This method changes values or adds items
        from a dict.
        """

        for key, value in dict_.items():
            try:
                self.dict[key]
            except KeyError:
                self.list.append(key)

            self.dict[key] = value

    def clear(self) -> None:

        """
        This method clears OrdDict.
        """

        self.list.clear()
        self.dict.clear()

    def extend(self, dict_: Dict[Hashable, Any]) -> None:

        """
        This method setdefaults all keys and values from dict.
        """

        for key, value in dict_.items():
            try:
                self.dict[key]
            except KeyError:
                self.dict[key] = value
                self.list.append(key)

    def pop(self, item: Hashable) -> Any:

        """
        This method deletes and returns a value from item.
        """

        self.list.remove(item)
        return self.dict.pop(item)

    def popitem(self) -> Tuple[Hashable, Any]:

        """
        This method deletes and returns the last key and value.
        """

        key = self.list.pop()
        return key, self.dict.pop(key)

    def pop_index(self, index: int = -1) -> Tuple[Hashable, Any]:

        """
        This method deletes and returns key and value from index.
        """

        key = self.list.pop(index)
        return key, self.dict.pop(key)

    def sort(self) -> None:

        """
        This method sorts OrdDict by keys.
        """

        self.list.sort()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

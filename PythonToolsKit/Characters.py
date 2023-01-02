#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements tools to build python package and tools.
#    Copyright (C) 2021, 2023  Maurice Lambert

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

This tool shows int, hexa, binary and latin1 from int, hexa, binary or latin1.

>>> chars = Characters()
>>> chars.from_string("abc")
('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
>>> str(chars)
'TEXT: abc\\nINT: 97 98 99\\nHEXA: 61 62 63\\nBINARY: 01100001 01100010 01100011'
>>> print(chars)
TEXT: abc
INT: 97 98 99
HEXA: 61 62 63
BINARY: 01100001 01100010 01100011
>>> repr(chars)
'Characters(TEXT: abc\\nINT: 97 98 99\\nHEXA: 61 62 63\\nBINARY: 01100001 01100010 01100011)'
>>> code = main()
TEXT: Characters.py
INT: 67 104 97 114 97 99 116 101 114 115 46 112 121
HEXA: 43 68 61 72 61 63 74 65 72 73 2e 70 79
BINARY: 01000011 01101000 01100001 01110010 01100001 01100011 01110100 01100101 01110010 01110011 00101110 01110000 01111001
>>> code
0
>>> 

Tests:
~# python3 -m doctest -v Characters.py
22 tests in 11 items.
22 passed and 0 failed.
Test passed.
~# coverage run -m doctest Characters.py
~# coverage report
Name            Stmts   Miss  Cover
-----------------------------------
Characters.py      63     14    78%
-----------------------------------
TOTAL              63     14    78%
~# 
"""

__version__ = "0.1.0"
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
PythonToolsKit  Copyright (C) 2022, 2023  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

print(copyright)

__all__ = [
    "get_boolean",
    "get_numbers",
    "drange",
    "try_type",
    "is_number",
    "get_ipv4_addresses",
    "is_ip",
]

from sys import argv, stderr, exit, executable
from typing import List, Tuple
from binascii import hexlify
from base64 import b16decode


class Characters:

    """
    This class shows int, hexa, binary and latin1 from int, hexa, binary or latin1.

    >>> chars = Characters()
    >>> chars.from_string("abc")
    ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
    >>> str(chars)
    'TEXT: abc\\nINT: 97 98 99\\nHEXA: 61 62 63\\nBINARY: 01100001 01100010 01100011'
    >>> print(chars)
    TEXT: abc
    INT: 97 98 99
    HEXA: 61 62 63
    BINARY: 01100001 01100010 01100011
    >>> 
    """

    def __init__(self):
        self.hexa: str = None
        self.string: str = None
        self.bin: List[str] = None
        self.int: List[int] = None
        self.translate = str.maketrans('', '', ': -')

    def __str__(self) -> str:
        return (
            f"TEXT: {self.text}\nINT: {' '.join([str(x) for x in self.int])}"
            f"\nHEXA: {self.hexa}\nBINARY: {' '.join(self.bin)}"
        )
        
    def __repr__(self) -> str:
        return self.__class__.__name__ + "(" + self.__str__() + ")"

    def from_string(self, data: str) -> Tuple[str, List[int], str, List[str]]:

        """
        This method returns integers, hexadecimal and binary from string.

        >>> chars = Characters()
        >>> chars.from_string("abc")
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        >>> 
        """

        text = self.text = data
        integers = self.int = [ord(car) for car in data]
        hexa = self.hexa = hexlify(data.encode("latin"), " ").decode()
        binary = self.bin = [f"{integer:0>8b}" for integer in integers]

        return text, integers, hexa, binary

    def from_int(self, data: List[int]) -> Tuple[str, List[int], str, List[str]]:

        """
        This method returns string, hexadecimal and binary from integers.

        >>> chars = Characters()
        >>> chars.from_int([97, 98, 99])
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        >>> 
        """

        integers = self.int = data
        text = self.text = bytes(data).decode("latin1")
        hexa = self.hexa = hexlify(self.text.encode("latin"), " ").decode()
        binary = self.bin = [f"{integer:0>8b}" for integer in integers]

        return text, integers, hexa, binary

    def from_bytes(self, encoded: bytes) -> Tuple[str, List[int], str, List[str]]:

        """
        This method returns string, hexadecimal, integers and binary from bytes.

        >>> chars = Characters()
        >>> chars.from_bytes(b'abc')
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        """

        return self.from_int([x for x in encoded])

    def from_hexa(self, hexa: str) -> Tuple[str, List[int], str, List[str]]:

        """
        This method returns string, integers and binary from hexadecimal.
         - formats accepted: "a1 b4 ff", "A1B4FF" and "A1-b4-Ff"

        >>> chars = Characters()
        >>> chars.from_hexa('61 62 63')
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        >>> chars.from_hexa('61:62:63')
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        >>> chars.from_hexa('61-62-63')
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        >>> chars.from_hexa('616263')
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        >>> chars.from_hexa("5e 6F4f")
        ('^oO', [94, 111, 79], '5e 6f 4f', ['01011110', '01101111', '01001111'])
        >>> 
        """

        return self.from_bytes(b16decode(hexa.translate(self.translate).upper().encode()))

    def from_bin(self, binary: str) -> Tuple[str, List[int], str, List[str]]:

        """
        This method returns string, hexadecimal, and integers from binary.
         - format accepted: "1100001 1100010 1100011"

        >>> chars = Characters()
        >>> chars.from_bin('01100001 01100010 01100011')
        ('abc', [97, 98, 99], '61 62 63', ['01100001', '01100010', '01100011'])
        >>> 
        """

        return self.from_int([int(x, 2) for x in binary.split()])


def main() -> int:
    help_message = f"""USAGE: {executable} {argv[0]} [OPTION] ascii
    OPTION:
        type {{integers, string, binary, hexa}} (default: string)

    ascii - formats:
        if type is integers: "97,98,99"
        if type is string: "abc"
        if type is binary: "1100001 1100010 1100011"
        if type is hexa:
            "61 62 63", "61-62-63", "61:62:63", "616263", "fF aB:6D-6d"
    """

    if len(argv) == 2:
        string = argv[1]
        type_ = "string"
    elif len(argv) == 3:
        _, type_, string = argv
    else:
        type_ = ""

    ascii_ = Characters()
    show_help = True

    if type_ == "integers":
        show_help = False
        ascii_.from_int([int(x) for x in string.split(",")])
    elif type_ == "string":
        show_help = False
        ascii_.from_string(string)
    elif type_ == "binary":
        show_help = False
        ascii_.from_bin(string)
    elif type_ == "hexa":
        show_help = False
        ascii_.from_hexa(string)

    if show_help:
        print(help_message, file=stderr)
        return 1

    print(ascii_)
    return 0


if __name__ == "__main__":
    exit(main())

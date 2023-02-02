#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This tool analyses PDF files for Forensic Investigations
#    Copyright (C) 2022, 2023  Maurice Lambert

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
This tool helps you to debug encodings errors.

I writed this tool because i had problems with Windows
commands output launching with PowerShell on remote host using WinRM.

The remote host encodes his command output as cp437.
My PowerShell decodes the command output as cp1252.

To know what encodings are used i run this tool with this command:
~# python3 DebugEncoding.py éêâ --bad-values "‚ˆƒ"    # I see in the output the 'é' is replaced by ',', 'ê' by 'ˆ' and 'â' by 'ƒ'.
...
Encoding: 'cp437', Decoding: 'cp1252', Output: '‚ˆƒ'
...
~# 

Problem and soluce using python:
>>> from string import printable
>>> from os import popen
>>> output1 = popen("schtasks").read()
>>> output2 = output1.encode("cp1252").decode("cp437")
>>> assert "tâche" not in output1
>>> assert "tâche" in output2
>>> assert "Prêt" not in output1
>>> assert "Prêt" in output2
>>> assert "Désactivé" not in output1
>>> assert "Désactivé" in output2
>>> matchs, works = debug_encoding('éêâ', '‚ˆƒ')
>>> ("cp437", "cp1252") in [(match.encoding, match.decoding) for match in matchs]
True
>>> ("‚ˆƒ", "cp437", "cp1252") in [(work.decoded_values, work.encoding, work.decoding) for x in works.values() for work in x if work.encoding.startswith('cp') and work.decoding.startswith('cp')]
True
>>> 

Soluce using PowerShell:
PS C:\Windows> $data = [Text.Encoding]::GetEncoding(1252).GetBytes($(schtasks))
PS C:\Windows> $command_output = [Text.Encoding]::GetEncoding(437).GetString($data)

~# python3 DebugEncoding.py éêâ --bad-values "‚ˆƒ"
Encoding: 'cp858', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp858', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp858', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp858', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp858', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp858', Decoding: 'mbcs', Output: '‚ˆƒ'
Encoding: 'cp857', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp857', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp857', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp857', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp857', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp857', Decoding: 'mbcs', Output: '‚ˆƒ'
Encoding: 'cp865', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp865', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp865', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp865', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp865', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp865', Decoding: 'mbcs', Output: '‚ˆƒ'
Encoding: 'cp861', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp861', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp861', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp861', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp861', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp861', Decoding: 'mbcs', Output: '‚ˆƒ'
Encoding: 'cp850', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp850', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp850', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp850', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp850', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp850', Decoding: 'mbcs', Output: '‚ˆƒ'
Encoding: 'cp860', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp860', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp860', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp860', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp860', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp860', Decoding: 'mbcs', Output: '‚ˆƒ'
Encoding: 'cp437', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp437', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp437', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp437', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp437', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp437', Decoding: 'mbcs', Output: '‚ˆƒ'
Encoding: 'cp863', Decoding: 'cp1254', Output: '‚ˆƒ'
Encoding: 'cp863', Decoding: 'cp1258', Output: '‚ˆƒ'
Encoding: 'cp863', Decoding: 'cp1252', Output: '‚ˆƒ'
Encoding: 'cp863', Decoding: 'cp1256', Output: '‚ˆƒ'
Encoding: 'cp863', Decoding: 'cp1255', Output: '‚ˆƒ'
Encoding: 'cp863', Decoding: 'mbcs', Output: '‚ˆƒ'
~# python DebugEncoding.py éêâ --decoding cp1252 --bad-values "‚ˆƒ" --json
[
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp861"
    },
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp857"
    },
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp863"
    },
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp437"
    },
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp858"
    },
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp860"
    },
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp865"
    },
    {
        "bad_values": "\u201a\u02c6\u0192",
        "decoded_values": "\u201a\u02c6\u0192",
        "decoding": "cp1252",
        "encoding": "cp850"
    }
]
~# python3 DebugEncoding.py éêâ --encoding cp1252 --json
{
    "\u0398\u03a9\u0393": {
        "bad_values": null,
        "decoded_values": "\u0398\u03a9\u0393",
        "decoding": "cp437",
        "encoding": "cp1252"
    },
    "\u03b9\u03ba\u03b2": {
        "bad_values": null,
        "decoded_values": "\u03b9\u03ba\u03b2",
        "decoding": "iso8859_7",
        "encoding": "cp1252"
    },
    "\u00e9\u00ea\u00e2": {
        "bad_values": null,
        "decoded_values": "\u00e9\u00ea\u00e2",
        "decoding": "iso8859_15",
        "encoding": "cp1252"
    },
    "\u03bf\u03c0\u03b8": {
        "bad_values": null,
        "decoded_values": "\u03bf\u03c0\u03b8",
        "decoding": "cp869",
        "encoding": "cp1252"
    },
    "\u00c8\u00cd\u201a": {
        "bad_values": null,
        "decoded_values": "\u00c8\u00cd\u201a",
        "decoding": "mac_iceland",
        "encoding": "cp1252"
    },
    "\u0439\u043a\u0432": {
        "bad_values": null,
        "decoded_values": "\u0439\u043a\u0432",
        "decoding": "cp1251",
        "encoding": "cp1252"
    },
    "\u05d9\u05da\u05d2": {
        "bad_values": null,
        "decoded_values": "\u05d9\u05da\u05d2",
        "decoding": "cp1255",
        "encoding": "cp1252"
    },
    "\u03b9\u03be\u03b2": {
        "bad_values": null,
        "decoded_values": "\u03b9\u03be\u03b2",
        "decoding": "mac_greek",
        "encoding": "cp1252"
    },
    "\u0436\u0416\u0420": {
        "bad_values": null,
        "decoded_values": "\u0436\u0416\u0420",
        "decoding": "cp855",
        "encoding": "cp1252"
    },
    "\u00da\u0155\u00d4": {
        "bad_values": null,
        "decoded_values": "\u00da\u0155\u00d4",
        "decoding": "cp852",
        "encoding": "cp1252"
    },
    "\u00e9\u0119\u00e2": {
        "bad_values": null,
        "decoded_values": "\u00e9\u0119\u00e2",
        "decoding": "iso8859_10",
        "encoding": "cp1252"
    },
    "\ufeef\ufef3\ufed7": {
        "bad_values": null,
        "decoded_values": "\ufeef\ufef3\ufed7",
        "decoding": "cp864",
        "encoding": "cp1252"
    },
    "\u00d5\u00f5\u00e3": {
        "bad_values": null,
        "decoded_values": "\u00d5\u00f5\u00e3",
        "decoding": "hp_roman8",
        "encoding": "cp1252"
    },
    "\u00e9\u017a\u0101": {
        "bad_values": null,
        "decoded_values": "\u00e9\u017a\u0101",
        "decoding": "iso8859_13",
        "encoding": "cp1252"
    },
    "\u0137\u013b\u014c": {
        "bad_values": null,
        "decoded_values": "\u0137\u013b\u014c",
        "decoding": "cp775",
        "encoding": "cp1252"
    },
    "Z\u00b2S": {
        "bad_values": null,
        "decoded_values": "Z\u00b2S",
        "decoding": "cp273",
        "encoding": "cp1252"
    },
    "\u00da\u00db\u00d4": {
        "bad_values": null,
        "decoded_values": "\u00da\u00db\u00d4",
        "decoding": "cp857",
        "encoding": "cp1252"
    },
    "\u0418\u0419\u0411": {
        "bad_values": null,
        "decoded_values": "\u0418\u0419\u0411",
        "decoding": "koi8_r",
        "encoding": "cp1252"
    },
    "\u0449\u044a\u0442": {
        "bad_values": null,
        "decoded_values": "\u0449\u044a\u0442",
        "decoding": "cp866",
        "encoding": "cp1252"
    },
    "\u0e49\u0e4a\u0e42": {
        "bad_values": null,
        "decoded_values": "\u0e49\u0e4a\u0e42",
        "decoding": "tis_620",
        "encoding": "cp1252"
    },
    "\u0649\u064a\u0642": {
        "bad_values": null,
        "decoded_values": "\u0649\u064a\u0642",
        "decoding": "iso8859_6",
        "encoding": "cp1252"
    },
    "\u0165\u00cd\u201a": {
        "bad_values": null,
        "decoded_values": "\u0165\u00cd\u201a",
        "decoding": "mac_latin2",
        "encoding": "cp1252"
    }
}
~# python3 DebugEncoding.py éêâ --decoding cp1252
Output: '…~…€…w':
        Encoding: 'shift_jis_2004', Decoding: 'cp1252'
Output: '…~…€…w':
        Encoding: 'shift_jisx0213', Decoding: 'cp1252'
Output: 'é\x00\x00\x00ê\x00\x00\x00â\x00\x00\x00':
        Encoding: 'utf_32_le', Decoding: 'cp1252'
Output: '+AOkA6gDi-':
        Encoding: 'utf_7', Decoding: 'cp1252'
Output: 'QRB':
        Encoding: 'cp500', Decoding: 'cp1252'
Output: 'QRB':
        Encoding: 'cp1140', Decoding: 'cp1252'
Output: 'QRB':
        Encoding: 'cp273', Decoding: 'cp1252'
Output: 'QRB':
        Encoding: 'cp1026', Decoding: 'cp1252'
Output: 'QRB':
        Encoding: 'cp037', Decoding: 'cp1252'
Output: 'ÿþé\x00ê\x00â\x00':
        Encoding: 'utf_16', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'cp1254', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'latin_1', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'mbcs', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'iso8859_14', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'iso8859_9', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'iso8859_3', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'cp1258', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'cp1256', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'iso8859_16', Decoding: 'cp1252'
Output: 'éêâ':
        Encoding: 'iso8859_15', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp860', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp865', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp863', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp861', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp858', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp850', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp857', Decoding: 'cp1252'
Output: '‚ˆƒ':
        Encoding: 'cp437', Decoding: 'cp1252'
Output: '\x1b$(D+1+4+$\x1b(B':
        Encoding: 'iso2022_jp_2', Decoding: 'cp1252'
Output: '\x1b$(D+1+4+$\x1b(B':
        Encoding: 'iso2022_jp_1', Decoding: 'cp1252'
Output: '\x1b$(D+1+4+$\x1b(B':
        Encoding: 'iso2022_jp_ext', Decoding: 'cp1252'
Output: 'ÿþ\x00\x00é\x00\x00\x00ê\x00\x00\x00â\x00\x00\x00':
        Encoding: 'utf_32', Decoding: 'cp1252'
Output: 'Ã©ÃªÃ¢':
        Encoding: 'utf_8', Decoding: 'cp1252'
Output: 'é\x00ê\x00â\x00':
        Encoding: 'utf_16_le', Decoding: 'cp1252'
Output: '©ß©à©Ø':
        Encoding: 'euc_jisx0213', Decoding: 'cp1252'
Output: '©ß©à©Ø':
        Encoding: 'euc_jis_2004', Decoding: 'cp1252'
Output: '\x1b$(Q)_)`)X\x1b(B':
        Encoding: 'iso2022_jp_2004', Decoding: 'cp1252'
Output: 'ÅÁÀ':
        Encoding: 'hp_roman8', Decoding: 'cp1252'
Output: '\x00é\x00ê\x00â':
        Encoding: 'utf_16_be', Decoding: 'cp1252'
Output: '\x00\x00\x00é\x00\x00\x00ê\x00\x00\x00â':
        Encoding: 'utf_32_be', Decoding: 'cp1252'
Output: '\x1b$(O)_)`)X\x1b(B':
        Encoding: 'iso2022_jp_3', Decoding: 'cp1252'
~# 

Tests:
~# python3 -m doctest -v DebugEncoding.py
13 tests in 8 items.
13 passed and 0 failed.
Test passed.
~# 
"""

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = "This tool helps you to debug encodings errors."
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/PythonToolsKit/"

copyright = """
DebugEncoding  Copyright (C) 2023  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["debug_encoding"]

print(copyright)

from argparse import ArgumentParser, Namespace
from encodings.aliases import aliases
from typing import Dict, List, Tuple
from collections import defaultdict
from dataclasses import dataclass
from contextlib import suppress
from sys import exit, stdout
from json import dump

@dataclass
class WorkingEncoding:

    """
    This dataclass stores working encodings (encode
    and decode without raised exceptions) data. 
    """

    encoding: str
    decoding: str
    decoded_values: str
    bad_values: str

def debug_encoding(values_to_test: str, bad_values: str = None, encoding: str = None, decoding: str = None) -> Tuple[List[WorkingEncoding], Dict[str, List[WorkingEncoding]]]:

    """
    This function helps developers to debug encodings.
    """
    
    working_encodings = defaultdict(list)
    matching_encodings = []
    
    decodings = encodings = set(aliases.values())
    
    if encoding:
        encodings = (encoding,)
        
    if decoding:
        decodings = (decoding,)
    
    for encoding in encodings:
        for decoding in decodings:
            if encoding == decoding:
                continue
            with suppress(UnicodeEncodeError, LookupError, UnicodeDecodeError):
                values = values_to_test.encode(encoding).decode(decoding)
                working = WorkingEncoding(encoding, decoding, values, bad_values)
                working_encodings[values].append(working)
                if values == bad_values:
                    matching_encodings.append(working)
    
    return matching_encodings, working_encodings

def parse_args() -> Namespace:

    """
    This function parses command line arguments.
    """
    
    parser = ArgumentParser(description="This script helps you to debug encoding problems.")
    encodings = parser.add_mutually_exclusive_group()
    encodings.add_argument('--encoding', '-e', help='If you know what encoding this text is encoded with, specify it in this argument.')
    encodings.add_argument('--decoding', '-d', help='If you know what encoding this text is decoded with, specify it in this argument.')
    parser.add_argument('--bad-values', '--values', '-v', help='How tested values are printed when you have your encoding problems.')
    parser.add_argument('--json', '-j', action="store_true", help='JSON output.')
    parser.add_argument('value_to_test')
    return parser.parse_args()
    
def main() -> int:

    """
    This function executes this script from the command line.
    """
    
    arguments = parse_args()
    matching_encodings, working_encodings = debug_encoding(arguments.value_to_test, arguments.bad_values, arguments.encoding, arguments.decoding)

    if matching_encodings:
        if arguments.json:
            dump([{attr: getattr(encoding, attr) for attr in dir(encoding) if not attr.startswith("__") and not attr.endswith("__")} for encoding in matching_encodings ], stdout, indent=4)
            return 0
        print("\n".join(
            f'Encoding: {encoding.encoding!r}, '
            f'Decoding: {encoding.decoding!r}, '
            f'Output: {encoding.decoded_values!r}'
            for encoding in matching_encodings
        ))
        return 0

    if arguments.json:
        dump({k: {attr: getattr(encoding, attr) for attr in dir(encoding) if not attr.startswith("__") and not attr.endswith("__")} for k, values in working_encodings.items() for encoding in values}, stdout, indent=4)
        return 0

    print("\n".join(
        f'Output: {encoding.decoded_values!r}:\n\t'
        f'Encoding: {encoding.encoding!r}, '
        f'Decoding: {encoding.decoding!r}'
        for encodings in working_encodings.values()
        for encoding in encodings
    ))
    return 0

if __name__ == "__main__":
    exit(main())

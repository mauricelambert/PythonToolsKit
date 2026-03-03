#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements tools to build python package and tools.
#    Copyright (C) 2026  Maurice Lambert

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
This module implements a library to get an Enhanced Structure with
colored printer, dict convertion and HTML extract.
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
PythonToolsKit  Copyright (C) 2026  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["FlagMeta", "EnumMeta", "EnhancedStruct"]

from ctypes import LittleEndianStructure, Structure, c_uint16, Array, _SimpleCData, sizeof
from typing import Callable, TypeVar, Dict, Any
from binascii import hexlify
from string import printable
from sys import exit

_EnhancedStruct = TypeVar("_EnhancedStruct", (Structure, LittleEndianStructure))
printable = set(ord(c) for c in printable.strip())

def field_to_bytes(value) -> bytes:
    """
    Convert a ctypes field to bytes safely
    """

    if isinstance(value, int):
        length = (value.bit_length() + 7) // 8 or 1
        return value.to_bytes(length, "little")
    elif isinstance(value, (bytes, bytearray, Array, _SimpleCData)):
        return bytes(value)
    else:
        return str(value).encode("utf-8")

class FlagMeta:
    """
    This class implements the meta flag fields.
    """

    def __init__(self, bit: int, name: str, short_desc: str = "", long_desc: str = "", normality: float = 1.0):
        self.bit = bit
        self.name = name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.normality = normality


class EnumMeta:
    """
    This class implements the meta enum fields.
    """

    def __init__(self, value: int, name: str, short_desc: str = "", long_desc: str = "", normality: float = 1.0):
        self.value = value
        self.name = name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.normality = normality


class FieldMeta:
    """
    This class implements the meta field.
    """

    def __init__(
        self,
        short_name: str = None,
        short_desc: str = "",
        long_desc: str = "",
        verbosity: int = 1,
        flags: FlagMeta = None,
        enum: EnumMeta = None,
        calcul_normality: Callable = None,
    ):
        self.short_name = short_name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.verbosity = verbosity
        self.flags = flags or []
        self.enum = enum or []
        self.calcul_normality = calcul_normality

def EnhancedStruct(little_endian=False) -> _EnhancedStruct:
    """
    This function implements the enhenced structure build.
    """

    base = LittleEndianStructure if little_endian else Structure

    class _EnhancedStruct(base):
        """
        This class implements an Enhanced structure.
        """

        _field_metas_ = {}
        _struct_name_ = None
        _struct_desc_ = ""
        _struct_offset_ = 0

        def _get_field_meta(self, name: str) -> FieldMeta:
            """
            This method returns a resolved name field with fallback.
            """

            return self._field_metas_.get(name, FieldMeta())

        def _get_field_range(self, name: str) -> Tuple[int, int]:
            """
            This method returns the start/end offset of the field.
            """

            offset = getattr(type(self), name).offset

            field_type = None
            for fname, ftype in self._fields_:
                if fname == name:
                    field_type = ftype
                    break
            else:
                raise ValueError(f"Field {name} not found in _fields_")

            size = sizeof(field_type)
            return self._struct_offset_ + offset, self._struct_offset_ + offset + size

        def _normality_score(self, name: str, value: Any):
            """
            This method returns the normality based on the field type.
            """

            meta = self._get_field_meta(name)

            if meta.flags:
                score = 1.0
                for f in meta.flags:
                    if value & (1 << f.bit):
                        score *= f.normality
                return score

            if meta.enum:
                for e in meta.enum:
                    if e.value == value:
                        return e.normality
                return 0.0

            return (meta.calcul_normality and meta.calcul_normality(value)) or 1.0

        def to_dict(self, verbosity: int = 1) -> Dict[str, Dict[str, Any]]:
            """
            This method returns a dict to represent the
            structure with each fields and values.
            """

            result = {}
            for field, _ in self._fields_:
                meta = self._get_field_meta(field)
                if meta.verbosity > verbosity:
                    continue

                value = getattr(self, field)
                start, end = self._get_field_range(field)

                result[field] = {
                    "friendly_name": meta.short_name or field,
                    "value": value,
                    "range": (start, end),
                    "normality": self._normality_score(field, value),
                    "description": meta.short_desc,
                }

            return result

        def to_html(self, verbosity: int = 1) -> str:
            """
            This method returns a HTML string to represent the
            structure with each fields and values.
            """

            struct_name = getattr(self, "_struct_name_", self.__class__.__name__)
            html = f"""
            <h2 style="background-color:#323232;color:#aff10b;padding:4px;text-align:center;">
                {struct_name}
            </h2>
            <table border="1" style="border-collapse:collapse;width:100%;font-family:monospace;font-weight:bold;">
                <tr>
                    <th style="background:#b779e3;color:#fff;padding:2px;">Field</th>
                    <th style="background:#fff0af;color:#000;padding:2px;">Range</th>
                    <th style="background:#ffd00b;color:#000;padding:2px;">Hex Value</th>
                    <th style="background:#d4abf2;color:#000;padding:2px;">ASCII</th>
                    <th style="background:#c9f757;color:#000;padding:2px;">Field description</th>
                    <th style="background:#e0e0e0;color:#333;padding:2px;">Value description</th>
                </tr>
            """

            for field, _ in self._fields_:
                meta = self._get_field_meta(field)
                if meta.verbosity > verbosity:
                    continue

                value = getattr(self, field)
                data = field_to_bytes(value)
                hex_part = hexlify(data).decode()
                ascii_part = "".join(chr(x) if x in printable else "." for x in data)

                score = self._normality_score(field, value)

                if score < 0.5:
                    value_color = "#ff4d4d"  # red
                elif score < 0.8:
                    value_color = "#b36b00"  # orange  "#ffcc00"  # yellow
                else:
                    value_color = "#4caf50"  # green

                start, end = self._get_field_range(field)
                range_str = f"{start:08x}-{end:08x}"

                enum_value = None
                for enum in meta.enum:
                    if enum.value == value:
                        enum_value = enum

                use_flag = False
                for flag in meta.flags:
                    if (1 << flag.bit) & value:
                        use_flag = True
                        html += f"""
                        <tr>
                            <td style="background:#b779e3;color:#fff;padding:2px;">{meta.short_name or field}</td>
                            <td style="background:#fff0af;color:#000;padding:2px;">{range_str}</td>
                            <td style="background:#ffd00b;color:{value_color};padding:2px;">{hex_part}</td>
                            <td style="background:#d4abf2;color:{value_color};padding:2px;">{ascii_part}</td>
                            <td style="background:#c9f757;color:#000;padding:2px;">{meta.short_desc}</td>
                            <td style="background:#e0e0e0;color:{value_color};padding:2px;">{(flag and f'{flag.name}: {flag.short_desc}') or ''}</td>
                        </tr>
                        """

                if not use_flag:
                    html += f"""
                        <tr>
                            <td style="background:#b779e3;color:#fff;padding:2px;">{meta.short_name or field}</td>
                            <td style="background:#fff0af;color:#000;padding:2px;">{range_str}</td>
                            <td style="background:#ffd00b;color:{value_color};padding:2px;">{hex_part}</td>
                            <td style="background:#d4abf2;color:{value_color};padding:2px;">{ascii_part}</td>
                            <td style="background:#c9f757;color:#000;padding:2px;">{meta.short_desc}</td>
                            <td style="background:#e0e0e0;color:{value_color};padding:2px;">{(enum_value and f'{enum_value.name}: {enum_value.short_desc}') or ''}</td>
                        </tr>
                    """

            html += "</table>"
            return html

        def _print_struct_header(self, color: bool = True) -> None:
            """
            This method prints the structure name.
            """

            struct_name = getattr(self, "_struct_name_", self.__class__.__name__)
            line = f" {struct_name} ".center(139, "*")
            if color:
                print(
                    "\n",
                    f"\x1b[48;2;50;50;50m\x1b[38;2;175;241;11m{line}\x1b[49m\x1b[39m",
                    "\n",
                    sep=""
                )
            else:
                print("\n", line, "\n", sep="")

        def pretty_print(self, verbosity: int = 1, color: bool = True) -> None:
            """
            This method prints a string to represent the
            structure with each fields and values.
            """

            self._print_struct_header(color=color)

            for field, _ in self._fields_:
                meta = self._field_metas_.get(field, FieldMeta())
                if meta.verbosity > verbosity:
                    continue

                value = getattr(self, field)
                start, end = self._get_field_range(field)
                data = field_to_bytes(value)
                hex_part = hexlify(data).decode().ljust(40)
                ascii_part = "".join(chr(x) if x in printable else "." for x in data).ljust(20)

                score = self._normality_score(field, value)

                if color:
                    if score < 0.5:
                        color_code = "\x1b[38;2;255;77;77m"
                    elif score < 0.8:
                        color_code = "\x1b[38;2;255;204;0m"
                    else:
                        color_code = "\x1b[38;2;76;175;80m"

                    print(
                        f"\x1b[38;2;183;121;227m{(meta.short_name or field).ljust(25)}",
                        f"\x1b[38;2;255;240;175m{start:0>8x}-{end:0>8x}".ljust(20),
                        f"\x1b[38;2;255;208;11m{hex_part}",
                        color_code + ascii_part,
                        f"\x1b[38;2;201;247;87m{meta.short_desc}",
                        "\x1b[39m",
                    )
                else:
                    print(
                        (meta.short_name or field).ljust(25),
                        f"{start:0>8x}-{end:0>8x}".ljust(20),
                        hex_part,
                        ascii_part,
                        meta.short_desc
                    )

    return _EnhancedStruct

def test() -> int:
    """
    This function test the file.
    """

    class MZHeader(EnhancedStruct(little_endian=True)):
        _struct_name_ = "DOS Header"
        _struct_desc_ = "Microsoft DOS executable header"

        _fields_ = [
            ("e_magic", c_uint16),
            ("e_cblp", c_uint16),
            ("e_test", c_uint16),
            ("e_test2", c_uint16),
        ]

        _field_metas_ = {
            "e_magic": FieldMeta(
                short_name="Magic",
                short_desc="Mark Zbikowski magic (MZ)",
                verbosity=1,
                enum=[
                    EnumMeta(0x5A4D, "MZ", "Valid MZ header", normality=1.0),
                ],
            ),
            "e_test": FieldMeta(
                short_name="Test",
                short_desc="Test field with normality",
                verbosity=1,
                enum=[
                    EnumMeta(0x5A4D, "MZ", "Valid MZ header", normality=1.0),
                    EnumMeta(0x0000, "MZ", "Invalid MZ header", normality=0.0),
                ],
            ),
            "e_test2": FieldMeta(
                short_name="Test Flags",
                short_desc="Field with multiple flags of varying normality",
                verbosity=1,
                flags=[
                    FlagMeta(bit=0, name="Flag A", short_desc="Very abnormal", normality=0.0),
                    FlagMeta(bit=1, name="Flag B", short_desc="Moderately normal", normality=0.5),
                    FlagMeta(bit=2, name="Flag C", short_desc="Very normal", normality=1.0),
                ],
            ),
        }

    hdr = MZHeader()
    hdr.e_magic = c_uint16(0x5A4D)
    hdr.e_cblp = c_uint16(144)
    hdr.e_test = c_uint16(0x5A4D)
    hdr.e_test2 = c_uint16(0)

    hdr.pretty_print()
    print(hdr.to_dict())
    print(hdr.to_html())

    hdr = MZHeader()
    hdr.e_magic = 0x5A4D
    hdr.e_cblp = 144
    hdr.e_test = 0x0000
    hdr.e_test2 = 1

    hdr.pretty_print()
    print(hdr.to_dict())
    print(hdr.to_html())

    hdr = MZHeader()
    hdr.e_magic = 0x5A4D
    hdr.e_cblp = 144
    hdr.e_test = 0x0001
    hdr.e_test2 = 2

    hdr.pretty_print()
    print(hdr.to_dict())
    print(hdr.to_html())
    return 0

if __name__ == "__main__":
    exit(test())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements tools to build python package and tools.
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
This package implements tools to build python package and tools.

>>> arg = ScapyArguments()
>>> arg.parse_args().iface
<NetworkInterface ...>
>>> arg.parse_args(["-i", "eth0"]).iface
<NetworkInterface ...>
>>> arg.parse_args(["--interface", "eth"]).iface
<NetworkInterface ...>

>>> arg = ScapyArguments(interface_args=["++custom", "|c"], prefix_chars="+|")
>>> arg.parse_args().iface
<NetworkInterface ...>
>>> arg.parse_args(["|c", "127.0.0"]).iface
<NetworkInterface ...>
>>> arg.parse_args(["++custom", "00:00:00:"]).iface
<NetworkInterface ...>

>>> arg = ScapyArguments(interface_kwargs={"required", True}, description="My program description")
>>> arg.parse_args(["-i", "172.16.10."]).iface
<NetworkInterface ...>
>>> arg.parse_args(["--interface", "0A:00:34:"]).iface
<NetworkInterface ...>

>>> get_ip_interfaces()
{'172.16.40.10': Interface(ip=IPv4Address('172.16.40.10'), network=IPv4Network('172.16.0.0/16'), route=(2886729728, 4294901760, '0.0.0.0', 'eth0', '172.16.0.1', 5256), interface=<NetworkInterface eth0 [UP+BROADCAST+RUNNING+SLAVE]>)}
>>> get_ip_interfaces(4)
{'172.16.40.10': Interface(ip=IPv4Address('172.16.40.10'), network=IPv4Network('172.16.0.0/16'), route=(2886729728, 4294901760, '0.0.0.0', 'eth0', '172.16.0.1', 5256), interface=<NetworkInterface eth0 [UP+BROADCAST+RUNNING+SLAVE]>)}
>>> get_ip_interfaces(6)
{'fe80::5656:5247:a5d8:dbce': Interface(ip=IPv6Address('fe80::5656:5247:a5d8:dbce'), network=IPv6Network('fe80::5656:5247:a5d8:dbce/128'), route=('fe80::5656:5247:a5d8:dbce', 128, '::', 'eth0', ['fe80::5656:5247:a5d8:dbce'], 5256), interface=<NetworkInterface eth0 [UP+BROADCAST+RUNNING+SLAVE]>)}

>>> get_gateway()
'172.16.0.1'
>>> get_gateway(4)
'172.16.0.1'
>>> get_gateway(6)
'fe80::5656:5247:a5d8:dbce'

>>> get_gateway_route()
Interface(ip=IPv4Address('172.16.40.10'), network=IPv4Network('172.16.0.0/16'), route=(2886729728, 4294901760, '0.0.0.0', 'eth0', '172.16.0.1', 5256), interface=<NetworkInterface eth0 [UP+BROADCAST+RUNNING+SLAVE]>)
>>> get_gateway_route(4)
Interface(ip=IPv4Address('172.16.40.10'), network=IPv4Network('172.16.0.0/16'), route=(2886729728, 4294901760, '0.0.0.0', 'eth0', '172.16.0.1', 5256), interface=<NetworkInterface eth0 [UP+BROADCAST+RUNNING+SLAVE]>)
>>> get_gateway_route(6)
Interface(ip=IPv6Address('fe80::5656:5247:a5d8:dbce'), network=IPv6Network('fe80::5656:5247:a5d8:dbce/128'), route=('fe80::5656:5247:a5d8:dbce', 128, '::', 'eth0', ['fe80::5656:5247:a5d8:dbce'], 5256), interface=<NetworkInterface eth0 [UP+BROADCAST+RUNNING+SLAVE]>)
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

__all__ = [
    "ScapyArguments",
    "get_gateway_route",
    "get_gateway",
    "get_ip_interfaces",
    "Interface",
]

from ipaddress import (
    IPv4Address,
    IPv4Network,
    IPv6Address,
    IPv6Network,
    ip_address,
    ip_network,
)
from typing import NewType, Union, Dict, List, Tuple
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from sys import executable

try:
    from scapy.all import IFACES, conf, NetworkInterface, ltoa
except ImportError as e:
    raise ImportError(
        "Scapy should be installed to use this module.\n"
        f"You can install it with: {executable} -m pip install scapy"
    ) from e


IPv6Route = NewType("IPv6Route", Tuple[str, int, str, str, List[str], int])
IPv4Route = NewType("IPv4Route", Tuple[int, int, str, str, str, int])
Route = NewType("Route", Union[IPv4Route, IPv6Route])


@dataclass
class Interface:
    ip: ip_address
    network: ip_network
    route: Route
    interface: NetworkInterface


class ScapyArguments(ArgumentParser):

    """
    This class implements ArgumentsParser with
    interface argument and iface research.
    """

    interface_args: list = ["--interface", "-i"]
    interface_kwargs: dict = {
        "help": "Part of the IP, MAC or name of the interface",
    }

    def __init__(
        self,
        *args,
        interface_args=interface_args,
        interface_kwargs=interface_kwargs,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.interface_args = interface_args
        self.interface_kwargs = interface_kwargs
        self.add_argument(*interface_args, **interface_kwargs)

    def parse_args(
        self, args: List[str] = None, namespace: Namespace = None
    ) -> Namespace:
        """
        This function implements the iface
        research from interface arguments.
        """

        namespace: Namespace = ArgumentParser.parse_args(self, args, namespace)

        argument_name: str = max(self.interface_args, key=len)
        for char in self.prefix_chars:
            if char == argument_name[0]:
                argument_name = argument_name.lstrip(char)
                break

        interface = getattr(namespace, argument_name, None)

        if interface is not None:
            interface = interface.casefold()

            for temp_iface in IFACES.values():
                ip = temp_iface.ip
                mac = temp_iface.mac or ""
                name = temp_iface.name or ""
                network_name = temp_iface.network_name or ""

                mac = mac.casefold()
                name = name.casefold()
                network_name = network_name.casefold()

                if (
                    (ip and interface in ip)
                    or (mac and interface in mac)
                    or (name and interface in name)
                    or (network_name and interface in network_name)
                ):
                    namespace.iface = temp_iface
                    return namespace

        namespace.iface = conf.iface
        return namespace


def get_ip_interfaces(version: int = 4) -> Dict[str, Interface]:
    """
    This function generates a dict of Interfaces by IP
    (version should be 4 for IPv4 addresses and 6 for IPv6 addresses).
    """

    if version == 4:
        return {
            ip: Interface(
                IPv4Address(ip),
                IPv4Network("%s/%s" % (ltoa(route[0]), ltoa(route[1]))),
                route,
                interface,
            )
            for interface in IFACES.data.values()
            for ip in interface.ips[4]
            for route in conf.route.routes
            if route[1] != 4294967295
            and IPv4Address(ip)
            in IPv4Network("%s/%s" % (ltoa(route[0]), ltoa(route[1])))
        }
    elif version == 6:
        return {
            ip: Interface(
                IPv6Address(ip),
                IPv6Network("%s/%i" % (route[0], route[1])),
                route,
                interface,
            )
            for interface in IFACES.data.values()
            for ip in interface.ips[6]
            for route in conf.route6.routes
            if IPv6Address(ip) in IPv6Network("%s/%i" % (route[0], route[1]))
        }
    else:
        raise ValueError(
            "Version (first and optional argument should"
            " be 4 for IPv4 addresses or 6 for IPv6 addresses."
        )


def get_gateway(version: int = 4) -> str:
    """
    This function returns gateway (IPv4 or IPv6).
    """

    if version == 4:
        return conf.route.route("0.0.0.0")[2]
    elif version == 6:
        return conf.route6.route("::/0")[2]
    else:
        raise ValueError(
            "Version (first and optional argument should"
            " be 4 for IPv4 addresses or 6 for IPv6 addresses."
        )


def get_gateway_route(version: int = 4) -> Interface:
    """
    This function returns the gateway Interface.
    """

    gateway = ip_address(get_gateway(version))
    interfaces = get_ip_interfaces(version)

    for interface in interfaces.values():
        if gateway in interface.network:
            return interface

    _interface = get_gateway_route(4 if version == 6 else 4)

    for interface in interfaces.values():
        if interface.interface is _interface.interface:
            return interface

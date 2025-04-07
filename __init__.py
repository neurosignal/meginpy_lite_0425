#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
meginpy_lite_0425 was inherited from MeginPy for converting the 
string type digitization into extra type headshape points using show_fiff.
Author: Amit Jaiswwal <amit.jaiswal@megin.fi> 
"""
from . import digitization

try:
    from ._version import __version__
except ModuleNotFoundError:
    print("_version.py not present. Trying to get version using pkg_resources")
    __version__ = "unknown"

__all__ = [
    "digitization",
]

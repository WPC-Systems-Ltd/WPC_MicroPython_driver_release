'''
System - get_system_info.py.

This example demonstrates how to get system information.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Get driver verion
version = pywpc.Sys_getDriverVersion()
print(version)

## Get driver name
name = pywpc.Sys_getDriverName()
print(name)
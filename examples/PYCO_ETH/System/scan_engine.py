
'''
System - scan_engine.py.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Start scanning engine
pywpc.Sys_startScanEngine()

n = 100
do = [0] * 8
ao = [0] * 8

for i in range(n):
    di = pywpc.DI_readPort()
    ai = pywpc.AI_readPort()

    do[0]= di[0]
    do[1] = int(ai[1] > 5)
    ao[0] = ai[0]
    ao[1] = 10 * di[1] - 5

    pywpc.DO_writePort(do)
    pywpc.AO_writePort(ao)

    time.sleep(0.02)

## Stop scanning engine
pywpc.Sys_stopScanEngine()


#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : finding.py
@Time : 4/10/22 5:49 PM
@Desc: 
"""

import time

nemo = ["NEMO"]
large = ['NEMO'] * 10


def find_nemo(nemo):
    """
    :param nemo:
    :return:
    """
    start = time.time()
    for x in nemo:
        if x == "NEMO":
            print("Found nemo")
    done = time.time()
    elapsed = done - start
    print('Took ' + str(elapsed) + ' milliseconds')


find_nemo(large)

#!/usr/bin/env python3

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OTHER = '\033[96m'
    ENDC = '\033[0m'


print(bcolors.OTHER + "DOCKER TEST 1" + bcolors.ENDC)


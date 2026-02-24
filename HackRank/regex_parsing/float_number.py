"""Detect Floating point numbers"""
import re

RULE = r'^[+-]?\d*\.\d+$'

for i in range(int(input())):
    print(bool(re.fullmatch(RULE, input())))

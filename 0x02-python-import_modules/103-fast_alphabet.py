#!/usr/bin/python3
from string import ascii_uppercase; import os;
os.write(1, bytes(ascii_uppercase + '\n', 'utf-8'))

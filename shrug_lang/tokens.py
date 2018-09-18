from enum import Enum


class Tokens(Enum):
    SHRUG = 1
    NUMBER = 2
    STRING = 3
    ID = 4
    BOF = 5
    EOF = 6
    EOL = 7
    INVALID = 8

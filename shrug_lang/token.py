class Token:
    SHRUG = 1
    NUMBER = 2
    STRING = 3
    ID = 4
    BOF = 5
    EOF = 6
    EOL = 7
    INVALID = 8

    def __init__(self, _type, value=None):
        self.type = _type
        self.value = value

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type

    def __str__(self):
        return f'Token({self.type}, {self.value})'

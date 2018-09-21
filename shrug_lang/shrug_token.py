from dataclasses import dataclass
from enum import Enum
from typing import Union


class TokenType(Enum):
    SHRUG = 1
    NUMBER = 2
    STRING = 3
    ID = 4
    EOL = 5
    INVALID = 6


@dataclass(init=False)
class Token:
    type: TokenType
    value: Union[int, str, None] = None

    def __init__(self, _type: TokenType, value: Union[int, str, None]=None):
        if not isinstance(_type, TokenType):
            raise TypeError('Token type must be of TokenType')
        must_have_value = {TokenType.NUMBER, TokenType.STRING, TokenType.ID,
                           TokenType.INVALID}
        if _type in must_have_value and value is None:
            raise ValueError(f'Token type {_type} must have a value')
        self.type = _type
        self.value = value

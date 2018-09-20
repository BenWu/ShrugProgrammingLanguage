from dataclasses import dataclass
from enum import Enum
from typing import Any


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
    value: Any = None

    def __init__(self, _type, value=None):
        must_have_value = {TokenType.NUMBER, TokenType.STRING, TokenType.ID,
                           TokenType.INVALID}
        if _type in must_have_value and value is None:
            raise ValueError(f'Token type {_type} must have a value')
        self.type = _type
        self.value = value

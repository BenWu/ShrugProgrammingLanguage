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


@dataclass
class Token:
    type: TokenType
    value: Any = None

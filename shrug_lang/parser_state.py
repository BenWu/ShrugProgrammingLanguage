from enum import Enum

from shrug_lang.errors import TokenError
from shrug_lang.shrug_token import Token, TokenType


class ParserState(Enum):
    EMPTY = 0
    INVALID = 1001
    END = 1002

    MATH = 1
    ADDITION = 2
    SUBTRACTION = 3
    MULTIPLICATION = 4
    DIVISION = 5
    MODULUS = 6

    COMPARE = 11
    EQ = 12
    NEQ = 13
    GT = 14
    GTE = 15
    LT = 16
    LTE = 17


class StateTransformer:
    """Calculates next state given a token"""

    def __init__(self):
        self.state_transformer = {
            ParserState.EMPTY: {
                TokenType.ID: ParserState.EMPTY,
                TokenType.NUMBER: ParserState.END,
                TokenType.BOOL: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.MATH
            },

            ParserState.INVALID: {},

            ParserState.END: {},

            ParserState.MATH: {
                TokenType.ID: ParserState.ADDITION,
                TokenType.NUMBER: ParserState.ADDITION,
                TokenType.BOOL: ParserState.ADDITION,
                TokenType.STRING: ParserState.ADDITION,
                TokenType.SHRUG: ParserState.COMPARE
            },

            ParserState.ADDITION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.BOOL: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.SUBTRACTION
            },

            ParserState.SUBTRACTION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.BOOL: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.MULTIPLICATION
            },

            ParserState.MULTIPLICATION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.BOOL: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.DIVISION
            },

            ParserState.DIVISION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.BOOL: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.MODULUS
            },

            ParserState.MODULUS: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.BOOL: ParserState.END,
                TokenType.STRING: ParserState.END
            },
        }

    def next_state(self, state: ParserState, token: Token) -> ParserState:
        try:
            return self.state_transformer[state][token.type]
        except KeyError:
            raise TokenError(f'Unexpected token {token} at state {state}')

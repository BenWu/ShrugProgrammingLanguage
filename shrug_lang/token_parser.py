from enum import Enum
from typing import Union

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


class TokenError(Exception):
    pass


class StateTransformer:
    """Calculates next state given a token"""

    def __init__(self):
        self.state_transformer = {
            ParserState.EMPTY: {
                TokenType.ID: ParserState.EMPTY,
                TokenType.NUMBER: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.MATH
            },

            ParserState.INVALID: {},

            ParserState.END: {},

            ParserState.MATH: {
                TokenType.ID: ParserState.ADDITION,
                TokenType.NUMBER: ParserState.ADDITION,
                TokenType.STRING: ParserState.ADDITION,
                TokenType.SHRUG: ParserState.COMPARE
            },

            ParserState.ADDITION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.SUBTRACTION
            },

            ParserState.SUBTRACTION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.MULTIPLICATION
            },

            ParserState.MULTIPLICATION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.DIVISION
            },

            ParserState.DIVISION: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.STRING: ParserState.END,
                TokenType.SHRUG: ParserState.MODULUS
            },

            ParserState.MODULUS: {
                TokenType.ID: ParserState.END,
                TokenType.NUMBER: ParserState.END,
                TokenType.STRING: ParserState.END
            },
        }

    def next_state(self, state: ParserState, token: Token) -> ParserState:
        try:
            return self.state_transformer[state][token.type]
        except KeyError:
            raise TokenError(f'Unexpected token {token} at state {state}')


class WtfError(Exception):
    """(For debugging) Should never occur"""
    pass


class Operation:
    @staticmethod
    def check_for_undefined(val1, val2):
        """Raise an error with correct message if either value is undefined"""
        if val1[0] is None and val2[0] is None:
            raise ValueError(f'Undefined values {val1[1]} and {val2[1]}')
        if val1[0] is None:
            raise ValueError(f'Undefined values {val1[1]}')
        if val2[0] is None:
            raise ValueError(f'Undefined values {val2[1]}')

    @staticmethod
    def check_non_numbers(val1, val2, operation_type):
        """Raise an error if either value is not an int"""
        val1 = val1[0]
        val2 = val2[0]
        if isinstance(val1, str) and isinstance(val2, str):
            raise TypeError(
                f'Unsupported {operation_type} types: string and string')
        if isinstance(val1, str) and isinstance(val2, int):
            raise TypeError(
                f'Unsupported {operation_type} types: str and number')
        if isinstance(val1, int) and isinstance(val2, str):
            raise TypeError(
                f'Unsupported {operation_type} types: number and str')

    @staticmethod
    def add(val1, val2):
        Operation.check_for_undefined(val1, val2)
        val1 = val1[0]
        val2 = val2[0]
        if isinstance(val1, str):
            if isinstance(val2, str):
                return val1 + val2
            if isinstance(val2, int):
                return val1 + str(val2)
            raise WtfError
        if isinstance(val1, int):
            if isinstance(val2, str):
                return str(val1) + val2
            if isinstance(val2, int):
                return val1 + val2
            raise WtfError
        raise WtfError

    @staticmethod
    def subtract(val1, val2):
        Operation.check_for_undefined(val1, val2)
        Operation.check_non_numbers(val1, val2, 'subtraction')
        return val1[0] - val2[0]

    @staticmethod
    def multiply(val1, val2):
        Operation.check_for_undefined(val1, val2)
        if isinstance(val1[0], str) and isinstance(val2[0], str):
            raise TypeError('Unsupported multiplication types: '
                            'string and string')
        return val1[0] * val2[0]

    @staticmethod
    def divide(val1, val2):
        Operation.check_for_undefined(val1, val2)
        Operation.check_non_numbers(val1, val2, 'division')
        return val1[0] // val2[0]

    @staticmethod
    def modulus(val1, val2):
        Operation.check_for_undefined(val1, val2)
        Operation.check_non_numbers(val1, val2, 'modulus')
        return val1[0] % val2[0]


class TokenParser:
    def __init__(self):
        self.math_operations = {
            ParserState.ADDITION: Operation.add,
            ParserState.SUBTRACTION: Operation.subtract,
            ParserState.MULTIPLICATION: Operation.multiply,
            ParserState.DIVISION: Operation.divide,
            ParserState.MODULUS: Operation.modulus,
        }
        self.state_transformer = StateTransformer()
        self.value_map = {}
        self.state = ParserState.EMPTY
        self.tokens = []
        self.assign_to = None
        self.current_value = None
        self.value1 = None
        self.value2 = None

    def reset_state(self):
        self.state = ParserState.EMPTY
        self.tokens = []
        self.assign_to = None
        self.current_value = None
        self.value1 = None
        self.value2 = None

    def next_token(self, token: Token):
        try:
            if token.type == TokenType.EOL:
                try:
                    if self.state == ParserState.EMPTY:
                        if self.assign_to:
                            return self.get_value(self.assign_to)
                        return
                    if self.state == ParserState.END:
                        if self.assign_to:
                            self.set_value(self.assign_to, self.current_value)
                        else:
                            return self.current_value
                        return
                finally:
                    self.reset_state()
                # Not in valid state to end line
                raise TokenError('Unexpected end-of-line')

            if token.type == TokenType.INVALID:
                raise TokenError(f'Invalid token {token.value}')

            if self.state == ParserState.EMPTY:
                if token.type == TokenType.ID:
                    self.assign_to = token.value
                elif (token.type == TokenType.NUMBER or
                      token.type == TokenType.STRING):
                    self.current_value = token.value

            elif self.state == ParserState.MATH:
                if token.type == TokenType.ID:
                    self.value1 = (self.get_value(token.value), token.value)
                elif (token.type == TokenType.NUMBER or
                      token.type == TokenType.STRING):
                    self.value1 = (token.value,)

            elif self.state in self.math_operations.keys():
                if token.type == TokenType.ID:
                    self.value2 = (self.get_value(token.value), token.value)
                    self.current_value = (self.math_operations[self.state]
                                          (self.value1, self.value2))
                elif (token.type == TokenType.NUMBER or
                      token.type == TokenType.STRING):
                    self.value2 = (token.value,)
                    self.current_value = (self.math_operations[self.state]
                                          (self.value1, self.value2))

            self.next_state(token)

        except Exception as e:
            self.reset_state()
            raise e

    def next_state(self, token: Token):
        self.state = self.state_transformer.next_state(self.state, token)

    def get_value(self, key: str) -> Union[int, str, None]:
        return self.value_map.get(key)

    def set_value(self, key: str, value: Union[int, str, None]):
        self.value_map[key] = value

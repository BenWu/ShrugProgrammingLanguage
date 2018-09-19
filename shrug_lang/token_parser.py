from enum import Enum

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


class TokenError(Exception):
    pass


class TokenParser:
    def __init__(self):
        self.value_map = {}
        self.state = ParserState.EMPTY
        self.tokens = []
        self.assign_to = None
        self.current_value = None

    def reset_state(self):
        self.state = ParserState.EMPTY
        self.tokens = []
        self.assign_to = None
        self.current_value = None

    def next_token(self, token: Token):
        if token.type == TokenType.EOL:
            if self.state == ParserState.EMPTY:
                if self.assign_to:
                    print(self.get_value(self.assign_to))
                return
            if self.state == ParserState.END:
                if self.assign_to:
                    self.set_value(self.assign_to, self.current_value)
                else:
                    print(self.current_value)
                self.reset_state()
                return
            # Not in valid state to end line
            raise TokenError('Unexpected end-of-line')

        if token.type == TokenType.INVALID:
            raise TokenError(f'Invalid token {token.value}')

        if self.state == ParserState.EMPTY:
            if token.type == TokenType.ID:
                self.assign_to = token.value
                self.current_value = self.get_value(token.value)
            elif token.type == TokenType.NUMBER or TokenType.STRING:
                self.state = ParserState.END
                self.current_value = token.value
            elif token.type == TokenType.SHRUG:
                self.state = ParserState.MATH
        else:
            pass

    def get_value(self, key):
        return self.value_map.get(key)

    def set_value(self, key, value):
        self.value_map[key] = value

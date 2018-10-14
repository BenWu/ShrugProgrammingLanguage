from typing import Union

from shrug_lang.errors import TokenError
from shrug_lang.operators import CompOp, MathOp
from shrug_lang.parser_state import ParserState, StateTransformer
from shrug_lang.shrug_token import Token, TokenType


class TokenParser:
    def __init__(self):
        self.operations = {
            ParserState.ADDITION: MathOp.add,
            ParserState.SUBTRACTION: MathOp.subtract,
            ParserState.MULTIPLICATION: MathOp.multiply,
            ParserState.DIVISION: MathOp.divide,
            ParserState.MODULUS: MathOp.modulus,
            ParserState.EQ: CompOp.eq,
            ParserState.NEQ: CompOp.neq,
            ParserState.GT: CompOp.gt,
            ParserState.GTE: CompOp.gte,
            ParserState.LT: CompOp.lt,
            ParserState.LTE: CompOp.lte,
        }
        self.state_transformer = StateTransformer()
        self.value_map = {}
        self.state = ParserState.EMPTY
        self.tokens = []
        self.assign_to = None
        self.current_value = None
        self.value1 = None
        self.value2 = None
        self.in_cond = False
        self.skip_line = False
        self.comment = False

        # Not reset after line
        self.indent = 0
        self.skip_indented = False  # skip lines that are indented +1

    def reset_state(self):
        self.state = ParserState.EMPTY
        self.tokens = []
        self.assign_to = None
        self.current_value = None
        self.value1 = None
        self.value2 = None
        self.in_cond = False
        self.skip_line = False
        self.comment = False

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
                        elif self.in_cond:
                            if self.current_value:
                                self.indent += 1
                            else:
                                self.skip_indented = True
                        else:
                            return self.current_value
                        return
                finally:
                    self.reset_state()
                # Not in valid state to end line
                raise TokenError('Unexpected end-of-line')

            if token.type == TokenType.COMMENT:
                self.comment = True
                return

            if token.type == TokenType.INVALID:
                raise TokenError(f'Invalid token {token.value}')

            if self.skip_line:
                pass

            elif token.type == TokenType.INDENT:
                if token.value == self.indent:
                    if self.skip_indented:
                        self.skip_indented = False
                elif token.value < self.indent:
                    self.indent = token.value
                elif token.value > self.indent and self.skip_indented:
                    self.skip_line = True
                else:
                    raise TokenError('Unexpected indentation')

            elif self.state == ParserState.EMPTY:
                if token.type == TokenType.ID:
                    self.assign_to = token.value
                elif (token.type == TokenType.NUMBER or
                      token.type == TokenType.STRING or
                      token.type == TokenType.BOOL):
                    self.current_value = token.value

            elif (self.state == ParserState.MATH or
                  self.state == ParserState.COMPARE):
                if token.type == TokenType.ID:
                    self.value1 = (self.get_value(token.value), token.value)
                elif (token.type == TokenType.NUMBER or
                      token.type == TokenType.STRING or
                      token.type == TokenType.BOOL):
                    self.value1 = (token.value,)

            elif self.state in self.operations:
                operation = self.operations[self.state]
                if token.type == TokenType.ID:
                    self.value2 = (self.get_value(token.value), token.value)
                    self.current_value = operation(self.value1, self.value2)
                elif (token.type == TokenType.NUMBER or
                      token.type == TokenType.STRING or
                      token.type == TokenType.BOOL):
                    self.value2 = (token.value,)
                    self.current_value = operation(self.value1, self.value2)

            if self.state == ParserState.COND:
                if token.type == TokenType.ID:
                    self.current_value = self.get_value(token.value)
                    if self.assign_to:
                        raise TokenError('Cannot assign conditional statement')
                elif (token.type == TokenType.NUMBER or
                      token.type == TokenType.STRING or
                      token.type == TokenType.BOOL):
                    self.current_value = token.value
                    if self.assign_to:
                        raise TokenError('Cannot assign conditional statement')
                self.in_cond = True

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

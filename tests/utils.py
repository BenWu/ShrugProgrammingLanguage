import unittest

from shrug_lang.shrug_token import Token, TokenType
from shrug_lang.token_parser import TokenParser


class TokenGenerator:
    @staticmethod
    def get_eol():
        return Token(TokenType.EOL)

    @staticmethod
    def get_id(name='a'):
        return Token(TokenType.ID, name)

    @staticmethod
    def get_number(value=123):
        return Token(TokenType.NUMBER, value)

    @staticmethod
    def get_bool(value=True):
        return Token(TokenType.BOOL, value)

    @staticmethod
    def get_string(value='abc'):
        return Token(TokenType.STRING, value)

    @staticmethod
    def get_shrug():
        return Token(TokenType.SHRUG)

    @staticmethod
    def get_invalid(value='invalid'):
        return Token(TokenType.INVALID, value)

    @staticmethod
    def get_indent(value=0):
        return Token(TokenType.INDENT, value)


class BaseTokenParserTestCase(unittest.TestCase):
    """Base class for token parser test cases"""
    def setUp(self):
        self.token_parser = TokenParser()

    def process_tokens(self, tokens):
        return list(filter(
            lambda x: x is not None,
            [self.token_parser.next_token(token) for token in tokens]))

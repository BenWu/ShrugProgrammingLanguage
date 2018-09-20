import unittest

from shrug_lang.shrug_token import TokenType, Token
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
    def get_string(value='abc'):
        return Token(TokenType.STRING, value)


class TestTokenParser(unittest.TestCase):
    """Token parser should give correct output based on series of tokens"""

    def setUp(self):
        self.token_parser = TokenParser()

    def process_tokens(self, tokens):
        return [self.token_parser.next_token(token) for token in tokens]

    def test_single_int_output(self):
        tokens = [TokenGenerator.get_number(5), TokenGenerator.get_eol()]
        expected = [None, 5]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_single_string_output(self):
        tokens = [TokenGenerator.get_string('abc'), TokenGenerator.get_eol()]
        expected = [None, 'abc']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_output_unassigned(self):
        tokens = [TokenGenerator.get_id(), TokenGenerator.get_eol()]
        expected = [None, None]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_assign_int_and_output(self):
        tokens = [TokenGenerator.get_id(), TokenGenerator.get_number(123),
                  TokenGenerator.get_eol(), TokenGenerator.get_id(),
                  TokenGenerator.get_eol()]
        expected = [None, None, None, None, 123]
        self.assertEqual(expected, self.process_tokens(tokens))


if __name__ == '__main__':
    unittest.main()

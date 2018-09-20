import unittest

from shrug_lang.shrug_token import TokenType, Token
from shrug_lang.token_parser import TokenParser


class TestTokenParser(unittest.TestCase):
    """Token parser should give correct output based on series of tokens"""

    def setUp(self):
        self.token_parser = TokenParser()

    def process_tokens(self, tokens):
        return [self.token_parser.next_token(token) for token in tokens]

    def test_single_int_output(self):
        tokens = [Token(TokenType.NUMBER, 5), Token(TokenType.EOL)]
        expected = [None, 5]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_single_string_output(self):
        tokens = [Token(TokenType.STRING, 'abc'), Token(TokenType.EOL)]
        expected = [None, 'abc']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_output_unassigned(self):
        tokens = [Token(TokenType.ID), Token(TokenType.EOL)]
        expected = [None, None]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_assign_int_and_output(self):
        tokens = [Token(TokenType.ID, 'a'), Token(TokenType.NUMBER, 98),
                  Token(TokenType.EOL), Token(TokenType.ID, 'a'),
                  Token(TokenType.EOL)]
        expected = [None, None, None, None, 98]
        self.assertEqual(expected, self.process_tokens(tokens))


if __name__ == '__main__':
    unittest.main()

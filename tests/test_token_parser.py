import unittest

from shrug_lang.errors import TokenError
from .utils import BaseTokenParserTestCase, TokenGenerator


class TestBasicTokenParser(BaseTokenParserTestCase):
    """Token parser should give correct output based on series of tokens"""
    def test_empty_line(self):
        tokens = [TokenGenerator.get_eol()]
        expected = []
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_single_int_output(self):
        tokens = [TokenGenerator.get_number(5), TokenGenerator.get_eol()]
        expected = [5]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_single_string_output(self):
        tokens = [TokenGenerator.get_string('abc'), TokenGenerator.get_eol()]
        expected = ['abc']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_output_unassigned(self):
        tokens = [TokenGenerator.get_id(), TokenGenerator.get_eol()]
        expected = []
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_assign_int_and_output(self):
        tokens = [TokenGenerator.get_id(), TokenGenerator.get_number(123),
                  TokenGenerator.get_eol(), TokenGenerator.get_id(),
                  TokenGenerator.get_eol()]
        expected = [123]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_assign_bool_and_output(self):
        tokens = [TokenGenerator.get_id(), TokenGenerator.get_bool(True),
                  TokenGenerator.get_eol(), TokenGenerator.get_id(),
                  TokenGenerator.get_eol()]
        expected = [True]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_assign_string_and_output(self):
        tokens = [TokenGenerator.get_id(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_eol(), TokenGenerator.get_id(),
                  TokenGenerator.get_eol()]
        expected = ['abc']
        self.assertEqual(expected, self.process_tokens(tokens))


class TestInvalidTokens(BaseTokenParserTestCase):
    """Token parser should raise exception when given invalid token"""
    def test_invalid_token(self):
        self.assertRaises(TokenError, self.token_parser.next_token,
                          TokenGenerator.get_invalid('invalid'))

    def test_incomplete_line1(self):
        self.token_parser.next_token(TokenGenerator.get_shrug())
        self.assertRaises(TokenError, self.token_parser.next_token,
                          TokenGenerator.get_eol())

    def test_incomplete_line2(self):
        self.token_parser.next_token(TokenGenerator.get_id())
        self.token_parser.next_token(TokenGenerator.get_shrug())
        self.assertRaises(TokenError, self.token_parser.next_token,
                          TokenGenerator.get_eol())

    def test_invalid_token_at_state(self):
        self.token_parser.next_token(TokenGenerator.get_string())
        self.assertRaises(TokenError, self.token_parser.next_token,
                          TokenGenerator.get_string())


if __name__ == '__main__':
    unittest.main()

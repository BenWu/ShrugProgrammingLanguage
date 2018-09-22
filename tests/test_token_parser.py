import unittest

from shrug_lang.shrug_token import Token, TokenType
from shrug_lang.token_parser import Operation, TokenError, TokenParser


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

    @staticmethod
    def get_shrug():
        return Token(TokenType.SHRUG)

    @staticmethod
    def get_invalid(value='invalid'):
        return Token(TokenType.INVALID, value)


class BaseTokenParserTestCase(unittest.TestCase):
    """Base class for token parser test cases"""
    def setUp(self):
        self.token_parser = TokenParser()

    def process_tokens(self, tokens):
        return [self.token_parser.next_token(token) for token in tokens]


class TestBasicTokenParser(BaseTokenParserTestCase):
    """Token parser should give correct output based on series of tokens"""
    def test_empty_line(self):
        tokens = [TokenGenerator.get_eol()]
        expected = [None]
        self.assertEqual(expected, self.process_tokens(tokens))

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


class TestMathOperations(BaseTokenParserTestCase):
    """ADDITiON"""

    def test_var_var_addition(self):
        tokens = [TokenGenerator.get_id('aa'), TokenGenerator.get_number(5),
                  TokenGenerator.get_eol(),
                  TokenGenerator.get_id('bb'), TokenGenerator.get_number(6),
                  TokenGenerator.get_eol(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_id('aa'),
                  TokenGenerator.get_id('bb'), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, None, None, None, 11]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_str_addition(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('ab'),
                  TokenGenerator.get_string('cd'), TokenGenerator.get_eol()]
        expected = [None, None, None, 'abcd']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_int_int_addition(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(12),
                  TokenGenerator.get_number(3), TokenGenerator.get_eol()]
        expected = [None, None, None, 15]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_int_addition(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(12),
                  TokenGenerator.get_string('abc'), TokenGenerator.get_eol()]
        expected = [None, None, None, '12abc']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_int_str_addition(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_number(34), TokenGenerator.get_eol()]
        expected = [None, None, None, 'abc34']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_assign_addition(self):
        tokens = [TokenGenerator.get_id('a'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(12),
                  TokenGenerator.get_number(3), TokenGenerator.get_eol(),
                  TokenGenerator.get_id('a'), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, 15]
        self.assertEqual(expected, self.process_tokens(tokens))

    """SUBTRACTION"""

    def test_int_int_subtraction(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(12),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(3),
                  TokenGenerator.get_eol()]
        expected = [None, None, None, None, 9]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_str_subtraction(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('ab'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_string('cd'),
                  TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_str_int_subtraction(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(12),
                  TokenGenerator.get_shrug(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_int_str_subtraction(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(34),
                  TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_assign_subtraction(self):
        tokens = [TokenGenerator.get_id('a'), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(12), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(3), TokenGenerator.get_eol(),
                  TokenGenerator.get_id('a'), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, None, 9]
        self.assertEqual(expected, self.process_tokens(tokens))

    """MULTIPLICATION"""

    def test_int_int_multiplication(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(13),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(4), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, 52]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_str_multiplication(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('ab'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_string('cd'), TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_str_int_multiplication(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(3),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_string('abc'), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, 'abcabcabc']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_int_str_multiplication(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(2), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, 'abcabc']
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_assign_multiplication(self):
        tokens = [TokenGenerator.get_id('a'), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(12), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(3),
                  TokenGenerator.get_eol(), TokenGenerator.get_id('a'),
                  TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, None, None, 36]
        self.assertEqual(expected, self.process_tokens(tokens))

    """DIVISION"""

    def test_int_int_division(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(12),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(4),
                  TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, 3]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_str_division(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('ab'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_string('cd'),
                  TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_str_int_division(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(3),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_int_str_division(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(2),
                  TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_assign_division(self):
        tokens = [TokenGenerator.get_id('a'), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(14), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(3), TokenGenerator.get_eol(),
                  TokenGenerator.get_id('a'), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, None, None, None, 4]
        self.assertEqual(expected, self.process_tokens(tokens))

    """MODULUS"""

    def test_int_int_modulus(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(12),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(5), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, None, 2]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_str_modulus(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('ab'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_string('cd'), TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_str_int_modulus(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_number(3),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_string('abc'), TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_int_str_modulus(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_string('abc'),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(2), TokenGenerator.get_eol()]
        self.assertRaises(TypeError, self.process_tokens, tokens)

    def test_assign_modulus(self):
        tokens = [TokenGenerator.get_id('a'), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(10), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(3),
                  TokenGenerator.get_eol(), TokenGenerator.get_id('a'),
                  TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None,
                    None, None, None, None, 1]
        self.assertEqual(expected, self.process_tokens(tokens))

    """ERROR CHECKING"""

    def test_operation_check_undefined(self):
        Operation.check_for_undefined((1, 'a'), (2, 'b'))
        self.assertRaises(ValueError, Operation.check_for_undefined,
                          (None, None), (2, 'b'))
        self.assertRaises(ValueError, Operation.check_for_undefined,
                          (1, 'a'), (None, None))
        self.assertRaises(ValueError, Operation.check_for_undefined,
                          (None, None), (None, None))


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

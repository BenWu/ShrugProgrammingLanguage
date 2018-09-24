import unittest

from shrug_lang.token_parser import MathOp

from .utils import BaseTokenParserTestCase, TokenGenerator


class TestMathOperations(BaseTokenParserTestCase):
    """Integration tests for parsing lines that involve math operations"""

    """ADDITION"""

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

    def test_bool_bool_addition(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_bool(True),
                  TokenGenerator.get_bool(True), TokenGenerator.get_eol()]
        expected = [None, None, None, 2]
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

    def test_bool_bool_subtraction(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_bool(False),
                  TokenGenerator.get_shrug(), TokenGenerator.get_bool(True),
                  TokenGenerator.get_eol()]
        expected = [None, None, None, None, -1]
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

    def test_bool_bool_multiplication(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_bool(False),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_bool(True), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, 0]
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

    def test_bool_bool_division(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_bool(True),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_bool(True),
                  TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, 1]
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

    def test_bool_bool_modulus(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_bool(True),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_bool(True), TokenGenerator.get_eol()]
        expected = [None, None, None, None, None, None, None, 0]
        self.assertEqual(expected, self.process_tokens(tokens))

    """ERROR CHECKING"""

    def test_operation_check_undefined(self):
        MathOp.check_for_undefined((1, 'a'), (2, 'b'))
        self.assertRaises(ValueError, MathOp.check_for_undefined,
                          (None, None), (2, 'b'))
        self.assertRaises(ValueError, MathOp.check_for_undefined,
                          (1, 'a'), (None, None))
        self.assertRaises(ValueError, MathOp.check_for_undefined,
                          (None, None), (None, None))


if __name__ == '__main__':
    unittest.main()


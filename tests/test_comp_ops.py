import unittest

from shrug_lang.operators import CompOp
from .utils import BaseTokenParserTestCase, TokenGenerator


class TestCompOperations(unittest.TestCase):
    def test_equality(self):
        self.assertTrue(CompOp.eq(('',), ('',)))
        self.assertTrue(CompOp.eq(('abc',), ('abc',)))
        self.assertTrue(CompOp.eq((1,), (1,)))
        self.assertTrue(CompOp.eq((True,), (True,)))
        self.assertTrue(CompOp.eq((True,), (1,)))

        self.assertFalse(CompOp.eq(('',), ('a',)))
        self.assertFalse(CompOp.eq((2,), (1,)))
        self.assertFalse(CompOp.eq((False,), (True,)))
        self.assertFalse(CompOp.eq((True,), (2,)))

    def test_inequality(self):
        self.assertFalse(CompOp.neq(('',), ('',)))
        self.assertFalse(CompOp.neq(('abc',), ('abc',)))
        self.assertFalse(CompOp.neq((1,), (1,)))
        self.assertFalse(CompOp.neq((True,), (True,)))
        self.assertFalse(CompOp.neq((True,), (1,)))

        self.assertTrue(CompOp.neq(('',), ('a',)))
        self.assertTrue(CompOp.neq((2,), (1,)))
        self.assertTrue(CompOp.neq((False,), (True,)))
        self.assertTrue(CompOp.neq((True,), (2,)))

    def test_gt(self):
        self.assertTrue(CompOp.gt(('b',), ('a',)))
        self.assertTrue(CompOp.gt((2,), (1,)))

        self.assertRaises(TypeError, CompOp.gt, 'a', 1)
        self.assertRaises(TypeError, CompOp.gt, 1, '')

        self.assertFalse(CompOp.gt(('a',), ('a',)))
        self.assertFalse(CompOp.gt((1,), (1,)))

        self.assertFalse(CompOp.gt(('a',), ('b',)))
        self.assertFalse(CompOp.gt((1,), (2,)))

    def test_gte(self):
        self.assertTrue(CompOp.gte(('b',), ('a',)))
        self.assertTrue(CompOp.gte((2,), (1,)))

        self.assertRaises(TypeError, CompOp.gte, 'a', 1)
        self.assertRaises(TypeError, CompOp.gte, 1, '')

        self.assertTrue(CompOp.gte(('a',), ('a',)))
        self.assertTrue(CompOp.gte((1,), (1,)))

        self.assertFalse(CompOp.gte(('a',), ('b',)))
        self.assertFalse(CompOp.gte((1,), (2,)))

    def test_lt(self):
        self.assertFalse(CompOp.lt(('b',), ('a',)))
        self.assertFalse(CompOp.lt((2,), (1,)))

        self.assertRaises(TypeError, CompOp.lt, 'a', 1)
        self.assertRaises(TypeError, CompOp.lt, 1, '')

        self.assertFalse(CompOp.lt(('a',), ('a',)))
        self.assertFalse(CompOp.lt((1,), (1,)))

        self.assertTrue(CompOp.lt(('a',), ('b',)))
        self.assertTrue(CompOp.lt((1,), (2,)))

    def test_lte(self):
        self.assertFalse(CompOp.lte(('b',), ('a',)))
        self.assertFalse(CompOp.lte((2,), (1,)))

        self.assertRaises(TypeError, CompOp.lte, 'a', 1)
        self.assertRaises(TypeError, CompOp.lte, 1, '')

        self.assertTrue(CompOp.lte(('a',), ('a',)))
        self.assertTrue(CompOp.lte((1,), (1,)))

        self.assertTrue(CompOp.lte(('a',), ('b',)))
        self.assertTrue(CompOp.lte((1,), (2,)))


class TestCompParser(BaseTokenParserTestCase):
    def test_var_var_eq(self):
        tokens = [TokenGenerator.get_id('a'), TokenGenerator.get_number(5),
                  TokenGenerator.get_eol(),
                  TokenGenerator.get_id('b'), TokenGenerator.get_number(5),
                  TokenGenerator.get_eol(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_id('a'), TokenGenerator.get_id('b'),
                  TokenGenerator.get_eol()]
        expected = [True]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_int_int_neq(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(4), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(4), TokenGenerator.get_eol()]
        expected = [False]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_int_int_gt(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(4), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number(2),
                  TokenGenerator.get_eol()]
        expected = [True]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_int_int_gte(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(3), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number(4), TokenGenerator.get_eol()]
        expected = [False]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_str_lt(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number('abc'), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_number('abd'),
                  TokenGenerator.get_eol()]
        expected = [True]
        self.assertEqual(expected, self.process_tokens(tokens))

    def test_str_str_lte(self):
        tokens = [TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number('abc'), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_shrug(), TokenGenerator.get_shrug(),
                  TokenGenerator.get_number('abc'), TokenGenerator.get_eol()]
        expected = [True]
        self.assertEqual(expected, self.process_tokens(tokens))


if __name__ == '__main__':
    unittest.main()

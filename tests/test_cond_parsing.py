import unittest

from .utils import BaseTokenParserTestCase, TokenGenerator

cond_shrugs = [TokenGenerator.get_shrug()] * 3


class TestCondParsing(BaseTokenParserTestCase):
    def test_simple_true_cond(self):
        tokens = [
            TokenGenerator.get_indent(), *cond_shrugs, TokenGenerator.get_bool(True), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), TokenGenerator.get_number(5), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), TokenGenerator.get_number(6), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(0), TokenGenerator.get_number(7), TokenGenerator.get_eol()
        ]
        processed = self.process_tokens(tokens)
        expected = [5, 6, 7]
        self.assertEqual(expected, processed)

    def test_simple_false_cond(self):
        tokens = [
            TokenGenerator.get_indent(), *cond_shrugs, TokenGenerator.get_bool(False), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), TokenGenerator.get_number(5), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), TokenGenerator.get_number(6), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(0), TokenGenerator.get_number(7), TokenGenerator.get_eol()
        ]
        processed = self.process_tokens(tokens)
        expected = [7]
        self.assertEqual(expected, processed)

    def test_multiple_cond(self):
        tokens = [
            TokenGenerator.get_indent(), *cond_shrugs, TokenGenerator.get_bool(True), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), TokenGenerator.get_number(5), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(), *cond_shrugs, TokenGenerator.get_bool(True), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), TokenGenerator.get_number(6), TokenGenerator.get_eol()
        ]
        processed = self.process_tokens(tokens)
        expected = [5, 6]
        self.assertEqual(expected, processed)

    def test_nested_cond(self):
        tokens = [
            TokenGenerator.get_indent(), *cond_shrugs, TokenGenerator.get_bool(True), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), TokenGenerator.get_number(5), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), *cond_shrugs, TokenGenerator.get_bool(True), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(2), TokenGenerator.get_number(6), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(2), *cond_shrugs, TokenGenerator.get_bool(True), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(3), TokenGenerator.get_number(7), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(1), *cond_shrugs, TokenGenerator.get_bool(False), TokenGenerator.get_eol(),
            TokenGenerator.get_indent(2), TokenGenerator.get_number(8), TokenGenerator.get_eol(),
        ]
        processed = self.process_tokens(tokens)
        expected = [5, 6, 7]
        self.assertEqual(expected, processed)


if __name__ == '__main__':
    unittest.main()

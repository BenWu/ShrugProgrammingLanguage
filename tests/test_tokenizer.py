import unittest

from shrug_lang import tokenizer
from shrug_lang.tokens import Tokens


class TestLineParser(unittest.TestCase):
    """Line parser class should return correctly read tokens"""

    def test_empty_line(self):
        line = ''
        empty_line = [(Tokens.EOL,)]
        self.assertEqual(empty_line, Tokens.parse_line(line))

        line = '     '
        self.assertEqual(empty_line, Tokens.parse_line(line))

    def test_shrug(self):
        line = '¯\_(ツ)_/¯'
        single_shrug = [(Tokens.SHRUG,), (Tokens.EOL,)]
        self.assertEqual(single_shrug, Tokens.parse_line(line))

    def test_numbers(self):
        line = '2'
        single_number1 = [(Tokens.NUMBER, 2), (Tokens.EOL,)]
        self.assertEqual(single_number1, Tokens.parse_line(line))

        line = '43435356'
        single_number2 = [(Tokens.NUMBER, 43435356), (Tokens.EOL,)]
        self.assertEqual(single_number2, Tokens.parse_line(line))

        line = 'dfs3'
        invalid_id1 = [(Tokens.INVALID, 'dfs3'), (Tokens.EOL,)]
        self.assertEqual(invalid_id1, Tokens.parse_line(line))

        line = 'abc%'
        invalid_id2 = [(Tokens.INVALID, 'abc%'), (Tokens.EOL,)]
        self.assertEqual(invalid_id2, Tokens.parse_line(line))

    def test_ids(self):
        line = 'a'
        single_id1 = [(Tokens.ID, 'a'), (Tokens.EOL,)]
        self.assertEqual(single_id1, Tokens.parse_line(line))

        line = 'variable'
        single_id2 = [(Tokens.ID, 'variable'), (Tokens.EOL,)]
        self.assertEqual(single_id2, Tokens.parse_line(line))

    def test_strings(self):
        line = '""'
        empty_string = [(Tokens.STRING, ''), (Tokens.EOL,)]
        self.assertEqual(empty_string, Tokens.parse_line(line))

        line = '"a"'
        short_string = [(Tokens.STRING, 'a'), (Tokens.EOL,)]
        self.assertEqual(short_string, Tokens.parse_line(line))

        line = '"a bc def gh i jk lmn op q rs tuv wx u y z"'
        long_string = [
            (Tokens.STRING, 'a bc def gh i jk lmn op q rs tuv wx u y z'),
            (Tokens.EOL,)
        ]
        self.assertEqual(long_string, Tokens.parse_line(line))

        line = '"fs\'d\' f" " s " " fd_ f"'
        weird_string = [
            (Tokens.STRING, 'fs\'d\' f'),
            (Tokens.STRING, ' s '),
            (Tokens.STRING, ' fd_ f'),
            (Tokens.EOL,)
        ]
        self.assertEqual(weird_string, Tokens.parse_line(line))

        line = '"a'
        invalid_string = [(Tokens.INVALID, '"a'), (Tokens.EOL,)]
        self.assertEqual(invalid_string, Tokens.parse_line(line))

        line = '"¯\_(ツ)_/¯"'
        shrug_string = [(Tokens.STRING, '¯\_(ツ)_/¯'), (Tokens.EOL,)]
        self.assertEqual(shrug_string, Tokens.parse_line(line))

    def test_complex(self):
        line = ('¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ x ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯'
                ' 4 var "mm" 434')
        tokens = [(Tokens.SHRUG,), (Tokens.ID, 'n'), (Tokens.SHRUG,),
                  (Tokens.ID, 'x'), (Tokens.SHRUG,), (Tokens.SHRUG,),
                  (Tokens.SHRUG,), (Tokens.NUMBER, 4), (Tokens.ID, 'var'),
                  (Tokens.STRING, 'mm'), (Tokens.NUMBER, 434), (Tokens.EOL,)]
        self.assertEqual(tokens, Tokens.parse_line(line))

    def test_join_strings(self):
        # trivial
        self.assertEqual([], Tokens.join_strings([]))
        self.assertEqual([''], Tokens.join_strings(['']))
        # unfinished strings
        self.assertEqual(['"'], Tokens.join_strings(['"']))
        self.assertEqual(['"affsdf'], Tokens.join_strings(['"affsdf']))
        self.assertEqual(['"affsdf abc'],
                         Tokens.join_strings(['"affsdf', 'abc']))
        # proper strings
        self.assertEqual(['"abc"'], Tokens.join_strings(['"abc"']))
        self.assertEqual(['"abc "def ghi"'],
                         Tokens.join_strings(['"abc', '"def', 'ghi"']))
        self.assertEqual(
            ['abc', '3', '"abc "def ghi"', 'hello', "ppp"],
            Tokens.join_strings(
                ['abc', '3', '"abc', '"def', 'ghi"', 'hello', "ppp"]))
        self.assertEqual(
            ['"     "'],
            Tokens.join_strings(['"', '', '', '', '', '"']))


if __name__ == '__main__':
    unittest.main()

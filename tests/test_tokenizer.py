import unittest

from shrug_lang import tokenizer
from shrug_lang.token import Token, Token


class TestLineParser(unittest.TestCase):
    """Line parser class should return correctly read tokens"""

    def test_empty_line(self):
        line = ''
        empty_line = [Token(Token.EOL)]
        self.assertEqual(empty_line, tokenizer.parse_line(line))

        line = '     '
        self.assertEqual(empty_line, tokenizer.parse_line(line))

    def test_shrug(self):
        line = '¯\_(ツ)_/¯'
        single_shrug = [Token(Token.SHRUG), Token(Token.EOL)]
        self.assertEqual(single_shrug, tokenizer.parse_line(line))

    def test_numbers(self):
        line = '2'
        single_number1 = [Token(Token.NUMBER, 2), Token(Token.EOL)]
        self.assertEqual(single_number1, tokenizer.parse_line(line))

        line = '43435356'
        single_number2 = [Token(Token.NUMBER, 43435356), Token(Token.EOL)]
        self.assertEqual(single_number2, tokenizer.parse_line(line))

        line = 'dfs3'
        invalid_id1 = [Token(Token.INVALID, 'dfs3'), Token(Token.EOL)]
        self.assertEqual(invalid_id1, tokenizer.parse_line(line))

        line = 'abc%'
        invalid_id2 = [Token(Token.INVALID, 'abc%'), Token(Token.EOL)]
        self.assertEqual(invalid_id2, tokenizer.parse_line(line))

    def test_ids(self):
        line = 'a'
        single_id1 = [Token(Token.ID, 'a'), Token(Token.EOL)]
        self.assertEqual(single_id1, tokenizer.parse_line(line))

        line = 'variable'
        single_id2 = [Token(Token.ID, 'variable'), Token(Token.EOL)]
        self.assertEqual(single_id2, tokenizer.parse_line(line))

    def test_strings(self):
        line = '""'
        empty_string = [Token(Token.STRING, ''), Token(Token.EOL)]
        self.assertEqual(empty_string, tokenizer.parse_line(line))

        line = '"a"'
        short_string = [Token(Token.STRING, 'a'), Token(Token.EOL)]
        self.assertEqual(short_string, tokenizer.parse_line(line))

        line = '"a bc def gh i jk lmn op q rs tuv wx u y z"'
        long_string = [
            Token(Token.STRING, 'a bc def gh i jk lmn op q rs tuv wx u y z'),
            Token(Token.EOL)
        ]
        self.assertEqual(long_string, tokenizer.parse_line(line))

        line = '"fs\'d\' f" " s " " fd_ f"'
        weird_string = [
            Token(Token.STRING, 'fs\'d\' f'),
            Token(Token.STRING, ' s '),
            Token(Token.STRING, ' fd_ f'),
            Token(Token.EOL)
        ]
        self.assertEqual(weird_string, tokenizer.parse_line(line))

        line = '"a'
        invalid_string = [Token(Token.INVALID, '"a'), Token(Token.EOL)]
        self.assertEqual(invalid_string, tokenizer.parse_line(line))

        line = '"¯\_(ツ)_/¯"'
        shrug_string = [Token(Token.STRING, '¯\_(ツ)_/¯'), Token(Token.EOL)]
        self.assertEqual(shrug_string, tokenizer.parse_line(line))

    def test_complex(self):
        line = ('¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ x ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯'
                ' 4 var "mm" 434')
        tokens = [Token(Token.SHRUG, ), Token(Token.ID, 'n'),
                  Token(Token.SHRUG), Token(Token.ID, 'x'),
                  Token(Token.SHRUG, ), Token(Token.SHRUG),
                  Token(Token.SHRUG), Token(Token.NUMBER, 4),
                  Token(Token.ID, 'var'), Token(Token.STRING, 'mm'),
                  Token(Token.NUMBER, 434), Token(Token.EOL)]
        self.assertEqual(tokens, tokenizer.parse_line(line))

    def test_join_strings(self):
        # trivial
        self.assertEqual([], tokenizer.join_strings([]))
        self.assertEqual([''], tokenizer.join_strings(['']))
        # unfinished strings
        self.assertEqual(['"'], tokenizer.join_strings(['"']))
        self.assertEqual(['"affsdf'], tokenizer.join_strings(['"affsdf']))
        self.assertEqual(['"affsdf abc'],
                         tokenizer.join_strings(['"affsdf', 'abc']))
        # proper strings
        self.assertEqual(['"abc"'], tokenizer.join_strings(['"abc"']))
        self.assertEqual(['"abc "def ghi"'],
                         tokenizer.join_strings(['"abc', '"def', 'ghi"']))
        self.assertEqual(
            ['abc', '3', '"abc "def ghi"', 'hello', "ppp"],
            tokenizer.join_strings(
                ['abc', '3', '"abc', '"def', 'ghi"', 'hello', "ppp"]))
        self.assertEqual(
            ['"     "'],
            tokenizer.join_strings(['"', '', '', '', '', '"']))


if __name__ == '__main__':
    unittest.main()

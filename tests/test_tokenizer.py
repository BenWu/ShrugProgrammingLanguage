import unittest

from shrug_lang.shrug_token import TokenType, Token
from shrug_lang.tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    """Line parser class should return correctly read tokens"""

    def test_empty_line(self):
        line = ''
        self.assertEqual([Token(TokenType.INDENT, 0), Token(TokenType.EOL)],
                         Tokenizer.parse_line(line))

        line = '     '
        self.assertEqual([Token(TokenType.INDENT, 5), Token(TokenType.EOL)],
                         Tokenizer.parse_line(line))

    def test_comment(self):
        line = '# fsd'
        self.assertEqual([Token(TokenType.COMMENT)],
                         Tokenizer.parse_line(line))

        line = ' #'
        self.assertEqual([Token(TokenType.COMMENT)],
                         Tokenizer.parse_line(line))

    def test_shrug(self):
        line = '¯\_(ツ)_/¯'
        single_shrug = [Token(TokenType.INDENT, 0),
                        Token(TokenType.SHRUG),
                        Token(TokenType.EOL)]
        self.assertEqual(single_shrug, Tokenizer.parse_line(line))

    def test_numbers(self):
        line = '2'
        single_number1 = [Token(TokenType.INDENT, 0),
                          Token(TokenType.NUMBER, 2),
                          Token(TokenType.EOL)]
        self.assertEqual(single_number1, Tokenizer.parse_line(line))

        line = '43435356'
        single_number2 = [Token(TokenType.INDENT, 0),
                          Token(TokenType.NUMBER, 43435356),
                          Token(TokenType.EOL)]
        self.assertEqual(single_number2, Tokenizer.parse_line(line))

        line = '-12'
        single_number3 = [Token(TokenType.INDENT, 0),
                          Token(TokenType.NUMBER, -12),
                          Token(TokenType.EOL)]
        self.assertEqual(single_number3, Tokenizer.parse_line(line))

        line = 'dfs3'
        invalid_id1 = [Token(TokenType.INDENT, 0),
                       Token(TokenType.INVALID, 'dfs3'),
                       Token(TokenType.EOL)]
        self.assertEqual(invalid_id1, Tokenizer.parse_line(line))

        line = 'abc%'
        invalid_id2 = [Token(TokenType.INDENT, 0),
                       Token(TokenType.INVALID, 'abc%'),
                       Token(TokenType.EOL)]
        self.assertEqual(invalid_id2, Tokenizer.parse_line(line))

    def test_bool(self):
        line = 'False'
        just_false = [Token(TokenType.INDENT, 0),
                      Token(TokenType.BOOL, False),
                      Token(TokenType.EOL)]
        self.assertEqual(just_false, Tokenizer.parse_line(line))

        line = 'True'
        just_false = [Token(TokenType.INDENT, 0),
                      Token(TokenType.BOOL, True),
                      Token(TokenType.EOL)]
        self.assertEqual(just_false, Tokenizer.parse_line(line))

        line = 'False True True False'
        just_false = [Token(TokenType.INDENT, 0),
                      Token(TokenType.BOOL, False),
                      Token(TokenType.BOOL, True),
                      Token(TokenType.BOOL, True),
                      Token(TokenType.BOOL, False),
                      Token(TokenType.EOL)]
        self.assertEqual(just_false, Tokenizer.parse_line(line))

        line = 'false true'
        just_false = [Token(TokenType.INDENT, 0),
                      Token(TokenType.ID, 'false'),
                      Token(TokenType.ID, 'true'),
                      Token(TokenType.EOL)]
        self.assertEqual(just_false, Tokenizer.parse_line(line))

    def test_ids(self):
        line = 'a'
        single_id1 = [Token(TokenType.INDENT, 0),
                      Token(TokenType.ID, 'a'),
                      Token(TokenType.EOL)]
        self.assertEqual(single_id1, Tokenizer.parse_line(line))

        line = 'variable'
        single_id2 = [Token(TokenType.INDENT, 0),
                      Token(TokenType.ID, 'variable'),
                      Token(TokenType.EOL)]
        self.assertEqual(single_id2, Tokenizer.parse_line(line))

    def test_strings(self):
        line = '""'
        empty_string = [Token(TokenType.INDENT, 0),
                        Token(TokenType.STRING, ''),
                        Token(TokenType.EOL)]
        self.assertEqual(empty_string, Tokenizer.parse_line(line))

        line = '"a"'
        short_string = [Token(TokenType.INDENT, 0),
                        Token(TokenType.STRING, 'a'),
                        Token(TokenType.EOL)]
        self.assertEqual(short_string, Tokenizer.parse_line(line))

        line = '"a bc def gh i jk lmn op q rs tuv wx u y z"'
        long_string = [
            Token(TokenType.INDENT, 0),
            Token(TokenType.STRING, 'a bc def gh i jk lmn op q rs tuv wx u y z'),
            Token(TokenType.EOL)
        ]
        self.assertEqual(long_string, Tokenizer.parse_line(line))

        line = '"fs\'d\' f" " s " " fd_ f"'
        weird_string = [Token(TokenType.INDENT, 0),
                        Token(TokenType.STRING, 'fs\'d\' f'),
                        Token(TokenType.STRING, ' s '),
                        Token(TokenType.STRING, ' fd_ f'),
                        Token(TokenType.EOL)]
        self.assertEqual(weird_string, Tokenizer.parse_line(line))

        line = '"a'
        invalid_string = [Token(TokenType.INDENT, 0),
                          Token(TokenType.INVALID, '"a'),
                          Token(TokenType.EOL)]
        self.assertEqual(invalid_string, Tokenizer.parse_line(line))

        line = '"¯\_(ツ)_/¯"'
        shrug_string = [Token(TokenType.INDENT, 0),
                        Token(TokenType.STRING, '¯\_(ツ)_/¯'),
                        Token(TokenType.EOL)]
        self.assertEqual(shrug_string, Tokenizer.parse_line(line))

    def test_complex(self):
        line = ('¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ x ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯'
                ' 4 var "mm" 434')
        tokens = [Token(TokenType.INDENT, 0),
                  Token(TokenType.SHRUG), Token(TokenType.ID, 'n'),
                  Token(TokenType.SHRUG), Token(TokenType.ID, 'x'),
                  Token(TokenType.SHRUG), Token(TokenType.SHRUG),
                  Token(TokenType.SHRUG), Token(TokenType.NUMBER, 4),
                  Token(TokenType.ID, 'var'), Token(TokenType.STRING, 'mm'),
                  Token(TokenType.NUMBER, 434), Token(TokenType.EOL)]
        self.assertEqual(tokens, Tokenizer.parse_line(line))

    def test_join_strings(self):
        # trivial
        self.assertEqual([], Tokenizer.join_strings([]))
        self.assertEqual([''], Tokenizer.join_strings(['']))
        # unfinished strings
        self.assertEqual(['"'], Tokenizer.join_strings(['"']))
        self.assertEqual(['"affsdf'], Tokenizer.join_strings(['"affsdf']))
        self.assertEqual(['"affsdf abc'],
                         Tokenizer.join_strings(['"affsdf', 'abc']))
        # proper strings
        self.assertEqual(['"abc"'], Tokenizer.join_strings(['"abc"']))
        self.assertEqual(['"abc "def ghi"'],
                         Tokenizer.join_strings(['"abc', '"def', 'ghi"']))
        self.assertEqual(
            ['abc', '3', '"abc "def ghi"', 'hello', "ppp"],
            Tokenizer.join_strings(
                ['abc', '3', '"abc', '"def', 'ghi"', 'hello', "ppp"]))
        self.assertEqual(
            ['"     "'],
            Tokenizer.join_strings(['"', '', '', '', '', '"']))


if __name__ == '__main__':
    unittest.main()

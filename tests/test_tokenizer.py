import unittest

from shrug_lang.tokenizer import LineParser, Tokens


class TestLineParser(unittest.TestCase):
    """Line parser class should return correctly read tokens"""
    def setUp(self):
        self.parser = LineParser()

    def test_empty_line(self):
        line = ''
        empty_line = [(Tokens.EOL,)]
        self.assertEqual(empty_line, self.parser.parse(line))

    def test_shrug(self):
        line = '¯\_(ツ)_/¯'
        single_shrug = [(Tokens.SHRUG,), (Tokens.EOL,)]
        self.assertEqual(single_shrug, self.parser.parse(line))

    def test_numbers(self):
        line = '2'
        single_number1 = [(Tokens.NUMBER, 2), (Tokens.EOL,)]
        self.assertEqual(single_number1, self.parser.parse(line))

        line = '43435356'
        single_number2 = [(Tokens.NUMBER, 43435356), (Tokens.EOL,)]
        self.assertEqual(single_number2, self.parser.parse(line))

        line = 'dfs3'
        invalid_id1 = [(Tokens.INVALID, 'dfs3'), (Tokens.EOL,)]
        self.assertEqual(invalid_id1, self.parser.parse(line))

        line = 'abc%'
        invalid_id2 = [(Tokens.INVALID, 'abc%'), (Tokens.EOL,)]
        self.assertEqual(invalid_id2, self.parser.parse(line))

    def test_ids(self):
        line = 'a'
        single_id1 = [(Tokens.ID, 'a'), (Tokens.EOL,)]
        self.assertEqual(single_id1, self.parser.parse(line))

        line = 'variable'
        single_id2 = [(Tokens.ID, 'variable'), (Tokens.EOL,)]
        self.assertEqual(single_id2, self.parser.parse(line))

    def test_strings(self):
        line = '""'
        empty_string = [(Tokens.STRING, ''), (Tokens.EOL,)]
        self.assertEqual(empty_string, self.parser.parse(line))

        line = '"a"'
        short_string = [(Tokens.STRING, 'a'), (Tokens.EOL,)]
        self.assertEqual(short_string, self.parser.parse(line))

        line = '"a_bc_def_gh_i_jk_lmn_op_q_rs_tuv_wx_u_y_z"'
        long_string = [
            (Tokens.STRING, 'a_bc_def_gh_i_jk_lmn_op_q_rs_tuv_wx_u_y_z'),
            (Tokens.EOL,)
        ]
        self.assertEqual(long_string, self.parser.parse(line))

        line = '"fs\'d\'_f"_"_s_"f"_"fd__f"'
        weird_string = [
            (Tokens.STRING, 'fs\'d\'_f"_"_s_"f"_"fd__f'),
            (Tokens.EOL,)
        ]
        self.assertEqual(weird_string, self.parser.parse(line))

        line = '"a'
        invalid_string = [(Tokens.INVALID, '"a'), (Tokens.EOL,)]
        self.assertEqual(invalid_string, self.parser.parse(line))

        line = '"¯\_(ツ)_/¯"'
        shrug_string = [(Tokens.STRING, '¯\_(ツ)_/¯'), (Tokens.EOL,)]
        self.assertEqual(shrug_string, self.parser.parse(line))

    def test_complex(self):
        line = ('¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ x ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯'
                ' 4 var "mm" 434')
        tokens = [(Tokens.SHRUG,), (Tokens.ID, 'n'), (Tokens.SHRUG,),
                  (Tokens.ID, 'x'), (Tokens.SHRUG,), (Tokens.SHRUG,),
                  (Tokens.SHRUG,), (Tokens.NUMBER, 4), (Tokens.ID, 'var'),
                  (Tokens.STRING, 'mm'), (Tokens.NUMBER, 434), (Tokens.EOL,)]
        self.assertEqual(tokens, self.parser.parse(line))


if __name__ == '__main__':
    unittest.main()

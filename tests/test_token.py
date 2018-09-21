import unittest

from shrug_lang.shrug_token import Token, TokenType


class TestToken(unittest.TestCase):
    """Test token creation"""
    def test_invalid_type(self):
        self.assertRaises(TypeError, Token, 'type')
        self.assertRaises(TypeError, Token, 1)

    def test_mandatory_values(self):
        self.assertRaises(ValueError, Token, TokenType.STRING)
        self.assertRaises(ValueError, Token, TokenType.NUMBER)
        self.assertRaises(ValueError, Token, TokenType.ID)
        self.assertRaises(ValueError, Token, TokenType.INVALID)

    def test_valid_tokens(self):
        Token(TokenType.SHRUG)
        Token(TokenType.NUMBER, 1)
        Token(TokenType.STRING, 'abc')
        Token(TokenType.ID, 'a')
        Token(TokenType.EOL)
        Token(TokenType.INVALID, 'invalid')


if __name__ == '__main__':
    unittest.main()

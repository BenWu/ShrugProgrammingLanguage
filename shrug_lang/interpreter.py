from sys import stderr

from shrug_lang import tokenizer
from shrug_lang.token_parser import TokenError, TokenParser

# ¯\_(ツ)_/¯

if __name__ == '__main__':
    parser = TokenParser()

    while True:
        line = input()
        tokens = tokenizer.parse_line(line)
        try:
            for token in tokens:
                val = parser.next_token(token)
                if val is not None:
                    print(val)
        except TokenError as e:
            print(f'TokenError: {e}', file=stderr)
        except TypeError as e:
            print(f'TypeError: {e}', file=stderr)

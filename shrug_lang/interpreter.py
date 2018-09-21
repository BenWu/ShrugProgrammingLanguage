from sys import stderr

from shrug_lang.token_parser import TokenError, TokenParser
from shrug_lang.tokenizer import Tokenizer

# ¯\_(ツ)_/¯


def start_interpreter():
    parser = TokenParser()

    try:
        while True:
            print('>> ', end='')
            line = input()
            tokens = Tokenizer.parse_line(line)
            try:
                for token in tokens:
                    val = parser.next_token(token)
                    if val is not None:
                        print(val)
            except TokenError as e:
                print(f'TokenError: {e}', file=stderr)
            except TypeError as e:
                print(f'TypeError: {e}', file=stderr)
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == '__main__':
    start_interpreter()

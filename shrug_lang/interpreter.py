from argparse import ArgumentParser
from sys import stderr

from shrug_lang.token_parser import TokenError, TokenParser
from shrug_lang.tokenizer import Tokenizer

# ¯\_(ツ)_/¯

DESCRIPTION = """
Interpreter for Shrug language
"""


def parse_args():
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-q', '--quiet', action='store_true')
    return parser.parse_args()


def start_interpreter():
    args = parse_args()
    parser = TokenParser()
    try:
        while True:
            if not args.quiet:
                print('>> ', end='')
            line = input()
            tokens = Tokenizer.parse_line(line)
            try:
                for token in tokens:
                    val = parser.next_token(token)
                    if val is not None:
                        print(val)
            except (TokenError, ValueError, TypeError, ZeroDivisionError) as e:
                print(f'{type(e).__name__}: {e}', file=stderr)
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == '__main__':
    start_interpreter()

from shrug_lang import tokenizer
from shrug_lang.token_parser import TokenParser

if __name__ == '__main__':
    parser = TokenParser()

    while True:
        line = input()
        tokens = tokenizer.parse_line(line)
        for token in tokens:
            print(token)
            parser.next_token(token)

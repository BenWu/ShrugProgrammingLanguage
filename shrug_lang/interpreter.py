from shrug_lang.tokenizer import Tokenizer

if __name__ == '__main__':
    tokenizer = Tokenizer()

    while True:
        line = input()
        tokens = tokenizer.parse_line(line)
        print(tokens)

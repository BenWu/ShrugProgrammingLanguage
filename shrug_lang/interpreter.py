from shrug_lang import tokenizer

if __name__ == '__main__':
    while True:
        line = input()
        tokens = tokenizer.parse_line(line)
        print(tokens)

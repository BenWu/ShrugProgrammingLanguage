from shrug_lang.tokenizer import LineParser

if __name__ == '__main__':
    parser = LineParser()

    tokens = parser.parse(
        'fadsasfd ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ 34 fd3 3f "fs""da" "fsd"')

    print(tokens)

from typing import List

from shrug_lang.token import Token


def parse_line(line: str):
    unparsed_tokens = filter(None, join_strings(line.split(' ')))
    tokens = [parse_token(unparsed) for unparsed in unparsed_tokens]
    tokens.append(Token(Token.EOL))
    return tokens


def join_strings(unparsed_tokens: List[str]):
    """Join strings that have spaces in them"""
    new_unparsed = []
    reading_string = False
    current_string = []
    for unparsed_token in unparsed_tokens:
        if reading_string:
            if unparsed_token.endswith('"'):
                reading_string = False
                current_string.append(unparsed_token)
                new_unparsed.append(' '.join(current_string))
                current_string.clear()
            else:
                current_string.append(unparsed_token)
        elif (unparsed_token.startswith('"') and
              (len(unparsed_token) == 1 or
               not unparsed_token.endswith('"'))):
            reading_string = True
            current_string.append(unparsed_token)
        else:
            new_unparsed.append(unparsed_token)
    if len(current_string):
        new_unparsed.append(' '.join(current_string))
    return new_unparsed


def parse_token(unparsed_token: str):
    """Get token from given string"""
    if unparsed_token == '¯\_(ツ)_/¯':
        return Token(Token.SHRUG)
    if (len(unparsed_token) >= 2 and
            unparsed_token.startswith('"') and
            unparsed_token.endswith('"')):
        return Token(Token.STRING, unparsed_token[1:-1])
    if unparsed_token.isalpha():
        return Token(Token.ID, unparsed_token)
    if unparsed_token.isnumeric():
        return Token(Token.NUMBER, int(unparsed_token))
    return Token(Token.INVALID, unparsed_token)



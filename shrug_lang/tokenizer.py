from enum import Enum


class Tokens(Enum):
    SHRUG = 1
    NUMBER = 2
    STRING = 3
    ID = 4
    BOF = 5
    EOF = 6
    EOL = 7
    INVALID = 8


class ParserState(Enum):
    EMPTY = 1
    LARM1 = 2
    LARM2 = 3
    LARM3 = 4
    FACE1 = 5
    FACE2 = 6
    FACE3 = 7
    RARM1 = 8
    RARM2 = 9
    RARM3 = 10
    VAL = 11
    ID = 12


class LineParser:
    def parse(self, line: str):
        if len(line) == 0:
            return [(Tokens.EOL,)]
        unparsed_tokens = line.split(' ')
        tokens = list(filter(
            None, [self.parse_token(unparsed) for unparsed in unparsed_tokens]
        ))
        tokens.append((Tokens.EOL,))
        return tokens

    @staticmethod
    def parse_token(unparsed_token: str):
        if unparsed_token == '':
            return None
        if unparsed_token == '¯\_(ツ)_/¯':
            return Tokens.SHRUG,
        if (len(unparsed_token) >= 2 and
                unparsed_token.startswith('"') and
                unparsed_token.endswith('"')):
            # TODO: Handle strings with spaces
            return Tokens.STRING, unparsed_token[1:-1]
        if unparsed_token.isalpha():
            return Tokens.ID, unparsed_token
        if unparsed_token.isnumeric():
            return Tokens.NUMBER, int(unparsed_token)
        return Tokens.INVALID, unparsed_token



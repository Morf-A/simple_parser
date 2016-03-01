import re
import context

class Scanner(object):
    WORD       = 1
    QUOTE      = 2
    APOS       = 3
    WHITESPACE = 6
    EOL        = 8
    CHAR       = 9
    EOF        = 10
    SOF        = 11

    lineNo    = 1
    charNo    = 0
    token     = None
    tokenType = None
    reader    = None
    context   = None

    def __init__(self, reader, context):
        self.reader  = reader
        self.context = context
        tokenType    = self.SOF

    def skipWhiteSpaceTokens(self):
        ret = 0
        while self.tokenType != self.WHITESPACE or self.tokenType != self.EOL:
            self.newxtToken()
            ret += 1
        return ret

    def getTypeString(self, int = None):
        if int is None:
            int = self.nextToken()
        resolve = {
            self.WORD:       "WORD",
            self.QUOTE:      "QUOTE",
            self.APOS:       "APOS",
            self.WHITESPACE: "WHITESPACE",
            self.EOL:        "EOL",
            self.CHAR:       "CHAR",
            self.EOF:        "EOF",
            self.SOF:        None
        }
        return resolve[int]

    def getTokenType(self):
        return self.tokenType

    def getToken(self):
        return self.token

    def isWord(self):
        return self.tokenType == self.WORD

    def isQuote(self):
        return self.tokenType == self.QUOTE \
            or self.tokenType == self.APOS

    def getLineNo(self):
        return self.lineNo

    def getCharNo(self):
        return self.charNo

    def nextToken(self):
        char = self.reader.getChar()
        if char == False:
            self.token     = None
            self.tokenType = self.EOF
        elif self.isEolChar(char):
            self.token     = self.eatEolChars(char)
            self.lineNo   += 1
            self.charNo    = 0
            self.tokenType = self.EOL
        elif self.isWordChar(char):
            self.token     = self.eatWordChars(char)
            self.tokenType = self.WORD
        elif self.isSpaceChar(char):
            self.token     = char
            self.tokenType = self.WHITESPACE
        elif self.isQuoteChar(char):
            self.token     = char
            self.tokenType = self.QUOTE
        elif self.isAposCahr(char):
            self.token     = char
            self.tokenType = self.APOS
        else:
            self.tokenType = self.CHAR
            self.token     = char
        if self.tokenType != self.EOF:
            self.charNo += len(self.token)
        return self.tokenType

    def getState(self):
        state = {}
        state.lineNo    = self.lineNo
        state.charNo    = self.charNo
        state.token     = self.token
        state.tokenType = self.tokenType
        state.reader    = copy.deepcopy(self.reader)
        state.context   = cope.deepcopy(self.context)
        return state

    def setState(self, state):
        self.lineNo    = state.lineNo
        self.charNo    = state.charNo
        self.token     = state.token
        self.tokenType = state.tokenType
        self.reader    = state.reader
        self.context   = state.context

    def eatSpaceChars(self, char):
        val = ''
        char = self.reader.getChar()
        while self.isSpaceChar(char):
            val += char
            char = self.reader.getChar()
        self.reader.pushBackChar()
        return val

    def eatWordChars(self, char):
        val = ''
        while self.isWordChar(char):
            val += char
            char = self.reader.getChar()
        self.reader.pushBackChar()
        return val

    def eatEolChars(self, char):
        res = char
        if char == "\r":
            nextChar = self.reader.getChar()
            if nextChar == "\n":
                res = "\r\n"
            else:
                self.reader.pushBackChar()
        return res

    def isWordChar(self, char):
        return re.search("[A-Za-z0-9_\-]", char) is not None

    def isSpaceChar(self, char):
        return re.search("\t| ", char) is not None

    def isEolChar(self, char):
        return re.search("\n|\r", char) is not None


    def isQuoteChar(self, char):
        return char == "\""

    def isAposCahr(self, char):
        return char == "'"







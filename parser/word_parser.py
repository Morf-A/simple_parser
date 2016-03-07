from abstract_parser import AbstractParser

class WordParser(AbstractParser):

    def __init__(self, word=None):
        super(WordParser, self).__init__()
        self.word = word

    def doScan(self, scanner):
        return scanner.getTokenType() == scanner.WORD and\
            (self.word is None or self.word == scanner.getToken())

    def term(self):
        return True



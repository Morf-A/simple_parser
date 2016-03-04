from abstract_parser import AbstractParser
class CharacterParser(AbstractParser):

    char = None

    def __init__(self, char):
        super(CharacterParser, self).__init__()
        self.char = char

    def doScan(self, scanner):
        return scanner.getToken() == self.char

    def term(self):
        return True



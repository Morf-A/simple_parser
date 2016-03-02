from abstract_parser import AbstractParser
class CharacterParser(AbstractParser):

    char = None

    def __init__(self, char, name=None, respectSpace=False):
        super(CharacterParser, self).__init__(name, respectSpace)
        self.char = char

    def doScan(self, scanner):
        return scanner.getToken() == self.char

    def term(self):
        return True



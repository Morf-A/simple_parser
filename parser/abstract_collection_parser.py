from abstract_parser import AbstractParser

class AbstractCollectionParser(AbstractParser):

    def __init__(self):
        super(AbstractCollectionParser, self).__init__()
        self.parsers = []

    def add(self, *parser_array):
        for parser in parser_array:
            self.parsers.append(parser)

    def term(self):
        return False


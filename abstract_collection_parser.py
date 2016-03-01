import abstract_parser

class AbstractCollectionParser(AbstractParser):
    parsers = []

    def add(self, parser):
        self.parsers.append(parser)

    def term(self):
        return False


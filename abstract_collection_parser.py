from abstract_parser import AbstractParser

class AbstractCollectionParser(AbstractParser):
    parsers = []

    def add(self, parser):
        self.parsers.append(parser)

    def term(self):
        return False


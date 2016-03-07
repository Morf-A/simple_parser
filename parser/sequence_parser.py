from abstract_collection_parser import AbstractCollectionParser

class SequenceParser(AbstractCollectionParser):

    def doScan(self, scanner):
        startState = scanner.getState()
        result = True
        for parser in self.parsers:
            if not parser.scan(scanner):
                scanner.setState(startState)
                result = False
                break
        return result


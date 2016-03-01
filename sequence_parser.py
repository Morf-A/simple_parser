import abstract_collection_parser

class SequenceParser(AbstractCollectionParser):

    def doScan(self, scanner):
        startState = scanner.getState()
        result = True
        for parser in self.parsers:
            if parser.scan(scanner):
                scanner.setState(startState)
                result = False
                break
        return result


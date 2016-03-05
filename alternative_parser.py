from abstract_collection_parser import AbstractCollectionParser

class AltetnativeParser(AbstractCollectionParser):

    def doScan(self, scanner):
        result = False
        state = scanner.getState()
        for parser in self.parsers:
            scanResult = parser.scan(scanner)
            if scanResult:
                result = True
                break
        if not result:
            scanner.setState(state)
        return result

from abstract_collection_parser import AbstractCollectionParser

class RepetitionParser(AbstractCollectionParser):

    def __init__(self, minimum=0, maximum=1):
        super(RepetitionParser, self).__init__()
        if minimum < 0:
            raise Exception("Minimum must be more or equal 0")
        if maximum < 0:
            raise Exception("Minimum must be more or equal 0")
        if minimum > maximum:
            raise Exception("Minimum must be less or equal maximum")
        self.minimum = minimum
        self.maximum = maximum


    def add(self, parser):
        if len(self.parsers) > 1:
            raise Exception('RepetitionParser takes only one parser')
        self.parsers.append(parser)

    def doScan(self, scanner):
        startState = scanner.getState()
        counter = 0
        result  = True
        scanResult = True
        if len(self.parsers) > 0:
            parser = self.parsers[0]
            while counter < self.maximum and scanResult:
                scanResult = parser.scan(scanner)
                counter += 1
            if not scanResult:
                counter -= 1
            if counter < self.minimum:
                scanner.setState(startState)
                result = False
        return result

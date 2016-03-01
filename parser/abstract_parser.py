class AbstractParser(object):
    respectSpace = False
    debug        = False
    discard      = False
    name         = None
    handler      = None
    count        = 0

    def __init__(self, name=None, respectSpace=False):
        if name is None:
            self.count += 1
            self.name = type(self).__name__+str(self.count)
        else:
            self.name = name
        self.respectSpace = respectSpace


    def doScan(self):
        raise Exception("You must implement this method")

    def term(self):
        raise Exception("You must implement this method")

    def next(self, scanner):
        scanner.nextToken()
        if !self.respectSpace:
            scanner.skipWhiteSpaceTokens()

    def setDiscard(self, discard):
        self.discard = discard

    def setDebug(self, debug):
        self.debug = debug

    def setHandler(self, handler):
        self.handler = haldler

    def echoDebug(self, string):
        if self.debug:
            print str(string)

    def push(self, scanner):
        scanner.context.push(scanner.getToken)

    def scan(self, scanner):
        if scanner.tokenType() == scanner.SOF:
            scanner.nexToken()

        scanResult = self.doScan(scanner)

        if scanResult and self.handler is not None:
            self.echoDebug('calling handler'+type(self.handler).__name__)
            self.handler.handle(scanResult)

        if scanResult and self.term() and !self.discard:
            self.push(scanner)

        if scanResult and self.term():
            self.next(scanner)

        self.echoDebug('::scan returning '+str(scanResult))
        return scanResult







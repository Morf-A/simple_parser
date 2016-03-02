class AbstractParser(object):
    def __init__(self, name=None, respectSpace=False):
        self.__discard = False
        self.__handler = None
        self.count     = 0
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
        if not self.respectSpace:
            scanner.skipWhiteSpaceTokens()

    def setDiscard(self, discard):
        self.__discard = discard

    def setHandler(self, handler):
        self.__handler = haldler

    def push(self, scanner):
        scanner.context.append(scanner.getToken())

    def scan(self, scanner):
        if scanner.getTokenType() == scanner.SOF:
            scanner.nextToken()

        scanResult = self.doScan(scanner)

        if scanResult and self.__handler is not None:
            self.__handler.handle(scanResult)

        if scanResult and self.term() and not self.__discard:
            self.push(scanner)

        if scanResult and self.term():
            self.next(scanner)
        print 'token:'+str(scanner.getToken())
        print 'self.term(): '+str(self.term())
        print 'scanResult: '+str(scanResult)
        print ""
        return scanResult







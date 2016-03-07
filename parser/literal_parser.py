from abstract_parser import AbstractParser

class LiteralParser(AbstractParser):

    def push(self, scanner):
        pass

    def doScan(self, scanner):
        result = False;
        string = '';
        quote = scanner.getTokenType();
        if quote == scanner.QUOTE or\
           quote == scanner.APOS:
            result = True
            while True:
                scanner.nextToken();
                if scanner.getTokenType() == scanner.EOF:
                    raise Exception('Unquote '+quote+' unfound')
                if scanner.getTokenType() == quote:
                    break
                string += scanner.getToken()

            if not self.getDiscard():
                scanner.context.append(string)
        return result

    def term(self):
        return True



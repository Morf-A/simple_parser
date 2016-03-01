from scanner import Scanner
from context import Context
from stringreader import Stringreader

context = Context()
reader  = Stringreader("$input equals \"4\" or $input equals 'four'")
#reader  = stringreader("$")
scanner = Scanner(reader, context)

print "token\tcharNo\tsrtingType"
while(scanner.nextToken() != scanner.EOF):
    print scanner.getToken() + "\t" + str(scanner.getCharNo()) + "\t" +scanner.getTypeString(scanner.getTokenType())



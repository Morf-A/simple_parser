from scanner import Scanner
from stringreader import Stringreader

#reader  = Stringreader("$input equals \"4\" or $input equals 'four'")
context = []
reader  = Stringreader("!")
scanner = Scanner(reader, context)

print "token\tcharNo\tsrtingType"
while(scanner.nextToken() != scanner.EOF):
    print scanner.getToken() + "\t" + str(scanner.getCharNo()) + "\t" +scanner.getTypeString(scanner.getTokenType())



from character_parser import CharacterParser
from sequence_parser import SequenceParser
from scanner import Scanner
from context import Context
from stringreader import Stringreader


a = CharacterParser('&')
b = CharacterParser('*')
sec = SequenceParser()
sec.add(a)
sec.add(b)

context = []
reader  = Stringreader("&*")
scanner = Scanner(reader, context)
sec.scan(scanner)

print context

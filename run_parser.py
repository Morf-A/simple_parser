from character_parser import CharacterParser
from sequence_parser import SequenceParser
from scanner import Scanner
from stringreader import Stringreader
from repetition_parser import RepetitionParser

# a = CharacterParser('&')
# b = CharacterParser('*')
# sec = SequenceParser()
# sec.add(a)
# sec.add(b)
# repeat = RepetitionParser(2, 4)
# repeat.add(sec)
# v    = CharacterParser('!')
# sec2 = SequenceParser();
# sec2.add(repeat)
# sec2.add(v)

e = CharacterParser('&')
v = CharacterParser('!')
rep = RepetitionParser(2, 4)
rep.add(v)
sec = SequenceParser()
sec.add(rep, e)


context = []
reader  = Stringreader("!&")
scanner = Scanner(reader, context)
scanResult = sec.scan(scanner)

print context

print('scanResult: ', str(scanResult))

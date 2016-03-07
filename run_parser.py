import sys
sys.path.append("parser")

from character_parser import CharacterParser
from sequence_parser import SequenceParser
from scanner import Scanner
from stringreader import Stringreader
from repetition_parser import RepetitionParser
from alternative_parser import AlternativeParser
from word_parser import WordParser
from literal_parser import LiteralParser

s  = CharacterParser('$')
eq = CharacterParser('=')
s.setDiscard(True)
word = WordParser()
literal = LiteralParser()

sec = SequenceParser()
sec.add(s, word, eq, literal)

context = []
reader  = Stringreader("$string = 'Mama mila ramu'")
scanner = Scanner(reader, context)
scanResult = sec.scan(scanner)

print context

print('scanResult: ', str(scanResult))

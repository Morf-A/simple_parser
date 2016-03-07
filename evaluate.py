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

class Evaluate(object):

    def __init__(self, string):
        self.expression_statement = None
        self.operand_statement    = None
        self.compile(string)

    def compile(self, string):
        context = []
        reader  = Stringreader(string)
        scanner = Scanner(reader, context)
        scanresult = self.expression().scan(scanner)
        print(scanner.context)
        # if not scanresult or scanner.tokenType() != Scanner.EOF:
        #     msg = "\n"
        #     msg += 'line: '  + str(scanner.getLineNo()) + "\n"
        #     msg += 'char: '  + str(scanner.getCharNo()) + "\n"
        #     msg += 'token: ' + str(scanner.getToken())  + "\n"
        #     raise Exception(msg)
        #     self.interpreter = scanner.context.pop()

    def expression(self):
        if self.expression_statement is None:
            self.expression_statement = SequenceParser()
            alt = AlternativeParser()
            alt.add(self.orExpr(), self.andExpr())
            rep = RepetitionParser()
            rep.add(alt)
            self.expression_statement.add(self.operand())
            self.expression_statement.add(rep)
        return self.expression_statement

    def orExpr(self):
        word = WordParser('or')
        word.setDiscard(True)
        sec = SequenceParser()
        sec.add(word, self.operand())
        return sec

    def andExpr(self):
        word = WordParser('and')
        word.setDiscard(True)
        sec = SequenceParser()
        sec.add(word, self.operand())
        return sec

    def eqExpr(self):
        word = WordParser('equals')
        word.setDiscard(True)
        sec = SequenceParser()
        sec.add(word, self.operand())
        return sec

    def operand(self):
        if self.operand_statement is None:
            self.operand_statement = SequenceParser()
            expr_sec = SequenceParser()
            br1 = CharacterParser('(')
            br1.setDiscard(True)
            br2 = CharacterParser('(')
            br2.setDiscard(True)
            expr_sec.add(br1, self.expression(), br2)

            var_sec = SequenceParser()
            char = CharacterParser('$')
            char.setDiscard(True)
            var_sec.add(char, WordParser())
            alt = AlternativeParser()
            alt.add(\
                expr_sec,\
                LiteralParser(),\
                var_sec\
            )

            rep = RepetitionParser()
            rep.add(self.eqExpr())
            self.operand_statement.add(alt, rep)
        return self.operand_statement




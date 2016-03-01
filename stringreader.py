class Stringreader(object):
    __in  = None
    __pos = None
    __len = None

    def __init__(self, string):
        self.__in  = string
        self.__pos = 0
        self.__len = len(string)


    def getChar(self):
        char = False
        if self.__pos < self.__len:
            char = self.__in[self.__pos]
        if self.__pos <= self.__len:
            self.__pos += 1
        return char

    def pushBackChar(self):
        self.__pos -= 1
        if(self.__pos < 0):
            self.__pos = 0




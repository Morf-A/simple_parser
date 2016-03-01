class Context:
    __storage = []

    def push(self, val):
        __storage.append(val)

    def pop(self,val):
        return __storage.pop()

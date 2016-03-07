class Expression:
    value    = None

    def interpret(self):
        pass

    def getValue(self):
        return self.value

    def setValue(self, value=None):
        self.value = value

class LiteralExpression(Expression):

    def __init__(self, value = None):
        self.value = value


class VariableExpression(Expression):
    name  = None

    def __init__(self, name, value=None):
        self.name  = name
        self.value = value

class OperatorExpression(Expression):
    l_expr = None
    r_expr = None

    def __init__(self, l_expr, r_expr):
        self.l_expr = l_expr
        self.r_expr = r_expr

    def doInterpret(self, l_value, r_value):
        pass

    def interpret(self):
        self.l_expr.interpret()
        self.r_expr.interpret()
        l_res = self.l_expr.getValue()
        r_res = self.r_expr.getValue()
        self.setValue(self.doInterpret(l_res, r_res))


class BooleanOrExpression(OperatorExpression):
     def doInterpret(self, l_value, r_value):
        return l_value or r_value

class BooleanAndExpression(OperatorExpression):
    def doInterpret(self, l_value, r_value):
        return l_value and r_value


class BooleanEqualsExpression(OperatorExpression):
    def doInterpret(self, l_value, r_value):
        return l_value == r_value

import expression

def variable_handler(scanner):
    varname = scanner.context.pop()
    scanner.context.append(VariableExpression(varname))

def literal_handler(scanner):
    literal = scanner.context.pop()
    scanner.context.append(LiteralExpression(literal))

def equals_handler(scanner):
    l = scanner.context.pop()
    r = scanner.context.pop()
    scanner.context.append(BooleanEqualsExpression(l, r))

def or_handler(scanner):
    l = scanner.context.pop()
    r = scanner.context.pop()
    scanner.context.append(BooleanOrExpression(l, r))

def and_handler(scanner):
    l = scanner.context.pop()
    r = scanner.context.pop()
    scanner.context.append(BooleanAndExpression(l, r))

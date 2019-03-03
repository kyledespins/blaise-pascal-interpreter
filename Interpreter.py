from Token import *

class Interpreter(object):
    def __init__(self, lexer):
        # client string input, e.g. "3 + 5", "12 - 5 + 3", etc
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """Return an INTEGER token value."""
        token = self.current_token
        self.eat(INTEGER)
        return token.value


    def expr(self):
        """Arithmetic expression parser / interpreter."""
        # set current token to the first token taken from the input
        #self.current_token = self.lexer.get_next_token()

        result = self.factor()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.factor()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.factor()
        while self.current_token.type in (DIVIDE, MULTIPLY):
            token = self.current_token
            if token.type == DIVIDE:
                self.eat(DIVIDE)
                result = result / self.factor()
            elif token.type == MULTIPLY:
                self.eat(MULTIPLY)
                result = result * self.factor()

        return result

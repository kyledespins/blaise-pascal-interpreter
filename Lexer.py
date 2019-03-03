from calc1 import Token
from token_types import *

class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "3 * 5", "12 / 3 * 4", etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        if self.current_char is None:
            return Token(EOF, None) 
        if self.current_char.isspace():
            self.advance()
            return self.get_next_token()

        if self.current_char.isdigit():
            i = None
            while self.current_char is not None and self.current_char.isdigit():
                if i is None:
                    i = int(self.current_char)
                else:
                    i = int(str(i) + str(self.current_char))
                self.advance()
            token = Token(INTEGER, int(i))
            return token

        if self.current_char == '+':
            token = Token(PLUS, self.current_char)
            self.advance()
            return token

        if self.current_char == '-':
            token = Token(MINUS, self.current_char)
            self.advance()
            return token

        if self.current_char == '/':
            token = Token(DIVIDE, self.current_char)
            self.advance()
            return token
            
        if self.current_char == '*':
            token = Token(MULTIPLY, self.current_char)
            self.advance()
            return token
        self.error()

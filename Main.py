from Interpreter import * 
from Lexer import *


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(Lexer(text))
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
import sys
import ply.yacc as yacc
import TreePrinter

from matrix_parser import MatrixParser

if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    MatrixParser = MatrixParser()
    parser = yacc.yacc(module=MatrixParser)
    text = file.read()
    ast = parser.parse(text, lexer=MatrixParser.matrix_lexer)
    print(ast.printTree())


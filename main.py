#!/usr/bin/python
from yyparse.ZCCparser import parser, printAST
from yyparse.ZCClex import lexer as ZCClexer
from symbol.symtab import c_types
from public.ZCCglobal import global_context,FuncType

if __name__ == '__main__':
    # with open("yyparse/missSEMI.c") as f:
    # with open("yyparse/missRightCurly.c") as f:
    # with open("symbol/test.c") as f:
    # with open("symbol/preprocessed.c") as f:
    with open("test/a.c") as f:

        codes = f.read()
        pt = parser.parse(codes, lexer=ZCClexer)
        print "errorCounter=", parser.errorCounter
        printAST(pt)
    print(global_context)



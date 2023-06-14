from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor
from NewVisitor import NewVisitor
import sys

def displayHelp():
    resp=""
    resp+="Hi, this programm attempts to convert asm to c++\n"
    resp+="For it to work you have provide two arguments\n"
    resp+="First argument is the input file name, the asm one\n"
    resp+="The second one is the desired name of the output file\n"
    resp+="Example use would be as follows:\n"
    resp+="python test.asm output.cpp"
    print(resp)

def main():
    if len(sys.argv)==1 or (len(sys.argv)<=2 and sys.argv[1]!="--help") or len(sys.argv)>=4:
        print("please provide valid amount of arguments, --help for help")
        quit()
    
    elif(sys.argv[1]=="--help"):
        displayHelp()
        quit()
    
    try:
        input_file=FileStream(sys.argv[1])
        
    except Exception as e:
        print(e)
        quit()
    output_file_name=sys.argv[2]
    lexer=MyGrammarLexer(input_file)
    stream=CommonTokenStream(lexer)
    parser=MyGrammarParser(stream)
    tree=parser.parse()
    visitor=NewVisitor()
    visitor.visitParse(tree)
    visitor.generateFile(output_file_name)

    

if __name__=='__main__':
    main()





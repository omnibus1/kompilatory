grammar MyGrammar;

parse
   : globalStart textSection (section)* dataSection EOF
   ;

globalStart
   :GLOBALSTART 
   ;

textSection
   :  TEXTSECTIONHEADER 
   ;


section
   :  sectionName':' (instruction)*
   ;

dataSection
   :  DATASECTIONHEADER (definition)*
   ;

definition
   :declaration
   |equdeclaration
   ;

declaration
   :variableName defineDirective (numericValue|stringWithQuotes)
   ;
equdeclaration
   :variableName EQU DOLLAR variableName
   ;

defineDirective
   :DB
   |DW

   ;

stringWithQuotes
   :STRINGWITHQUOTES
   ;

sectionName
   :  VARIABLENAME
   ;

instruction
   :move|syscall|jump|increment|compare
   ;

move
   :MOVEINSTRUCTION register ',' (numericValue|variableName)
   ;

register
   :EAX
   |EBX
   |ECX
   |EDX
   ;

compare
   :COMPARE (register) ',' (numericValue|variableName)
   ;

increment
   : INCREMENT (register|variableName)
   ;

variableName
   :VARIABLENAME
   ;

numericValue
   :HEX_VALUE
   |INT_VALUE
   ;

syscall
   : SYSCALL HEX_VALUE
   ;

jump
   :jumpType sectionName
   ;

jumpType
   :JMP
   |JMP_LESS
   |JMP_GREATER
   |JMP_EQU
   ;


WHITESPACE: [\p{Zs}\t] -> skip;
SYSCALL:'int';
EAX:'eax';
EBX:'ebx';
ECX:'ecx';
EDX:'edx';
INT_VALUE:'0'|[1-9][0-9]*;
HEX_VALUE:'0x'[0-9a-fA-F]*;
MOVEINSTRUCTION:'mov';
DB:'db';
DW:'dw';
JMP:'jmp';
JMP_LESS:'jl';
JMP_GREATER:'jg';
JMP_EQU:'je';
EQU:'equ';
DOLLAR:'$-';
STRINGWITHQUOTES:'"'[a-zA-Z0-9!@#$%^&* ]*'"';
GLOBALSTART:'global _start';
TEXTSECTIONHEADER:'section .text:';
DATASECTIONHEADER:'section .data:';
INCREMENT:'inc';
COMPARE:'cmp';
VARIABLENAME:[a-z_][a-zA-Z_0-9]*;

NEWLINE: ('\r\n' | [\r\n]) -> skip;

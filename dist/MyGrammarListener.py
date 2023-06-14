# Generated from MyGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#parse.
    def enterParse(self, ctx:MyGrammarParser.ParseContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#parse.
    def exitParse(self, ctx:MyGrammarParser.ParseContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#globalStart.
    def enterGlobalStart(self, ctx:MyGrammarParser.GlobalStartContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#globalStart.
    def exitGlobalStart(self, ctx:MyGrammarParser.GlobalStartContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#textSection.
    def enterTextSection(self, ctx:MyGrammarParser.TextSectionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#textSection.
    def exitTextSection(self, ctx:MyGrammarParser.TextSectionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#section.
    def enterSection(self, ctx:MyGrammarParser.SectionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#section.
    def exitSection(self, ctx:MyGrammarParser.SectionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#dataSection.
    def enterDataSection(self, ctx:MyGrammarParser.DataSectionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#dataSection.
    def exitDataSection(self, ctx:MyGrammarParser.DataSectionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#definition.
    def enterDefinition(self, ctx:MyGrammarParser.DefinitionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#definition.
    def exitDefinition(self, ctx:MyGrammarParser.DefinitionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#declaration.
    def enterDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#declaration.
    def exitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#equdeclaration.
    def enterEqudeclaration(self, ctx:MyGrammarParser.EqudeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#equdeclaration.
    def exitEqudeclaration(self, ctx:MyGrammarParser.EqudeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#defineDirective.
    def enterDefineDirective(self, ctx:MyGrammarParser.DefineDirectiveContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#defineDirective.
    def exitDefineDirective(self, ctx:MyGrammarParser.DefineDirectiveContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#stringWithQuotes.
    def enterStringWithQuotes(self, ctx:MyGrammarParser.StringWithQuotesContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#stringWithQuotes.
    def exitStringWithQuotes(self, ctx:MyGrammarParser.StringWithQuotesContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#sectionName.
    def enterSectionName(self, ctx:MyGrammarParser.SectionNameContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#sectionName.
    def exitSectionName(self, ctx:MyGrammarParser.SectionNameContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#instruction.
    def enterInstruction(self, ctx:MyGrammarParser.InstructionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#instruction.
    def exitInstruction(self, ctx:MyGrammarParser.InstructionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#move.
    def enterMove(self, ctx:MyGrammarParser.MoveContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#move.
    def exitMove(self, ctx:MyGrammarParser.MoveContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#register.
    def enterRegister(self, ctx:MyGrammarParser.RegisterContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#register.
    def exitRegister(self, ctx:MyGrammarParser.RegisterContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#compare.
    def enterCompare(self, ctx:MyGrammarParser.CompareContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#compare.
    def exitCompare(self, ctx:MyGrammarParser.CompareContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#increment.
    def enterIncrement(self, ctx:MyGrammarParser.IncrementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#increment.
    def exitIncrement(self, ctx:MyGrammarParser.IncrementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#variableName.
    def enterVariableName(self, ctx:MyGrammarParser.VariableNameContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#variableName.
    def exitVariableName(self, ctx:MyGrammarParser.VariableNameContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#numericValue.
    def enterNumericValue(self, ctx:MyGrammarParser.NumericValueContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#numericValue.
    def exitNumericValue(self, ctx:MyGrammarParser.NumericValueContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#syscall.
    def enterSyscall(self, ctx:MyGrammarParser.SyscallContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#syscall.
    def exitSyscall(self, ctx:MyGrammarParser.SyscallContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#jump.
    def enterJump(self, ctx:MyGrammarParser.JumpContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#jump.
    def exitJump(self, ctx:MyGrammarParser.JumpContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#jumpType.
    def enterJumpType(self, ctx:MyGrammarParser.JumpTypeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#jumpType.
    def exitJumpType(self, ctx:MyGrammarParser.JumpTypeContext):
        pass



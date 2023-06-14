# Generated from MyGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#parse.
    def visitParse(self, ctx:MyGrammarParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#globalStart.
    def visitGlobalStart(self, ctx:MyGrammarParser.GlobalStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#textSection.
    def visitTextSection(self, ctx:MyGrammarParser.TextSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#section.
    def visitSection(self, ctx:MyGrammarParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#dataSection.
    def visitDataSection(self, ctx:MyGrammarParser.DataSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#definition.
    def visitDefinition(self, ctx:MyGrammarParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#declaration.
    def visitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#equdeclaration.
    def visitEqudeclaration(self, ctx:MyGrammarParser.EqudeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#defineDirective.
    def visitDefineDirective(self, ctx:MyGrammarParser.DefineDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#stringWithQuotes.
    def visitStringWithQuotes(self, ctx:MyGrammarParser.StringWithQuotesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#sectionName.
    def visitSectionName(self, ctx:MyGrammarParser.SectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#instruction.
    def visitInstruction(self, ctx:MyGrammarParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#move.
    def visitMove(self, ctx:MyGrammarParser.MoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#register.
    def visitRegister(self, ctx:MyGrammarParser.RegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#compare.
    def visitCompare(self, ctx:MyGrammarParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#increment.
    def visitIncrement(self, ctx:MyGrammarParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#variableName.
    def visitVariableName(self, ctx:MyGrammarParser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#numericValue.
    def visitNumericValue(self, ctx:MyGrammarParser.NumericValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#syscall.
    def visitSyscall(self, ctx:MyGrammarParser.SyscallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#jump.
    def visitJump(self, ctx:MyGrammarParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#jumpType.
    def visitJumpType(self, ctx:MyGrammarParser.JumpTypeContext):
        return self.visitChildren(ctx)



del MyGrammarParser
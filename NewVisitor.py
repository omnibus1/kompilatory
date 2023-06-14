from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor
from collections import defaultdict

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class NewVisitor(MyGrammarVisitor):

    def __init__(self):
        self.variables=[]
        self.eax=None
        self.ebx=None
        self.ecx=None
        self.edx=None
        self.curr_scope=None
        self.body=""
        self.compared={}
        self.scopeDict={"_start":"\t"}
        self.section={}
        self.jumpFrom={}
        self.sectionOrder=[]
        self.stack=[]
        self.code=""

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
        # if self.curr_scope=="_start"
        self.curr_scope=ctx.sectionName().getText()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#dataSection.
    def visitDataSection(self, ctx:MyGrammarParser.DataSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#definition.
    def visitDefinition(self, ctx:MyGrammarParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#declaration.
    def visitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        
        is_string=ctx.stringWithQuotes()
        if is_string:
            var_name=ctx.variableName().getText()
            str_value=is_string.getText()
            self.variables.append(f"std::string {var_name}={str_value};")

            return 
        is_numeric=ctx.numericValue()
        if is_numeric:
            var_name=ctx.variableName().getText()
            num_value=is_numeric.getText()
            self.variables.append(f"int {var_name}={num_value};")

            return
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#equdeclaration.
    def visitEqudeclaration(self, ctx:MyGrammarParser.EqudeclarationContext):
        is_equ=ctx.variableName()
        if is_equ:
            var_name=is_equ[0].getText()
            second_var=is_equ[1].getText()
            self.variables.append(f"int {var_name}={second_var}.length();")

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#defineDirective.
    def visitDefineDirective(self, ctx:MyGrammarParser.DefineDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#stringWithQuotes.
    def visitStringWithQuotes(self, ctx:MyGrammarParser.StringWithQuotesContext):
        return ctx.getText()


    # Visit a parse tree produced by MyGrammarParser#sectionName.
    def visitSectionName(self, ctx:MyGrammarParser.SectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#instruction.
    def visitInstruction(self, ctx:MyGrammarParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#move.
    def visitMove(self, ctx:MyGrammarParser.MoveContext):
        is_register=ctx.register()
        if is_register:
            register=is_register.getText()
            is_numeric=ctx.numericValue()
            if is_numeric:
                num_value=ctx.numericValue().getText()
                self.moveValueIntoRegister(register,num_value)

            else:
                var_value=ctx.variableName().getText()
                self.moveVariableIntoRegister(register,var_value)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#register.
    def visitRegister(self, ctx:MyGrammarParser.RegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#compare.
    def visitCompare(self, ctx:MyGrammarParser.CompareContext):
        
        
        reg=ctx.register().getText()
        is_numeric=ctx.numericValue()
        if is_numeric:
            num=is_numeric.getText()
            self.compared={reg:num}
        else:
            var=ctx.variableName().getText()
            self.compared={reg:var}

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#increment.
    def visitIncrement(self, ctx:MyGrammarParser.IncrementContext):
        register=ctx.register().getText()

        value=self.valueAtRegister(register)

        self.section[self.curr_scope]+=f"{self.scopeDict[self.curr_scope]}{value}+=1;\n"

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#variableName.
    def visitVariableName(self, ctx:MyGrammarParser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#numericValue.
    def visitNumericValue(self, ctx:MyGrammarParser.NumericValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#syscall.
    def visitSyscall(self, ctx:MyGrammarParser.SyscallContext):
        hex=ctx.HEX_VALUE().getText()
        if hex=="0x80":
            if self.eax=="0x4":#0x4 stands for sout
                if self.curr_scope!="_start":
                    self.section[self.curr_scope]+=f"{self.scopeDict[self.curr_scope]}std::cout<<{self.ecx}<<\"\\n\";\n"
                else:
                    self.body+=f"{self.scopeDict[self.curr_scope]}std::cout<<{self.ecx}<<\"\\n\";\n"

        # print(self.section)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#jump.
    def visitJump(self, ctx:MyGrammarParser.JumpContext):
        

        
        jump_section_name=ctx.sectionName().getText()
        if jump_section_name!="exit":
            
            if self.curr_scope!=jump_section_name:
                
                jump_type=ctx.jumpType().getText()
                reg=list(self.compared.keys())[0]
                self.createSectionStart(jump_section_name,reg,jump_type)
                # print(self.section)

        
        sec_name=ctx.sectionName().getText()
        if sec_name!="exit":
            self.scopeDict[sec_name]=self.scopeDict[self.curr_scope]+"\t"
        

        if self.curr_scope not in self.jumpFrom:
            self.jumpFrom[self.curr_scope]=[sec_name]
        else:
            self.jumpFrom[self.curr_scope].append(sec_name)

        return self.visitChildren(ctx)
    


    def createSectionStart(self,section_name,reg,jump_type):
        value_in_reg=self.valueAtRegister(reg)
        if jump_type=="jl":
            self.section[section_name]=f"{self.scopeDict[self.curr_scope]}if({value_in_reg}<{self.compared[reg]})"+"{\n"
        elif jump_type=="jg":
            self.section[section_name]=f"{self.scopeDict[self.curr_scope]}if({value_in_reg}>{self.compared[reg]})"+"{\n"
        elif jump_type=="je":
            self.section[section_name]=f"{self.scopeDict[self.curr_scope]}if({value_in_reg}=={self.compared[reg]})"+"{\n"
        else:
            print("jump not supported yet")

    

    def visitJumpType(self, ctx:MyGrammarParser.JumpTypeContext):
        return self.visitChildren(ctx)

    def moveValueIntoRegister(self,register,value):
        if register=="eax":
            self.eax=value

        elif register=="ebx":
            self.ebx=value

        elif register=="edx":
            self.edx=value

        else:
            self.ecx=value

        

    def moveVariableIntoRegister(self,register,variable):
        if register=="eax":
            self.eax=variable

        elif register=="ebx":
            self.ebx=variable

        elif register=="edx":
            self.edx=variable

        else:
            self.ecx=variable

    def preorder(self,section):
        if section!="exit":
            self.sectionOrder.append(section)
            if section!="_start":
                if section in self.jumpFrom[section]:
                    self.code+=self.section[section].replace("if","while")
                else:
                    self.code+=self.section[section]
            for s in self.jumpFrom[section]:
                if s!=section:
                    self.preorder(s)

            if section!="_start":
                self.code+=self.scopeDict[section]+"}\n"
        




    def declareVariables(self):
        return "\n\t".join(self.variables) 

    def generateFile(self,output_file_name):
        self.preorder("_start")
        res="#include <iostream>\nint main(){\n\t"
        res+=self.declareVariables()+"\n"
        res+=self.body
        res+=self.code
        res+="\n\treturn 0;\n\t}"
        try:
            if not output_file_name.endswith(".cpp"):
                output_file_name+=".cpp"
            f=open(output_file_name,"w")
            f.write(res)
            f.close()
        except Exception as e:
            print(e)


    def valueAtRegister(self,reg):

        if reg=="eax":
            return self.eax
        elif reg=="ebx":
            return self.ebx
        elif reg=="ecx":
            return self.ecx
        else:
            return self.edx


del MyGrammarParser
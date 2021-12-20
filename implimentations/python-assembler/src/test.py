import ast
import codegen
import dict_ksm
def main():
    myast = ast.ksm_ast()
    myast.parse("""
            mov
            m0x1
            m0x2
            loop:
            dec
            m0x1
            second_loop:
            mov
            m0x1
            10
            jmp
            loop
            inc m0xFF
            jmpnz second_loop""")
    myast.tokenize(dict_ksm.d)
    mycodegen = codegen.codegenerator(myast)
    mycodegen.gencode_ksm()
main()

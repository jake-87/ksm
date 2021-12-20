import ast
import codegen
import dict_ksm
import sys
def main():
    myast = ast.ksm_ast()
    file = ""
    debug = False
    try:
        file = sys.argv[1]
    except:
        print("File must be first arg.")
    try:
        debug = sys.argv[2]
    except:
        pass
    with open(file) as f:
        data = f.read()
    myast.parse(data)
    myast.tokenize(dict_ksm.d, debug)
    mycodegen = codegen.codegenerator(myast)
    mycodegen.gencode_ksm(debug)
main()

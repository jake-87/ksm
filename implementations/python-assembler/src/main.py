import ast
import codegen
import dict_ksm
import sys
import io
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
    with io.open(file, "r", encoding="utf8") as f:
        data = f.read()
    myast.parse(data)
    myast.tokenize(dict_ksm.d, debug)
    mycodegen = codegen.codegenerator(myast)
    ret = mycodegen.gencode_ksm(debug)
    print(ret)
main()

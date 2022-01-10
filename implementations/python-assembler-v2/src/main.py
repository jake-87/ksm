import sys
import io
import assemble
def main():
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
    print(file, debug)
    print(data)
    assemble.generate_bin(data)
main()

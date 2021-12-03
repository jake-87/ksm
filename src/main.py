import parse
import sys
def main(argv):
    print(argv)
    debug = 0
    memory = 16
    try:
        file = argv[1]
        try:
            debug = argv[2]
        except:
            pass
        try:
            memory = int(argv[3])
        except:
            pass
    except:
        
        print("No file provided. Try python3 main.py <ksm file>")
        exit(1)
    parse.parse(file, debug, memory)
if __name__ == "__main__":
    main(sys.argv)

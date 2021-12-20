import re
class ast():
    # Simple AST representation
    def __init__(self):
        self.ast = []
    def parse(self, mstr, splits = [" ", "\n", "\t", "\r"]):
        ast = re.split(str("|".join(splits)), mstr)
        new_ast = [elem for elem in ast if elem.strip()]
        self.ast = new_ast
    def get(self):
        return self.ast
    def set(self, ast):
        self.ast = ast

class ksm_ast(ast):
    # KSM AST
    def __init__(self):
        super()
        self.tokenized = []
        self.lablere = re.compile("^[^\:]+:")
    def get_tok(self):
        return self.tokenized
    def tokenize(self, dict, debug = False):
        # Tokenise into sub arrays, based on a dict with format:
        # { "Token": #number_of_args }
        # EG:
        # { "mov": 2 }
        i = 0
        ast = self.get()
        while 1:
            tok = ast[i]
            # Lables match the RE, eg: "lable:"
            if tok in dict or self.lablere.match(tok):
                tmp = []
                tok_len = dict[tok] + 1 if not self.lablere.match(tok) else 1
                k = 0
                tok_len_cpy = tok_len
                while tok_len:
                    tok = ast[i + k].replace(",", "")
                    tmp.append(tok)
                    tok_len -= 1
                    k += 1
                i += tok_len_cpy
                self.tokenized.append(tmp)
            if i >= len(ast):
                break
        if debug:
            print("Tokenized:", self.tokenized)

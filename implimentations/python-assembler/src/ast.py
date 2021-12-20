import re
class ast():
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
    def __init__(self):
        super()
        self.tokenized = []
        self.lablere = re.compile("^[^\:]+:")
    def get_tok(self):
        return self.tokenized
    def tokenize(self, dict):
        i = 0
        ast = self.get()
        while 1:
            tok = ast[i]
            if tok in dict or self.lablere.match(tok):
                tmp = []
                tok_len = dict[tok] + 1 if not self.lablere.match(tok) else 1
                k = 0
                while tok_len:
                    tok = ast[i + k]
                    tmp.append(tok)
                    tok_len -= 1
                    k += 1
                self.tokenized.append(tmp)
            i += 1
            if i >= len(ast):
                break
        print("Tokenized:", self.tokenized)

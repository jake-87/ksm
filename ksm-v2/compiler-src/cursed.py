def evil(tok):
    # We don't talk about this file.
    try:
        a = tok[0]
        try:
            b = tok[1]
            try:
                c = tok[2]
            except IndexError:
                c = ""
        except IndexError:
            b = ""
            try:
                c = tok[2]
            except IndexError:
                c = ""
    except IndexError:
        a = ""
        try:
            b = tok[1]
            try:
                c = tok[2]
            except IndexError:
                c = ""
        except IndexError:
            b = ""
            try:
                c = tok[2]
            except IndexError:
                c = ""
    return (a, b, c)
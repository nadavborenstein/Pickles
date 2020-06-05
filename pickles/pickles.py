# Made by Nadav Borenstein

import pickle


def dump(obj, fp, protocol=None, *, fix_imports=True):
    with open(fp, "wb") as file:
        pickle.dump(obj, file, protocol=protocol, fix_imports=fix_imports)


def load(fp, *, fix_imports=True, encoding="ASCII", errors="strict"):
    with open(fp, "rb") as file:
        obj = pickle.load(file, fix_imports=fix_imports, encoding=encoding, errors=errors)
    return obj
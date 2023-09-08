def vallidate_input(msg: str, obj: type):
    ok = False
    out = None
    while not ok:
        raw = input(msg)
        try:
            if obj == bool:
                lower_raw = raw.lower()
                if lower_raw == "false" or lower_raw == "no":
                    out = False
                elif lower_raw == "0" or lower_raw == "no":
                    out = False
                else:
                    out = True
            else:
                out = obj(raw)
            ok = True
        except ValueError:
            pass
    return out


if __name__ == "__main__":
    x = vallidate_input("Enter number\n", int)
    print(x)
    y = vallidate_input("Enter boolean\n", bool)
    print(y)

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
                    ok = True
                elif lower_raw == "0" or lower_raw == "no":
                    out = False
                    ok = True
                else:
                    out = True
            elif obj == list:
                if raw in obj:
                    out = True
                    ok = True
                else:
                    out = False
            else:
                out = obj(raw)
                ok = True
        except ValueError:
            pass
    return out


if __name__ == "__main__":
    pass
    # x = vallidate_input("Enter number\n", int)
    # print(x)
    # y = vallidate_input("Enter boolean\n", bool)
    # print(y)
    # x = input("enter\n")
    # if x.startswith("0"):
    #     print("NO 0!!!")
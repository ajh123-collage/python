from typing import Any


def vallidate_input(msg: str, obj: type) -> Any:
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
                    ok = True
            elif isinstance(obj, list):
                if raw in obj:
                    out = raw
                    ok = True
                else:
                    out = False
            else:
                out = obj(raw)
                ok = True
        except ValueError:
            pass
    return out


def validate_range(msg: str, minVal: int, maxVal: int) -> int:
    val = vallidate_input(msg, int)
    if val >= minVal and val <= maxVal:
        return val
    else:
        return validate_range(msg, minVal, maxVal)


if __name__ == "__main__":
    pass
    # x = vallidate_input("Enter number\n", int)
    # print(x)
    # y = vallidate_input("Enter boolean\n", bool)
    # print(y)
    # x = input("enter\n")
    # if x.startswith("0"):
    #     print("NO 0!!!")
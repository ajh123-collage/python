x = "A"

def test(a):
    match a:
        case "A":
            return 1
        case "B":
            return 2
        case "U" | "XYZ" | "ASDA":
            return 0
        case (q, w):
            print(q, w)
            return 3
        case _:
            return 0
        
y = test(x)
print(y)

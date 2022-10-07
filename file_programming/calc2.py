sum = input("enter sum")

in_add = sum.split("+")
in_mul = sum.split("*")
in_div = sum.split("/")
in_take = sum.split("-")

if len(in_add) > 1:
    print(int(in_add[0])+int(in_add[1]))
elif len(in_mul) > 1:
    print(int(in_mul[0])*int(in_mul[1]))
elif len(in_div) > 1:
    print(int(in_div[0])/int(in_div[1]))
elif len(in_take) > 1:
    print(int(in_take[0])-int(in_take[1]))

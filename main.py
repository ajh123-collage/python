def func1(self):
    print("func 1")

class1 = type("class1", (), {"func2": func1})


x = class1()
x.func2()

class class2:
    def func2(self):
        print("func 1")

z = class2()
z.func2()
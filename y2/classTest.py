def goodbye(self):
    print("world")


Test = type("test", (object,), {
    "hello": goodbye
})

me = Test()

me.hello()

print(me.__dict__)
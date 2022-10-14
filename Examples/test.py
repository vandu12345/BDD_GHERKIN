from re import X


x=6

def func1():
    # x=5
    def func2():
        # x=7
        print(x)
    func2()
    # print(x)

func1()
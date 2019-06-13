x=7
y=8.5
print(x+y)
print(type(x))

def fun(x):
    '函数的功能描述'
    a=2
    print("i am in fun")
    return

fun(3)

class obj:
    '类的功能描述'
    a=2
    def fun(self):
        print("i am in obj.fun")
        
o=obj()
o.fun()
print(o.__doc__)
print(obj.__doc__)
print(fun.__doc__)
#内置函数及模块
print(dir())
print(obj.__dir__)
print(dir(fun))

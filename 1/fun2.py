# funkcja wewnętrzna
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    print(fun2)
    return fun2  # zwrócenie adresu funkcji fun2, referencji


fun1()
print(fun1)  # <function fun1.<locals>.fun2 at 0x0000016EA2D29E40>
print(type(fun1))  # <class 'function'>
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000002313DB09E40>
print(type(xFun))
xFun()  # To jest fun2

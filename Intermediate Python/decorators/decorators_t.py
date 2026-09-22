def decorator_test(func):
    def wrapper(*args,**kwargs):
        print(f"{args}")
        print(f"{kwargs}")

        result = func(*args,**kwargs)

        print (f"{result}")
        return result
    return wrapper


@decorator_test
def sum(a,b,c):
    return a + b + c

@decorator_test
def hello(name, hello="Hola"):
    return f"{hello}, {name}!"

sum(5,10,4)

hello("fenlir")
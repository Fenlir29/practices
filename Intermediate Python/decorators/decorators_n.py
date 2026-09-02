def check_if_num(func):
    def wrapper(*args, **kwargs):
        for i in args :
            if not isinstance(i,(int,float)):
                raise TypeError("solo se permiten numeros")

        for i in kwargs.values():
            if not isinstance(i,(int,float)):
                raise TypeError("solo se permiten numeros")
        
        return func(*args, **kwargs)
    return wrapper

@check_if_num
def sum(a,b):
    return a + b

# print(sum(50,"fenlir"))

# print(sum(50,10))



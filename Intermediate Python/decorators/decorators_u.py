from datetime import date

class user():
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth


    @property
    def age(self):
        today = date.today()

        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day
        ):
            age -= 1

        return age

def check_age(func):
    def wrapper(*args, **kwargs):

        user = args[0]

        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad")

        return func(*args, **kwargs)

    return wrapper

@check_age
def legal_age(user):
    print("mayor de edad")

fenlir = user(date(1999, 5, 20))

rilenf = user(date(2020, 5, 20))

legal_age(fenlir)

# legal_age(rilenf)
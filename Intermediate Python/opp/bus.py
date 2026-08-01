class Person():
	def __init__(self, name):
		self.name = name
		self.age = 0
		


class Bus:
    def __init__(self,max_passagers):
         self.max_passagers = max_passagers
         self.passengers = []

    def add_passagers(self,person):
        if self.max_passagers > len(self.passengers):
            self.passengers.append(person)
        else:
            print("El bus esta lleno")

    

    def remove_passagers(self,person):
        if len(self.passengers) == 0:
            print("no hay pasajeros ")
        else:
            self.passengers.remove(person)


isaac = Person("isaac")
juan = Person("Juan")
ana = Person("Ana")
bus_test = Bus(2)

bus_test.add_passagers(isaac)
bus_test.add_passagers(juan)
bus_test.add_passagers(ana) 
bus_test.remove_passagers(isaac)
for person in bus_test.passengers:
    print(person.name)
class Patient:

    def __init__(self,name,age):
        self.__name=name
        self.age=age

    def display(self):
        print("Patient:", self.__name)
        print("Age:", self.age)


class Doctor(Patient):

    def __init__(self,name,age,specialization):
        super().__init__(name,age)
        self.specialization=specialization

    def show(self):
        self.display()
        print("Specialization:", self.specialization)


p1=Patient("Padma",23)

d1=Doctor(
"Rajesh",
40,
"Cardiology"
)

print("\nPatient Object")
p1.display()

print("\nDoctor Object")
d1.show()

class Car:
    company=0
    price=0
    color=0
    def details(self):
        print("company",self.company)
        print("price",self.price)
        print("color",self.color)
print("CAR1")
car1=Car()
car1.company="Maruthi"
car1.price=500000
car1.color="Blue"
car1.details()

print("CAR 2")
car2=Car()
car2.company="Swift"
car2.price=700000
car2.color="White"
car2.details()


print("CAR3")
car3=Car()
car3.company="Alto"
car3.price=900000
car3.color="indigo"
car3.details()

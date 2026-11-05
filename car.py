

# class Car:
    

#     def __init__(self, make, model, year,color):
    
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color



#     # def drive (self):
#     #     print ("This "+self.model+" is driving")

#     # def stop (self):
#     #     print ("this car has stopped")

# car_1 = Car ("Ford","Mustang",2023, "Black")

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_1.drive()
# car_1.stop()

# class Animal:
#     alive = True

#     def eat(self):
#         print ("This animal is eating")

#     def sleep (self):
#         print ("This animal is sleeping")

# class Rabbit (Animal):
#     def run (self):
#         print ("This rabbit is running")

# class Fish (Animal):
#     def swim (self):
#         print ("This fish is swimming")

# class Bird (Animal):
#     def fly (self):
#         print ("This bird is flying")

# rabbit= Rabbit()
# fish= Fish()
# bird= Bird()

# # print(rabbit.alive)
# # fish.eat()
# # bird.sleep()

# rabbit.run()
# fish.swim ()
# bird.fly ()

class Car:
    def __init__(self, cc: int, hp: float, color: str, brand:str):

        self.cc = cc
        self.hp = hp
        self.color = color
        self.brand = brand
        
    def present_car (self):
        return f"the car is {self.brand} with name and has hp {self.hp}"

    def improve_hp(self, extra_hp):
        self.hp += extra_hp
        return self.present_car()

rafails_car= Car (cc=1500, hp= 150, color= "black", brand = "VW")
presenter_rafails_car= rafails_car.present_car()
print(presenter_rafails_car)
new_presenter= rafails_car.improve_hp(extra_hp=30)
print(new_presenter)
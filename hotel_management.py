

class Person:
    """
    Describe the hotel's management system

    Args: 
    Name: the name of the person
    age: the age of the person 

    returns : str 
     the name and the age of each person
    
    """

    def __init__(self, name:str, age: int):

       self.name= name
       self.age= age 
        
    def get_details(self):
        print (f"Person with name {self.name} is {self.age} years old")

class Guest(Person):

    """
    Inherits from Person but with 2 additional attributes

    Args:
        room_number: int --> The guest’s assigned room. 
        nights: int-->  The number of nights the guest will stay. 

    """
    def __init__ (self, name:str, age:int, room_number: int, nights : int):
        super().__init__(name,age)

        self.room_number= room_number
        self.nights= nights
    
    def get_details (self):
            super().get_details ()
            print (f"Room number is: {self.room_number} and nights he/she stayed at the hotel is/are: {self.nights}")

    def calculate_bill (self, rate_per_night):
        self.rate_per_night = rate_per_night

        total_bill = self.nights * self.rate_per_night
        return total_bill

class Staff (Person):

        """
        Inherits from Person but with 2 additional attributes

        Args:   position: The job title of the staff member 
                salary: The staff member’s salary
        
        """
        def __init__ (self, name:str, age:int, position:str, salary: float):
            self.position= position 
            self.salary = salary
            super().__init__(name,age)
        def get_details (self):
            super().get_details ()
            print (f"The job title of the staff member is {self.position} and earns {self.salary} euros")

        def give_raise (self,amount):
            self.salary = self.salary + amount

class Hotel:
    """
    this class manages guests and staff

    Args: 
        name: The hotel’s name. 
        guests: A list to store guests. 
        staff: A list to store staff members.
    """

    def __init__ (self, name: str, guests: list | None=None, staff: list | None=None):
        self.name = name
        self.guests = guests
        self.staff = staff

    def check_in (self, guest):
        self.guests.append(guest)

    def check_out (self,guest):
        self.guests.remove(guest)

    def hire_staff (self, member):
        self.staff.append (member)

    def list_guests (self):
        for guest in self.guests:
            print (guest.name)

    def list_staff (self):
        for member in self.staff:
            print (member.name)

#erotima 1   
 
guest1= Guest (name= "Alexandra", age= 34, room_number= 145, nights= 3)
guest1.get_details ()

guest2= Guest ('Giorgos', 54, 203, 5)
guest3= Guest ('Maria', 25, 713, 2)
guest4= Guest ('Mitsos', 36, 512, 3)
guest2.get_details ()
guest3.get_details ()
guest4.get_details ()

staff1= Staff (name= "Makis", age= 42, position= "Floor Manager", salary= 3500)
staff1.get_details()

#erotima 2


guest2.get_details ()
print (guest2.room_number)
print (guest2.nights)

#erotima 3
hotel= Hotel ("Hilton",[],[])
hotel.check_in(guest1)
hotel.check_in(guest2)
hotel.check_in(guest3)
hotel.check_in(guest4)
hotel.list_guests()

hotel.hire_staff (staff1)
hotel.list_staff ()
print ("=========================")


#erotima 4

hotel.check_out(guest1)
hotel.list_guests()

staff2= Staff (name= "Alekos", age= 40, position= "Receptionist", salary= 2500)
staff2.give_raise(300)
staff2.get_details ()

#erotima 5
print ("---------------------------------")

print ("The final list of Guests is:")
hotel.list_guests()

print ("The final list of staff is:")
hotel.list_staff ()
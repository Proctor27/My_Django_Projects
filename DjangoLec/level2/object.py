"""class Cat():
    #CLASS OBJECT ATTRIBUTES
    species = 'mammal'
    def __init__(self,breed,name): #Attributes
        self.breed = breed
        self.name = name

mycat = Cat(breed="OrangeCat",name="Garfield")
print(mycat.breed,mycat.name,mycat.species)
"""

"""class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
    #Calculate the Area
    def area(self):
        return self.radius*self.radius *Circle.pi
    #Function to change the Radius
    def new_radius(self,new_rad):
        self.radius = new_rad

mycircle = Circle(3)
mycircle.new_radius(1000)
print(mycircle.area())"""

"""#INHEIRTANCE 
class Animal():

    def __init__(self,Name):
        print(Name,":Created")
    def whoAMI(self):
        print("Animal")
    def eat(self):
        print("eating")

class Cat(Animal):
    def __init__(self,Name):
       # Animal.__init__(self)
        self.Name = Name
        print(Name,":Created")
    def Meow(self):
        print("Meow")
#reaper = Animal()
Birds = Cat(Name="cat")
Birds.whoAMI()
Birds.eat()
Birds.Meow()"""


#SPECIAL METHODS
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        #STRING METHOD
    def __str__(self):
        return("Title: {}, Author: {}, Pages:{}".format(self.title,self.author,self.pages))
        #LENGTH METHOD
    def __len__(self):
        return self.pages
    #DELETE METHOD
    def __del__(self):
        print("a book was destroyed!")

Fire = Book("python","jose",33)
del Fire
# it is just simple example of OOP / inheritance and using self rather than traditional attributes name evrytime we make a function



class City:
    def __init__(self,name,location,population):
        self.name = name
        self.location = location
        self.population = population

    def get_weather_data( self):
        pass

    def display(self):
        print(f"Name: {self.name}, Location: {self.location}  Population: {self.population}")

class Capital(City):
    def __init__ (self,name, location, population, government):
        super().__init__(name,location,population)
        self.government = government

    def Government_Type(self):
        pass

    def Display_gov(self):
        super().display()
        print(f"GovernmentType :{self.government}")


# NewCity1 = City("newwyork" , "UnitedStates",200000000)
# NewCity2 = City("california" , "UnitedStates",240000000)
# NewCity3 = City("NewJersey" , "UnitedStates",100000000)
# NewCity1.display()
# NewCity2.display()
# NewCity3.display()
newCapital1 = Capital("newwyork" , "UnitedStates",200000000, "Republican")
newCapital1.Display_gov() 
newCapital1.display()
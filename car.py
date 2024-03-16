

class Fahrzeug:
    
    def __init__(self, anzahlRaeder: int):
        self.anzahlRaeder: str = anzahlRaeder
        
    def fahren(self):
        print(f"Das Fahrzeug fährt auf {self.anzahlRaeder} Rädern.")


class Car(Fahrzeug):
   
   # This is the constructor
    def __init__(self, make: str, model: str, year: int, color: str, anzahlRaeder: int):
        # This is the constructor of the parent class
        super().__init__(anzahlRaeder)

        self.make: str = make
        self.model: str = model
        # These are private attributes and are immutable
        self.__year: int = year
        self.__color: str = color

    @property
    def year(self):
        return self.__year
    
    @property
    def color(self):
        return self.__color

    # This is the string representation of the object
    # how to call it: print(car_1)        
    def __repr__(self) -> str:
        return f"{self.make} {self.model} {self.year} {self.color}"

    def drive(self):
        print("This " + self.model + " is driving!")

    def stop(self):
        print("This " + self.model + " is stopped!")      

    def age(self, current_year):
        return current_year - self.year

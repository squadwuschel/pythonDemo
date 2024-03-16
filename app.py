from car import Car
import random


acronymes = {
    "LOL": "Laughing Out Loud",
    "OMG": "Oh My God", 
    "WTF": "What The F***", 
    "BRB": "Be Right Back",
    "TTYL": "Talk To You Later" }

try:
  print(acronymes["LUL"])
except:
  print("LUL not found in dictionary") 
finally:
  print("Finally block is executed")

## Wenn der Key nicht existiert, wird None zurückgegeben
definitionOmg = acronymes.get("OMG")
if definitionOmg:
    print(definitionOmg)
else:
    print("OMG not found")

for key, value in acronymes.items():
    print(f"{key} = {value}")

for key in acronymes:
    print(f"{key} = {acronymes[key]}")


acronymes = ["LOL", "OMG", "WTF", "BRB", "TTYL"]

lolIsInList = "LOL" in acronymes
print(f"LOL is in list: {lolIsInList}")

randomValue = random.randint(1,12)
print(f"Random Value: {randomValue}")

def drucken():
    print("Hallo Welt")

car_1 = Car("Toyota", "Corolla", 2015, "Red", 4)
print(car_1)
car_1.model = "Corolla S"
car_1.__color = "Black"
print(car_1)
car_1.fahren()

car_1.drive()

car_2 = Car("Toyota", "Camry", 2018, "Blue", 2)
print(car_2)
car_2.stop()    
car_2.fahren()

drucken()


def divison(a: int, b: int) -> float:
    if(b == 0):
        raise Exception("b cannot be 0")

    return a / b
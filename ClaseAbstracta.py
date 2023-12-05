#animal es mi clase como va a tener un metodo abstracto , toda la clase se vuelve abstacta
#ademas para hacerlo abstracto tiene que Heredar de abc y importar el decorador AbstracMethod
#Esto es para hacer la clase abstracta
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre ,color) -> None:
        self.nombre=nombre,
        self.color=color


    @abstractmethod
    def Comer(self):
        pass #pass porque no va a hacer una accion , como es abstracto las otras clases son las que implementan





class Perro(Animal):
    
    def __init__(self, nombre, color, raza) -> None:
        super().__init__(nombre, color)
        self.nombre=nombre
        self.color=color
        self.raza=raza

    def Comer(self):
        print("Estoy comiendo comida para perro") 


 #Ahora se crean instancia de las clases que hacen la implementacion
perro = Perro("Jaime","negro","Lobo Siberiano")
perro.Comer()        
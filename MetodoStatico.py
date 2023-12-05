#Los metodos estaticos son de clase asi como las variables estaticas , y no reciben como parametro el self

class Estatica:
    def __init__(self) -> None:
        pass


    #Para hacer el metodo estatico utilizamos el decorador @staticMethod

    @staticmethod
    def metodo_estatico():
        print("Hola , soy un metodo estatico")

#Para llamar al metodo es con el nombre de la clase asi como con las variables estaticas

Estatica.metodo_estatico()

# los métodos estáticos se utilizan cuando la función está asociada con la clase 
# pero no necesita acceder ni modificar el estado de la instancia ni de la clase.
# No pueden acceder a los atributos ni métodos
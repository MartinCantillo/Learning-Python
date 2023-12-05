#los métodos de clase se utilizan cuando necesitas acceder a la clase y
# posiblemente modificar atributos de clase,

#Se utiliza el decorador classmethod y al metodo en ves de pasarse un self  se le pasa un cls( de clase)
class MetodoClase:

    valor="Primer valor"
    def __init__(self) -> None:
        pass


    #Para hacer el metodo estatico utilizamos el decorador @staticMethod

    @classmethod
    def metodo_clase(cls):
       cls.valor="segundo "
       return cls.valor

# Crear una instancia de la clase (si es necesario)
instancia = MetodoClase()

# Llamar al método de clase
resultado = instancia.metodo_clase()  # o MetodoClase.metodo_clase()

# Imprimir el resultado
print(resultado)
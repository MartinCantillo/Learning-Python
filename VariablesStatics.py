#las variables estaticas son de la clase y no van dentro de ningun metodo y se declaran al principio de la clase
#ademas se accede a ella atraves del nombre de la clase 

#para contar las instancias de la clase
class MiClase:
    contador_instancias = 0

    def __init__(self):
        MiClase.contador_instancias += 1

# Uso
obj1 = MiClase()
obj2 = MiClase()

print(MiClase.contador_instancias) 
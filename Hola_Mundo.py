def myFuncion(**diccionarios):
    for clave , valor in diccionarios.items():
        print(f'Clave : {clave} , Valor : {valor}')

myFuncion(titulo='Ingeniero de sistemas', profesion =' desarrollador Full Stack')

lista=[2,3,4,5]

print(7 in lista)

lista.append(7)
print(7 in lista)

#para eliminar un objeto o atributo se le pone del +nombreAtributo por ejemplo del edad

class Persona:
    def __init__(self, nombre , apellido) :
        self._nombre=nombre,
        self._apellido =apellido

     #get se debe colocar properti y el metodo debe ser llamado como el atributo el _ del atributo significa que es privado pero se puede acceder 
     #osea el _ en la variable es para que el programador vea que es privado pero ya con el get y set si el lenguaje lo vuelve privado
     #cuando son metodos de clase osea de instancias de clase a metodo se le coloca siempre el self , asi como en el constructor
    @property
    def nombre(self):
        return self._nombre
    
    #se le coloca al decorador primero el nombre del atributo .setter en el metodo y se le pasa el self y el nombre o atributo
    @nombre.setter
    def nombre(self ,nombre):
        self._nombre=nombre
    #para eliminar el objeto es con del (metodo de clase)

    def __del__(self):
        print(f'persona {self.nombre} eliminada')    
  



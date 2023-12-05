#from +nombre del archivo import* ##ahi importa todo de ese modulo o de ese archivo como clases etc  
class Persona:
    def __init__(self, nombre , apellido) :
        self.nombre=nombre
        self.apellido=apellido
    #to String de java aqui es el __str__, para mostrar informacion de la clase
    def __str__(self) -> str: #la flecha -> str es como una prediccion de lo que va a arrojar el metodo osea el return de tipo str
        return f"Nombre : {self.nombre}, Apellido {self.apellido}"    





#herencia hay que inicializar el constructor del padre en la clase hija con el super
#tambien se deben incializar en el constructor hijo
#en parentesis se le coloca el nombre de las clases padres(Herencia multiple )
class Trabajador(Persona):
    #pass
    def __init__(self, nombre, apellido, sueldo):
        super().__init__(nombre, apellido)#inicializando la clase padre
        self.nombre=nombre
        self.apellido=apellido
        self.sueldo=sueldo
    
    #para heredar algun metodo del padre es con el super, voy hacer el __str__ y con el super heredo
    def __str__(self) -> str:
        return f" {super().__str__()} , Sueldo : {self.sueldo}"




#ahora creamos el objeto de la clase hijo , asi se crea el objeto , nombre de la varibale = clase()
trabajador=Trabajador(nombre="Martin" ,apellido="Cantillo",sueldo=590000000)     

print(f'trabajador : {trabajador.nombre} , Apellido : {trabajador.apellido} , Sueldo : {trabajador.sueldo}')
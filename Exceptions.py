#la superclase de las excepciones es baseExcepcition y la hija es Exception y luego esta tiene mas hijas
try:
  a= int(input("Ingrese un numero"))
  b= int(input("Ingrese un numero"))
  resultado=a/b
  #se crea el objeto Exception y se renombra siempre(asi lo vamos a encontrar ) con 2 y se imprime la exception
  #el except es como el catch en java
except Exception as e:
  print(f"ocurrio un error {e}")  

#el else es cuando el try funciona correctamente que no tira excepcione
else:
    print(f"El codigo funciona correctamente ,  Resultado{resultado}")

#en finally siempre se va a ejecutar independientemente si se lanza o no una exception
finally:
   print("ejecucion bloque finally")    
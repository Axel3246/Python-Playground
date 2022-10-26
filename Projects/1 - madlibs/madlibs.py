'''
# Concatenación de Strings

# Supón que queremos crear un string que diga "suscribete a ______"
youtuber = "Axel"

# Algunas formas de crear y concatenar strings
print("suscribite a " + youtuber)
print("suscribete a {}".format(youtuber))
print(f"suscribete a {youtuber}")
'''

adj = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")
rock = input("Verbo: ")

# f significa f-string (nueva forma de concatenar)

madlib = f"La programación es {adj}! La verdad esta chido \
ya que me gusta mucho {verb1}. Hidratate y {verb2} como {rock}!"
    
print(madlib)


'''

Mi reto: Crear una colección de 4 madlibs y hacer que el usuario 
elija cual quiere utilizar

'''
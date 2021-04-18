import json
import glob
lista_personas = []
loop = True
while loop == True:

    option = int(
        input('\nSeleccione una opción\n1-Nuevo dato\n2-Listar todos\n3-Listar uno\n4-Editar uno\n5-Salir\n'))

    if option == 1:
        cont = 0
        name = input('Nombre:\n')
        age = int(input('Edad:\n'))
        study = bool(input('Esudia:\n'))
        sex = input('Sexo:\n')
        dict = {
            'name': name,
            'age': age,
            'study': study,
            'sex': sex
        }
        lista_personas.append(dict)
        f = open(str(cont)+".txt", "w+")
        f.write(json.dumps(dict))
        f.close()

    if option == 2:

        files = glob.glob("*.txt")
        for i in range(0, len(files)):
            file = open(str(i)+".txt", "r")
            dic = file.readline()
            print(dic)
            file.close()

    if option == 3:
        num = input('Inserte ID a leer:\n')
        try:
            name = glob.glob(num+".txt")
        except IOError:
            print('El archivo no existe')
        file = open(name[0], "r")
        dic = file.readline()
        print(dic)
        file.close()

    if option == 4:
        num = input('Inserte ID a leer:\n')
        name = input('Nombre:\n')
        age = int(input('Edad:\n'))
        study = bool(input('Esudia:\n'))
        sex = input('Sexo:\n')
        dict = {
            'name': name,
            'age': age,
            'study': study,
            'sex': sex
        }
        f = open(str(num)+".txt", "w+")
        f.write(json.dumps(dict))
        f.close()
if option == 4:
    loop = False

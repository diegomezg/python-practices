lista_personas = []
loop = True
lista_personas.append({
    'name': 'Diego',
    'age': 22,
    'study': True,
    'sex': 'M'
})
lista_personas.append({
    'name': 'Diego',
    'age': 22,
    'study': True,
    'sex': 'M'
})
lista_personas.append({
    'name': 'Diego',
    'age': 22,
    'study': True,
    'sex': 'M'
})
lista_personas.append({
    'name': 'Diego',
    'age': 22,
    'study': True,
    'sex': 'M'
})
while loop == True:

    option = int(
        input('Seleccione una opción\n1-Nuevo dato\n2-Listar\n3-Salir\n'))

    if option == 1:
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

    if option == 2:
        initial = int(input('Seleccione primer elemento a enlistar:\n'))
        final = int(input('Seleccione ultimo elemento a enlistar:\n'))

        for i in range(initial-1,final):
            print(lista_personas[i])

    if option == 3:
        loop=False
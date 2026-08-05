import random
lista_colores = [
    "Rojo",
    "Azul",
    "Verde",
    "Amarillo",
    "Naranja",
    "Morado",
    "Blanco",
    "Negro",
    "Gris",
    "Celeste"
]
ids = []
nombres = []
categorias = []
colores = []
responsables = []
prioridades = []
estados = []
fechas = []
observaciones = []
#-----------------------------------------#
#--|menu_principal_asignador_de_colores|--#
#-----------------------------------------#
while True:
    print("menu principal asignador de colores")
    print("1) registrar elemento")
    print("2) editar elemento")
    print("3) eliminar elemento")
    print("4) buscar elemento")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------------#
    #--|registrar_elemento|--#
    #------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_elemento = 1
        else:
            id_elemento = ids[-1] + 1
        nombre = input("nombre: ")
        categoria = input("categoría: ")
        color = random.choice(lista_colores)
        responsable = input("responsable: ")
        prioridad = input("prioridad (alta, media, baja): ")
        estado = input("estado (activo o inactivo): ")
        fecha = input("fecha de registro: ")
        observacion = input("observación: ")
        ids.append(id_elemento)
        nombres.append(nombre)
        categorias.append(categoria)
        colores.append(color)
        responsables.append(responsable)
        prioridades.append(prioridad)
        estados.append(estado)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("elemento registrado correctamente.")
        print("id:", id_elemento)
        print("color asignado:", color)
    #---------------------#
    #--|editar_elemento|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("editar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {colores[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("color:", colores[posicion])
                nombres[posicion] = input("nuevo nombre: ")
                categorias[posicion] = input("nueva categoría: ")
                respuesta = input("¿reasignar color automáticamente? (s/n): ")
                if respuesta.upper() == "S":
                    colores[posicion] = random.choice(lista_colores)
                responsables[posicion] = input("nuevo responsable: ")
                prioridades[posicion] = input("nueva prioridad: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("elemento actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_elemento|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("eliminar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {colores[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del elemento")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("color:", colores[posicion])
                respuesta = input("¿desea eliminar este elemento? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    colores.pop(posicion)
                    responsables.pop(posicion)
                    prioridades.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    print("elemento eliminado correctamente.")
                else:
                    print("el elemento no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_elemento|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("buscar elemento")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("categoría:", categorias[posicion])
                print("color:", colores[posicion])
                print("responsable:", responsables[posicion])
                print("prioridad:", prioridades[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            activos = 0
            inactivos = 0
            rojo = 0
            azul = 0
            verde = 0
            amarillo = 0
            naranja = 0
            morado = 0
            blanco = 0
            negro = 0
            gris = 0
            celeste = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {colores[i]} | {estados[i]}")
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "inactivo":
                    inactivos += 1
                if colores[i] == "Rojo":
                    rojo += 1
                elif colores[i] == "Azul":
                    azul += 1
                elif colores[i] == "Verde":
                    verde += 1
                elif colores[i] == "Amarillo":
                    amarillo += 1
                elif colores[i] == "Naranja":
                    naranja += 1
                elif colores[i] == "Morado":
                    morado += 1
                elif colores[i] == "Blanco":
                    blanco += 1
                elif colores[i] == "Negro":
                    negro += 1
                elif colores[i] == "Gris":
                    gris += 1
                elif colores[i] == "Celeste":
                    celeste += 1
            print("estadísticas asignador de colores")
            print("cantidad de registros:", len(ids))
            print("activos:", activos)
            print("inactivos:", inactivos)
            print("rojo:", rojo)
            print("azul:", azul)
            print("verde:", verde)
            print("amarillo:", amarillo)
            print("naranja:", naranja)
            print("morado:", morado)
            print("blanco:", blanco)
            print("negro:", negro)
            print("gris:", gris)
            print("celeste:", celeste)
            posicion = random.randint(0, len(ids) - 1)
            print("registro seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("categoría:", categorias[posicion])
            print("color:", colores[posicion])
            print("responsable:", responsables[posicion])
            print("prioridad:", prioridades[posicion])
            print("estado:", estados[posicion])
            print("fecha:", fechas[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el asignador de colores.")
        break
    else:
        print("opción no válida.")
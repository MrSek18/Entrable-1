def menu_principal():
    while True:
        os.system("cls")
        print("Menu de Opciones")
        print("1. Crear")
        print("2. Buscar")
        print("3. Editar")
        print("4. Eliminar")
        print("5. Listar")
        print("6. Salida")
        opcion= int(input("Selcciona ima opcion : "))

        if opcion==1:
            crear_Contacto()
            time.sleep(2)
        elif opcion==2:
            buscar_Contacto()
            time.sleep(2)
        elif opcion==3:
            editar_Contacto()
            time.sleep(2)
        elif opcion==4:
            eliminar_Contacto()
            time.sleep(2)
        elif opcion==5:
            listar_Contactos()
            time.sleep(4)
        elif opcion==6:
            print("Salir del Programa")
            break
        else:
            print("Opcion no válida!! intente de nuevo [1,2,3,4,5,6]")
            time.sleep(1)

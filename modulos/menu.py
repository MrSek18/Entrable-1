
import os
from agregar import crear_contacto
from editar import editar_contacto
from mostrar import buscar_contacto, mostrar_contactos
from quitar import eliminar_contacto


def menu_principal():
        os.system("cls")  # Limpia la pantalla para mejorar la legibilidad del menú
        print("Menu de Opciones")
        print("1. Crear contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar contactos")
        print("6. Salir")
        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            crear_contacto()
        elif opcion == 2:
            buscar_contacto()
        elif opcion == 3:
            editar_contacto()
        elif opcion == 4:
            eliminar_contacto()
        elif opcion == 5:
            mostrar_contactos()
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción no válida! Intente de nuevo [1, 2, 3, 4, 5, 6]")

if __name__ == "__main__":
    menu_principal()
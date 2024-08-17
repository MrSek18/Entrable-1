from contactos import datos
from contactos import  guardar_datos

def buscar_id():
    id = input("Ingresa el id: ")
    return id


def editar_contacto():
    id_contacto= buscar_id()
    
    for Contacto in datos["contactos"]:
        if Contacto["id_contacto"] == id_contacto:
            print("Editar datos del Contacto")
            Contacto["nom"]=input("Nombres   : ")
            Contacto["ape"]=input("Apellidos : ")
            Contacto["fn"]=input("Ingresa la fecha de cumpleaños en formato DD/MM/AA: ")
            Contacto["num"]=input("Número telefónico : ")
            Contacto["email"]=input("Email : ")
            Contacto["ec"]=input("Estado civil : ")
            Contacto["oa"]=input("Ocupacion actual : ")
            guardar_datos(datos)
            print()
            print("---Datos actualizados---")
            print(f'Nombres y apellidos: {Contacto["nom"]}, {Contacto["ape"]}')
            print(f'Fecha de nacimiento: {Contacto["fn"]}')
            print(f'Número telefónico: {Contacto["num"]}')
            print(f'Email: {Contacto["email"]}')
            print(f'Estado Civil: {Contacto["ec"]}')
            print(f'Ocupación actual: {Contacto["oa"]}')

        

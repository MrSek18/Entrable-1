from contactos import Contacto
from contactos import  datos
from contactos import  guardar_datos


def crear_contacto():
    nom=input("Ingresa Nombres : ")
    ape=input("Ingresa Apellidos : ")
    fn=input("Ingresa la fecha de cumpleaños en formato DD/MM/AA: ")
    num=input("Ingresa el numero telefónico : ")
    email=input("Digite el email: ")
    ec=input("Ingresa el estado civil: ")
    oa=input("Ingresa la ocupación actual : ")    

    nc=Contacto(nom, ape, fn, num, email, ec, oa)
    
    datos["contactos"].append(nc.__dict__)
    
    guardar_datos(datos)

        
    print("*"*35)
    print(f'El contacto {nc.nom} | {nc.ape} | {nc.fn} | {nc.num} | {nc.email} | {nc.ec} | {nc.oa} ')
    print(f'Este es su ID generado {nc.id_contacto} ')



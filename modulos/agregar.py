from contactos import Contacto
from contactos import Lista_Contactos


def crear_Contacto():
    nom=input("Ingresa Nombres : ")
    ape=input("Ingresa Apellidos : ")
    fn=input("Ingresa la fecha de cumpleaños en formato DD/MM/AA: ")
    num=input("Ingresa el numero telefónico : ")
    email=input("Digite el email: ")
    ec=input("Ingresa el estado civil: ")
    oa=input("Ingresa la ocupación actual : ")    

    nc=Contacto(nom, ape, fn, num, email, ec, oa)
    Lista_Contactos.append(nc)

    print("*"*35)
    print(f'El contacto {nc.nom} | {nc.ape} | {nc.fn} | {nc.num} | {nc.email} | {nc.ec} | {nc.oa} ')
    print(f'Este es su ID generado {nc.id_contacto} ')


crear_Contacto()
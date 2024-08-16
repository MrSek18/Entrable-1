from contactos import Lista_Contactos

def buscar_Contacto():
    id_con=input("Ingresa el ID del Contacto : ")

    for con in Lista_Contactos:
        if con.id_contacto == id_con:
            print("Contacto Encontrado")
            print(f'Nombre y Apellidos: {con.nom} {con.ape}')
            print(f'Fecha de nacimiento: {con.nom} {con.ape}')
            print("Apellidos y Nombres : " + con.apellidos + " , " + con.nombres)
            print("Sueldo              : " + str(con.sueldo))            
            return con                                               
    
    print("Contacto no Existe!!!")
    return None

def listar_Contactos():
    print("")
    print("*"*70)
    print("{:6}{:<15}{:<15}{:<10}{:>10}".format("ID", "Nombres", "Apellidos", "Area","Sueldo"))
    print("*"*70)

    areas_dic={1:"Producción",2:"Administrativo",3:"Sistemas"}

    for con in Lista_Contactos:
        print("{:6}{:<15}{:<15}{:<10}{:>10.2f}".format(con.id_con, con.nombres, con.apellidos, areas_dic[con.area],con.sueldo))

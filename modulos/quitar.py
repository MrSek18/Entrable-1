from contactos import Lista_Contactos

def eliminar_Contacto():
    id_=input("Ingresa el ID del Contacto : ")
    for emp in Lista_Contactos:
        if emp.id_emp==id_:
            print("Contacto Encontrado")
            print("Apellidos y Nombres : " + emp.apellidos + " , " + emp.nombres)
            print("Sueldo              : " + str(emp.sueldo))
            Lista_Contactos.remove(emp)
            
            return                                                
    
    print("Contacto no Existe!!!")
    return 
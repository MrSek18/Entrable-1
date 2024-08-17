from contactos import datos, guardar_datos

def eliminar_contacto():
    id=input("Ingresa el ID del Contacto : ")
    encontrado = False
    for con in datos["contactos"]:
        if con["id_contacto"] == id:
            print("Contacto Encontrado")
            datos["contactos"].remove(con)
            guardar_datos(datos)
            print("Usuario eliminado exitosamente")
            encontrado = True
            break                                                
        
    if not encontrado:
        print("El contacto no existe")
        

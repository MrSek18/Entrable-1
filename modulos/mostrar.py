from contactos import cargar_datos

datos = cargar_datos()


def buscar_contacto():
    id_con=input("Ingresa el ID del Contacto : ")
    for con in datos["contactos"]:
        if con["id_contacto"] == id_con:
            print("Contacto Encontrado")
            print(f'Nombre y Apellidos: {con["nom"]}, {con["ape"]} ')
            print(f'Fecha de nacimiento: {con["fn"]}')
            print(f'Número telefónico: {con["num"]}')
            print(f'email: {con["email"]} ')
            print(f'Estado civil: {con["ec"]}')
            print(f'Ocupacion actual: {con["oa"]}')
            return con                                               
    
    print("¡El contacto no existe!")
    return None

def mostrar_contactos():
    print("Lista de contactos actuales")
    print("*"*27)
    for con in datos.get("contactos",[]):
        print(
            f'{con.get("id_contacto", "")} \n Nombre: {con.get("nom","")} \n Apellido: {con.get("ape","")} \n Fecha de nacimiento: {con.get("fn","")} \n Numero telefónico: {con.get("num","")} \n Email: {con.get("email","")} \n Estado civil: {con.get("ec","")} \n Ocupacion actual: {con.get("oa","")} \n'
        )
        

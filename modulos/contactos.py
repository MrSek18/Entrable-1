import os
import json

archivo_json = "usuarios.json"

def cargar_datos():
    if os.path.exists(archivo_json):
        with open(archivo_json, "r") as archivo:
            try:
                datos = json.load(archivo)
                return datos
            except json.JSONDecodeError:
                return {"contactos": []}
    else:
        return {"contactos": []}

# Guardar los datos en el archivo JSON
def guardar_datos(datos):
    with open(archivo_json, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Inicializa la lista de contactos
datos = cargar_datos()

# Verifica el contador
contador_contactos = int(datos.get("contactos", [{}])[-1].get("id_contacto", "000")) if datos["contactos"] else 0


class Contacto:
    def __init__(self, nom, ape, fn, num, email, ec, oa):
        global contador_contactos
        contador_contactos += 1
        self.id_contacto = f"{contador_contactos:03d}"  
        self.nom = nom
        self.ape = ape
        self.fn = fn
        self.num = num
        self.email = email
        self.ec = ec
        self.oa = oa









            





    















    



















    

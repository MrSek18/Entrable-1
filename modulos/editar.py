from mostrar import buscar_Contacto

def editar_Contacto():
    Contacto= buscar_Contacto()
    if Contacto:
        print("Editar datos del Contacto")
        Contacto.nombres=input("Nombres   : ")
        Contacto.apellidos=input("Apellidos : ")
        print()

        print("1.Producción\n2.Administrativo\n3.Sistemas")
        Contacto.area=int(input("Area [1,2,3] : "))
        Contacto.sueldo=Contacto.calcular_sueldo_base(Contacto.area)
        
        print("*** Dato Actualizados ***")
        print("Apellidos y Nombres : " + Contacto.apellidos + " , " + Contacto.nombres)
        print("Sueldo              : " + str(Contacto.sueldo))



import sys
import os

# Agrega la carpeta 'modulos' al sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modulos'))

# Ahora importa el menú
from modulos.menu import menu_principal

if __name__ == "__main__":
    menu_principal()

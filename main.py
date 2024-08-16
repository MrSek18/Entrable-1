
import importlib
import pkgutil
import modulos

def cargar_todos_los_modulos(package):
    package_dir = package.__path__
    package_name = package.__name__

    for _, module_name, _ in pkgutil.iter_modules(package_dir):
        full_module_name = f"{package_name}.{module_name}"
        importlib.import_module(full_module_name)

cargar_todos_los_modulos(modulos)





modulos.menu_principal()


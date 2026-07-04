# Carpeta: servicios | Archivo: restaurante.py

# Importamos la clase padre para manejar la lista general de productos
from modelos.producto import Producto

class Restaurante:
    def __init__(self, nombre_local: str):
        """
        Clase de servicio que administra el catálogo completo del restaurante.
        """
        self.nombre_local: str = nombre_local
        # REQUISITO: Lista para almacenar los productos registrados
        self.catalogo_productos: list[Producto] = []

    def registrar_producto(self, nuevo_producto: Producto):
        """Método para agregar cualquier Platillo o Bebida al catálogo."""
        self.catalogo_productos.append(nuevo_producto)
        print(f"✅ Registrado con éxito: {nuevo_producto.nombre}")

    def mostrar_menu_completo(self):
        """
        REQUISITO: Demostrar POLIMORFISMO.
        Recorremos la lista llamando a mostrar_informacion(). Cada objeto
        actuará de forma diferente según sea un Platillo o una Bebida.
        """
        print(f"\n==========================================================================")
        print(f"       🍔 MENÚ DIGITAL - {self.nombre_local.upper()} 🍔")
        print(f"==========================================================================")
        
        if not self.catalogo_productos:
            print("El catálogo está vacío actualmente.")
        else:
            for producto in self.catalogo_productos:
                # Aquí ocurre el Polimorfismo en tiempo de ejecución
                producto.mostrar_informacion()
                
        print(f"==========================================================================\n")
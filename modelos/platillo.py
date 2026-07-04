# Carpeta: modelos | Archivo: platillo.py

# REQUISITO: Importar la clase padre para poder heredar
from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre: str, precio_inicial: float, tiempo_preparacion: int):
        """
        Clase hija Platillo que hereda de Producto.
        tiempo_preparacion: int -> Atributo propio (minutos que demora el chef).
        """
        # REQUISITO: Uso de super() para reutilizar el constructor del padre
        super().__init__(nombre, precio_inicial)
        self.tiempo_preparacion: int = tiempo_preparacion

    # REQUISITO: Sobrescribir el método para demostrar POLIMORFISMO
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        # Usamos obtener_precio() porque el precio está encapsulado en el padre
        print(f"🍽️  Platillo: {self.nombre:<20} | Precio: ${self.obtener_precio():.2f} | Prep: {self.tiempo_preparacion} min | Estado: {estado}")
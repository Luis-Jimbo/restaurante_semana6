# Carpeta: modelos | Archivo: bebida.py

# REQUISITO: Importar la clase padre para poder heredar
from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio_inicial: float, volumen_ml: int):
        """
        Clase hija Bebida que hereda de Producto.
        volumen_ml: int -> Atributo propio (tamaño de la bebida en mililitros).
        """
        # REQUISITO: Uso de super() para reutilizar el constructor del padre
        super().__init__(nombre, precio_inicial)
        self.volumen_ml: int = volumen_ml

    # REQUISITO: Sobrescribir el método para demostrar POLIMORFISMO
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"🥤 Bebida:   {self.nombre:<20} | Precio: ${self.obtener_precio():.2f} | Tamaño: {self.volumen_ml} ml | Estado: {estado}")
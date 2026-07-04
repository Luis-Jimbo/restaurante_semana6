# Carpeta: modelos | Archivo: producto.py

class Producto:
    def __init__(self, nombre: str, precio_inicial: float):
        """
        Clase Padre que representa un producto general.
        Aplica ENCAPSULACIÓN al hacer el precio privado con doble guion bajo (__).
        """
        self.nombre: str = nombre
        # REQUISITO: Atributo encapsulado (privado)
        self.__precio: float = precio_inicial
        self.disponible: bool = True

    # REQUISITO: Método de acceso (Getter) para obtener el precio privado
    def obtener_precio(self) -> float:
        return self.__precio

    # REQUISITO: Método de modificación (Setter) con VALIDACIÓN de precio no negativo ni cero
    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"💰 El precio de '{self.nombre}' se actualizó a ${nuevo_precio:.2f}")
        else:
            print(f"❌ Error: El precio ${nuevo_precio} no es válido. Debe ser mayor a 0.")

    def mostrar_informacion(self):
        """Método base que será sobrescrito en las clases hijas (Polimorfismo)."""
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"📦 Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}")
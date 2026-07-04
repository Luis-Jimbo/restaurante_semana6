# Archivo: main.py (Punto de arranque oficial del sistema)

# REQUISITO: Importar correctamente las clases hijas y el servicio
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

if __name__ == "__main__":
    print("=== INICIALIZANDO SISTEMA DE GESTIÓN (SEMANA 6) ===\n")

    # 1. Creamos el objeto del servicio principal
    mi_restaurante = Restaurante("El Rincón Fronterizo")

    # 2. REQUISITO: Crear al menos dos objetos de tipo Platillo
    # Atributos: nombre, precio_inicial, tiempo_preparacion (minutos)
    platillo1 = Platillo("Ceviche Mixto", 8.50, 15)
    platillo2 = Platillo("Seco de Pollo", 4.00, 10)

    # 3. REQUISITO: Crear al menos dos objetos de tipo Bebida
    # Atributos: nombre, precio_inicial, volumen_ml (mililitros)
    bebida1 = Bebida("Jugo de Maracuyá", 1.50, 400)
    bebida2 = Bebida("Limonada Imperial", 2.00, 500)

    print("--- REGISTRANDO PRODUCTOS EN EL SISTEMA ---")
    # 4. REQUISITO: Agregar los objetos creados a la lista del servicio Restaurante
    mi_restaurante.registrar_producto(platillo1)
    mi_restaurante.registrar_producto(platillo2)
    mi_restaurante.registrar_producto(bebida1)
    mi_restaurante.registrar_producto(bebida2)

    # 5. REQUISITO: Demostrar encapsulación y validación de modificación de precio
    print("\n--- PROBANDO ENCAPSULACIÓN Y VALIDACIONES DE PRECIO ---")
    # Intentamos cambiar el precio de forma correcta (Mayor a 0)
    platillo1.cambiar_precio(9.00)
    
    # Intentamos cambiar el precio de forma incorrecta (Menor o igual a 0) para verificar la validación
    bebida1.cambiar_precio(-0.50)  # Esto debe mostrar un mensaje de error controlado

    # 6. REQUISITO: Mostrar toda la información organizada demostrando POLIMORFISMO
    mi_restaurante.mostrar_menu_completo()
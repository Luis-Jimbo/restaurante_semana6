# Sistema de Gestión de Restaurante - Programación Orientada a Objetos (Semana 6)

Este repositorio contiene el desarrollo práctico de la Semana 6, enfocado en la implementación de jerarquías de herencia, protección de atributos mediante encapsulación y demostración de polimorfismo dinámico en Python.

## Información del Estudiante
* **Nombre Completo:** Luis Jimbo
* **Asignatura:** Programación Orientada a Objetos
* **Institución:** Universidad Estatal Amazónica (UEA)

---

## Estructura de la Arquitectura Modular
El proyecto sigue rigurosamente la distribución de paquetes solicitada por la rúbrica:
* **`modelos/producto.py`**: Contiene la clase padre `Producto` que encapsula el atributo de precio.
* **`modelos/platillo.py`**: Clase hija especializada que añade el atributo de tiempo de preparación.
* **`modelos/bebida.py`**: Clase hija especializada que gestiona el volumen en mililitros.
* **`servicios/restaurante.py`**: Servicio controlador que almacena y administra la colección general de productos.
* **`main.py`**: Punto de arranque que ejecuta las pruebas del sistema.

---

## Componentes Técnicos Evaluados

### 1. Relación de Herencia Aplicada
Se definió una jerarquía donde `Producto` actúa como clase base, mientras que `Platillo` y `Bebida` son clases derivadas. Se utiliza la instrucción `super().__init__()` en los constructores de las clases hijas para delegar y reutilizar la inicialización del nombre y del precio base, evitando la duplicidad de código.

### 2. Atributo Encapsulado y Validaciones
El atributo precio se protegió bajo un esquema de encapsulación estricta definiéndolo como privado (`self.__precio`). El acceso y modificación externa se realiza exclusivamente mediante métodos controladores:
* `obtener_precio()`: Método de acceso (Getter).
* `cambiar_precio()`: Método de modificación (Setter), el cual incluye una estructura condicional que valida que el nuevo valor sea estrictamente superior a cero, denegando precios inválidos o negativos.

### 3. Demostración de Polimorfismo
El polimorfismo dinámico se evidencia en el método `mostrar_menu_completo()` de la clase `Restaurante`. Al iterar sobre una lista genérica de tipo `list[Producto]`, se invoca el método `mostrar_informacion()`. En tiempo de ejecución, Python identifica automáticamente el tipo de objeto específico, imprimiendo el formato con minutos si es un platillo o con mililitros si es una bebida.

---

## Reflexión sobre los Principios de la POO
La implementación de herencia, encapsulación y polimorfismo eleva drásticamente la calidad y mantenibilidad del software. La encapsulación impide que los datos sensibles del negocio (como los costos) sufran mutaciones corruptas o accidentales desde fuera del objeto. Por su parte, la combinación de herencia y polimorfismo permite desarrollar sistemas altamente escalables; si en el futuro el restaurante requiere añadir una nueva categoría de producto (como postres), basta con derivar una nueva clase sin necesidad de modificar el servicio central de la aplicación.

# 2023.back-end
Seguna evaluación para la clase backend de inacap 2023

Este proyecto utiliza los modulos Apache y MySQL por XAMPP
La base de datos en el proyecto se llama "PORTAL"

# Requisitos
1. Elegir un tema y crear el proyecto en django.
2. Crear al menos una aplicación.
3. Basados en el patron models, views, templates.
    Crear cada una de las capas.
4. Crear una base de datos y la conexion.
5. Mostrar desde el administrador de django los datos de la base de datos.

# Contenidos
1. Portal para ofrecer productos y servicios
2. portal
3. patrones
    - models
        - persona
            - nombre
            - correo
            - productos [ ]
            - servicios [ ]
        - item (abstract)
            - nombre
            - precio
            - descripcion
        - item : producto
            - stock
        - item : servicio
            - tiempo (de duracion del servicio)
    - views
        - perfil
            - detalles
            - productos ofrecidos
            - servicios ofrecidos
        - productos
            - todos
            - detalles
                - personas que ofrecen
        - servicios
            - todos
            - detalles
                - personas que ofrecen
    - templates
        - main (para vista de 8 items a la vez)
        - detalle (para una carta principal y detalles de entidades relacionadas)
        - items (para modulos mas pequeños de html)
            - carta
            - navbar
            - tables
            - tabs
            - tarjeta
4. productos_servicios
5. mostrar
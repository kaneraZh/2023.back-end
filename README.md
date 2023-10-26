# 2023.back-end
Seguna evaluación para la clase backend de inacap 2023

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
            - productos []
            - servicios []
        - item (abstract)
            - nombre
            - precio
            - quienes []
        - item : producto
            - stock
        - item : servicio
    - views
        - ingresar
        - perfil
            - informacion
                - -editar
                - -productos  ver/editar
                - -servicios  ver/editar
        - productos
            - -todos
        - servicios
            - -todos
    - templates
        - perfil
        - productos
        - servicios
4. productos_servicios
5. mostrar
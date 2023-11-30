from django.template.loader import render_to_string
def carta(titulo:str,descripcion:str,precio:int,extra:str)->str:
    data = {}
    data['titulo']      = titulo
    data['descripcion'] = descripcion
    data['precio']      = precio
    data['extra']       = extra
    return render_to_string('items/carta.html', data)
def navbar(ventana:int = 0)->str:
    data = {'ventana' : max(min(ventana,2),0)}
    return render_to_string('items/navbar.html', data)
def tables(headings:list, columns:list, page:str, style:list):
    data = {}
    data['headings'] = headings
    class row:
        style:int
        title:str
        page:str
        contents:list
        def __init__(self, style:int, contents:list, page:str):
            self.style = style
            self.title = contents.pop(0)
            self.contents = contents
            self.page = page
    rows = []
    for i in range(len(columns)):
        stl:int = i
        while(stl >= len(style)):stl-= len(style)
        rows.append(row(style[stl], columns[i], page))
        #rows.append(column(0, columns[i]))
    data['rows'] = rows
    print(data)
    return render_to_string('items/tables.html', data)
def tabs(titles:list, contents:list):
    data = {}
    data = {'selected':titles[0]}
    class item:
        title:str
        content:str
        def __init__(self, title:str, content:str):
            self.title = title
            self.content = content
    items:list = []
    for i in range(len(titles)):
        items.append( item(titles[i], contents[i]) )
    data['items'] = items
    return render_to_string('items/tabs.html', data)
def tarjeta_producto(cabecera:str, titulo:str, descripcion:str)->str:
    data = {}
    data['cabecera']    = cabecera
    data['nombre']      = titulo
    data['descripcion'] = descripcion
    return render_to_string('items/tarjeta_producto.html', data)
def tarjeta_servicio(cabecera:str, titulo:str, descripcion:str)->str:
    data = {}
    data['cabecera']    = cabecera
    data['nombre']      = titulo
    data['descripcion'] = descripcion
    return render_to_string('items/tarjeta_servicio.html', data)
def tarjeta(cabecera:str, titulo:str, descripcion:str, pagina:str)->str:
    data = {}
    data['cabecera']    = cabecera
    data['nombre']      = titulo
    data['descripcion'] = descripcion
    data['pagina']      = pagina
    return render_to_string('items/tarjeta.html', data)

from django.shortcuts import render
import portal.models as models
def main(request):
    data = {}
    data['navbar'] = navbar(0)
    data['row1'] = []
    data['row2'] = []
    for p in models.Producto.objects.all()[:4]:
        data['row1'].append( tarjeta(p.precio, p.nombre, p.descripcion, 'producto_detalle') )
    for s in models.Servicio.objects.all()[:4]:
        data['row2'].append( tarjeta(s.precio, s.nombre, s.descripcion, 'servicio_detalle') )
    return render(request, 'main.html', data)
def producto(request, pagina:int=0):
    data = {}
    data['navbar'] = navbar(1)
    data['row1'] = []
    data['row2'] = []
    item_min = 8*pagina
    for p in models.Producto.objects.all()[item_min:item_min+4]:
        data['row1'].append( tarjeta(p.precio, p.nombre, p.descripcion, 'producto_detalle') )
    for p in models.Producto.objects.all()[item_min+4:item_min+8]:
        data['row2'].append( tarjeta(p.precio, p.nombre, p.descripcion, 'producto_detalle') )
    return render(request, 'main.html', data)
def servicio(request, pagina:int=0):
    data = {}
    data['navbar'] = navbar(2)
    data['row1'] = []
    data['row2'] = []
    item_min = 8*pagina
    for s in models.Servicio.objects.all()[item_min:item_min+4]:
        data['row1'].append( tarjeta(s.precio, s.nombre, s.descripcion, 'servicio_detalle') )
    for s in models.Servicio.objects.all()[item_min+4:item_min+8]:
        data['row2'].append( tarjeta(s.precio, s.nombre, s.descripcion, 'servicio_detalle') )
    return render(request, 'main.html', data)

def producto_detalle(request, nombre:str):
    data = {}
    
    data['navbar'] = navbar(1)
    obj = models.Producto.objects.get(nombre=nombre)
    data['principal'] = carta(obj.nombre, obj.descripcion, f'${obj.precio} por unidad', f'quedan {obj.stock} unidades')
    
    usuarios = models.Persona.objects.filter(productos__nombre=obj.nombre)
    columns = []
    for u in usuarios:
        columns.append([u.nombre, u.correo])
    data['tabs'] = tabs(
        ['Personas que ofrecen este producto'],
        [tables(
            ['Nombre','Correo'],
            columns,
            'persona',
            [0,1]
        )]
    )
    return render(request, 'detalle.html', data)
def servicio_detalle(request, nombre:str):
    data = {}
    
    data['navbar'] = navbar(1)
    obj = models.Servicio.objects.get(nombre=nombre)
    data['principal'] = carta(obj.nombre, obj.descripcion, f'${obj.precio} por sesión', f'La sesión durará {obj.tiempo}')
    
    usuarios = models.Persona.objects.filter(servicios__nombre=obj.nombre)
    columns = []
    for u in usuarios:
        columns.append([u.nombre, u.correo])
    data['tabs'] = tabs(
        ['Personas que ofrecen este servicio'],
        [tables(
            ['Nombre','Correo'],
            columns,
            'persona',
            [0,1]
        )]
    )
    return render(request, 'detalle.html', data)
def persona(request, nombre:str):
    data = {}
    data['navbar'] = navbar(0)
    obj = models.Persona.objects.get(nombre=nombre)
    data['principal'] = carta(obj.nombre, obj.correo, '', '')
    
    usuario = models.Persona.objects.get(nombre=nombre)
    productos = []
    servicios = []
    for p in usuario.productos.all():
        productos.append([p.nombre, p.precio, p.descripcion, p.stock])
    for s in usuario.servicios.all():
        servicios.append([s.nombre, s.precio, s.descripcion, s.tiempo])
    data['tabs'] = tabs(
        ['Productos_ofrecidos', 'Servicios_ofrecidos'],
        [
            tables(
                ['Nombre','Precio','Descripción','Stock'],
                productos,
                'producto_detalle',
                [0,1]
            ),
            tables(
                ['Nombre','Precio','Descripción','Duración'],
                servicios,
                'servicio_detalle',
                [0,1]
            )
        ]
    )
    return render(request, 'detalle.html', data)


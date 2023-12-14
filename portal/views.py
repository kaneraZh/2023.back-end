from django.template.loader import render_to_string
from django.shortcuts import redirect
def carta(titulo:str,descripcion:str,precio:int,extra:str)->str:
    data = {}
    data['titulo']      = titulo
    data['descripcion'] = descripcion
    data['precio']      = precio
    data['extra']       = extra
    return render_to_string('_items/carta.html', data)
def navbar(ventana:int = 0)->str:
    data = {'ventana' : max(min(ventana,2),0)}
    return render_to_string('_items/navbar.html', data)
def tables(headings:list, columns:list, url:str, style:list, pks:int):
    data = {}
    data['headings'] = headings
    rows = []
    for i in range(len(columns)):
        stl:int = i
        while(stl >= len(style)):stl-= len(style)
        rows.append({
            'style' : style,
            'title' : columns.pop(0),
            'contents' : columns,
            'url' : url,
            'pk' : pks.pop(0),
        })
        #rows.append(column(0, columns[i]))
    data['rows'] = rows
    print(data)
    return render_to_string('_items/tables.html', data)
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
    return render_to_string('_items/tabs.html', data)
def tarjeta_producto(cabecera:str, titulo:str, descripcion:str)->str:
    data = {}
    data['cabecera']    = cabecera
    data['nombre']      = titulo
    data['descripcion'] = descripcion
    return render_to_string('_items/tarjeta_producto.html', data)
def tarjeta_servicio(cabecera:str, titulo:str, descripcion:str)->str:
    data = {}
    data['cabecera']    = cabecera
    data['nombre']      = titulo
    data['descripcion'] = descripcion
    return render_to_string('_items/tarjeta_servicio.html', data)
def tarjeta(cabecera:str, titulo:str, descripcion:str, page:str, pk:int)->str:
    data = {}
    data['cabecera']    = cabecera
    data['nombre']      = titulo
    data['descripcion'] = descripcion
    data['page']      = page
    data['pk']          = pk
    return render_to_string('_items/tarjeta.html', data)

from django.shortcuts import render
import portal.models as models
def main(request):
    data = {}
    data['navbar_items'] = [
        {
            'url' : PERSONA_LISTA,
            'page': 0,
        },
        {
            'url' : PRODUCTO_LISTA,
            'page': 0,
        },
        {
            'url' : SERVICIO_LISTA,
            'page': 0,
        },
    ]
    data['row1'] = []
    data['row2'] = []
    for p in models.Producto.objects.all()[:4]:
        data['row1'].append(
            {
                "cabecera" : p.precio,
                "nombre" : p.nombre,
                "descripcion" : p.descripcion,
                "url" : PRODUCTO_VER,
                "pk" : p.id,
            }
        )
    for s in models.Servicio.objects.all()[:4]:
        data['row2'].append(
            {
                "cabecera" : s.precio,
                "nombre" : s.nombre,
                "descripcion" : s.descripcion,
                "url" : SERVICIO_VER,
                "pk" : s.id,
            }
        )
    return render(request, 'main.html', data)
def producto(request, page:int=0):
    data = {}
    data['navbar_items'] = [
        {
            'url' : PERSONA_LISTA,
            'page': 0,
        },
        {
            'url' : PRODUCTO_LISTA,
            'page': 0,
        },
        {
            'url' : SERVICIO_LISTA,
            'page': 0,
        },
    ]
    data['row1'] = []
    data['row2'] = []
    item_min = 8*page
    for p in models.Producto.objects.all()[item_min:item_min+4]:
        data['row1'].append(
            {
                "cabecera" : p.precio,
                "nombre" : p.nombre,
                "descripcion" : p.descripcion,
                "url" : PRODUCTO_VER ,
                "pk" : p.id,
            }
        )
    for p in models.Producto.objects.all()[item_min+4:item_min+8]:
        data['row2'].append(
            {
                "cabecera" : p.precio,
                "nombre" : p.nombre,
                "descripcion" : p.descripcion,
                "url" : PRODUCTO_VER ,
                "pk" : p.id,
            }
        )
    return render(request, 'main.html', data)
def servicio(request, page:int=0):
    data = {}
    data['navbar_items'] = [
        {
            'url' : PERSONA_LISTA,
            'page': 0,
        },
        {
            'url' : PRODUCTO_LISTA,
            'page': 0,
        },
        {
            'url' : SERVICIO_LISTA,
            'page': 0,
        },
    ]
    data['row1'] = []
    data['row2'] = []
    item_min = 8*page
    for s in models.Servicio.objects.all()[item_min:item_min+4]:
        data['row1'].append(
            {
                "cabecera" : s.precio,
                "nombre" : s.nombre,
                "descripcion" : s.descripcion,
                "url" : SERVICIO_VER ,
                "pk" : s.id,
            }
        )
    for s in models.Servicio.objects.all()[item_min+4:item_min+8]:
        data['row2'].append(
            {
                "cabecera" : s.precio,
                "nombre" : s.nombre,
                "descripcion" : s.descripcion,
                "url" : SERVICIO_VER ,
                "pk" : s.id,
            }
        )
    return render(request, 'main.html', data)

def producto_detalle(request, pk:int):
    data = {}
    
    data['navbar_items'] = [
        {
            'url' : PERSONA_LISTA,
            'page': 0,
        },
        {
            'url' : PRODUCTO_LISTA,
            'page': 0,
        },
        {
            'url' : SERVICIO_LISTA,
            'page': 0,
        },
    ]
    obj = models.Producto.objects.get(id=pk)
    data['principal'] = carta(obj.nombre, obj.descripcion, f'${obj.precio} por unidad', f'quedan {obj.stock} unidades')
    
    usuarios = models.Persona.objects.filter(productos__nombre=obj.nombre)
    columns = []
    ids = []
    for u in usuarios:
        columns.append([u.nombre, u.correo])
        ids.append(u.id)
    data['tabs'] = tabs(
        ['Personas que ofrecen este producto'],
        [tables(
            ['Nombre','Correo'],
            columns,
            PERSONA_VER,
            [0,1],
            ids,
        )]
    )
    return render(request, 'detalle.html', data)
def servicio_detalle(request, pk:str):
    data = {}
    
    data['navbar_items'] = [
        {
            'url' : PERSONA_LISTA,
            'page': 0,
        },
        {
            'url' : PRODUCTO_LISTA,
            'page': 0,
        },
        {
            'url' : SERVICIO_LISTA,
            'page': 0,
        },
    ]
    obj = models.Servicio.objects.get(id=pk)
    data['principal'] = carta(obj.nombre, obj.descripcion, f'${obj.precio} por sesión', f'La sesión durará {obj.tiempo}')
    
    usuarios = models.Persona.objects.filter(servicios__nombre=obj.nombre)
    columns = []
    ids = []
    for u in usuarios:
        columns.append([u.nombre, u.correo])
        ids.append(u.id)
    data['tabs'] = tabs(
        ['Personas que ofrecen este servicio'],
        [tables(
            ['Nombre','Correo'],
            columns,
            PERSONA_VER,
            [0,1],
            ids,
        )]
    )
    return render(request, 'detalle.html', data)
def persona(request, pk:int):
    data = {}
    data['navbar_items'] = [
        {
            'url' : PERSONA_LISTA,
            'page': 0,
        },
        {
            'url' : PRODUCTO_LISTA,
            'page': 0,
        },
        {
            'url' : SERVICIO_LISTA,
            'page': 0,
        },
    ]
    obj = models.Persona.objects.get(id=pk)
    data['principal'] = carta(obj.nombre, obj.correo, '', '')
    
    usuario = models.Persona.objects.get(id=pk)
    productos = []
    pids = []
    servicios = []
    sids = []
    for p in usuario.productos.all():
        productos.append([p.nombre, p.precio, p.descripcion, p.stock])
        pids.append(p.id)
    for s in usuario.servicios.all():
        servicios.append([s.nombre, s.precio, s.descripcion, s.tiempo])
        sids.append(s.id)
    data['tabs'] = tabs(
        ['Productos_ofrecidos', 'Servicios_ofrecidos'],
        [
            tables(
                ['Nombre','Precio','Descripción','Stock'],
                productos,
                PRODUCTO_VER,
                [0,1],
                pids,
            ),
            tables(
                ['Nombre','Precio','Descripción','Duración'],
                servicios,
                SERVICIO_VER,
                [0,1],
                sids,
            )
        ]
    )
    return render(request, 'detalle.html', data)

from .forms import PersonaForm
PERSONA_AGREGAR = 'persona_agregar'
PERSONA_MODIFICAR = 'persona_modificar'
PERSONA_ELIMINAR = 'persona_eliminar'
PERSONA_LISTA = 'persona_lista'
PERSONA_VER = 'persona_ver'
def persona_agregar(request):
    form = PersonaForm()
    if(request.method == 'POST'):
        form = PersonaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect(PERSONA_LISTA)
    context = {
        'form' : form,
        'lista' : PERSONA_LISTA,
    }
    return render(request, '_generic/agregar.html', context)
def persona_modificar(request, pk:int):
    model = models.Persona.objects.get(id=pk)
    form = PersonaForm(instance=model)
    if(request.method == 'POST'):
        form = PersonaForm(request.POST, instance=model)
        if(form.is_valid()):
            form.save()
            return redirect(PERSONA_LISTA)
    context = {
        'form' : form,
        'lista' : PERSONA_LISTA,
    }
    return render(request, '_generic/modificar.html', context)
def persona_eliminar(request, pk:int):
    models.Persona.objects.get(id=pk).delete()
    return redirect('persona_lista')
def persona_lista(request):
    title_list = [
        'id',
        'nombre',
        'correo',
        'productos',
        'servicios',
    ]
    object_list = []
    for obj in models.Persona.objects.all():
        productos = []
        for item in obj.productos.all():
            productos.append(f'{item}')
        servicios = []
        for item in obj.servicios.all():
            servicios.append(f'{item}')
        object_list.append([
            obj.id,
            obj.nombre,
            obj.correo,
            ', '.join(productos),
            ', '.join(servicios),
        ])
    context = {
        'title_list' : title_list,
        'object_list' : object_list,
        'modificar' : PERSONA_MODIFICAR,
        'eliminar' : PERSONA_ELIMINAR,
        'ver' : PERSONA_VER,
        'agregar' : PERSONA_AGREGAR,
    }
    return render(request, '_generic/lista.html', context)

from .forms import ProductoForm
PRODUCTO_AGREGAR = 'producto_agregar'
PRODUCTO_MODIFICAR = 'producto_modificar'
PRODUCTO_ELIMINAR = 'producto_eliminar'
PRODUCTO_LISTA = 'producto_lista'
PRODUCTO_VER = 'producto_ver'
def producto_agregar(request):
    form = ProductoForm()
    if(request.method == 'POST'):
        form = ProductoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect(PRODUCTO_LISTA)
    context = {
        'form' : form,
        'lista' : PRODUCTO_LISTA,
    }
    return render(request, '_generic/agregar.html', context)
def producto_modificar(request, pk:int):
    model = models.Producto.objects.get(id=pk)
    form = ProductoForm(instance=model)
    if(request.method == 'POST'):
        form = ProductoForm(request.POST, instance=model)
        if(form.is_valid()):
            form.save()
            return redirect(PRODUCTO_LISTA)
    context = {
        'form' : form,
        'lista' : PRODUCTO_LISTA,
    }
    return render(request, '_generic/modificar.html', context)
def producto_eliminar(request, pk:int):
    models.Producto.objects.get(id=pk).delete()
    return redirect('producto_lista')
def producto_lista(request):
    title_list = [
        'id',
        'nombre',
        'precio',
        'descripcion',
        'stock',
    ]
    object_list = []
    for obj in models.Producto.objects.all():
        object_list.append([
            obj.id,
            obj.nombre,
            obj.precio,
            obj.descripcion,
            obj.stock,
        ])
    context = {
        'title_list' : title_list,
        'object_list' : object_list,
        'modificar' : PRODUCTO_MODIFICAR,
        'eliminar' : PRODUCTO_ELIMINAR,
        'ver' : PRODUCTO_VER,
        'agregar' : PRODUCTO_AGREGAR,
    }
    return render(request, '_generic/lista.html', context)

from .forms import ServicioForm
SERVICIO_AGREGAR = 'servicio_agregar'
SERVICIO_MODIFICAR = 'servicio_modificar'
SERVICIO_ELIMINAR = 'servicio_eliminar'
SERVICIO_LISTA = 'servicio_lista'
SERVICIO_VER = 'servicio_ver'
def servicio_agregar(request):
    form = ServicioForm()
    if(request.method == 'POST'):
        form = ServicioForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect(SERVICIO_LISTA)
    context = {
        'form' : form,
        'lista' : SERVICIO_LISTA,
    }
    return render(request, '_generic/agregar.html', context)
def servicio_modificar(request, pk:int):
    model = models.Servicio.objects.get(id=pk)
    form = ServicioForm(instance=model)
    if(request.method == 'POST'):
        form = ServicioForm(request.POST, instance=model)
        if(form.is_valid()):
            form.save()
            return redirect(SERVICIO_LISTA)
    context = {
        'form' : form,
        'lista' : SERVICIO_LISTA,
    }
    return render(request, '_generic/modificar.html', context)
def servicio_eliminar(request, pk:int):
    models.Servicio.objects.get(id=pk).delete()
    return redirect('servicio_lista')
def servicio_lista(request):
    title_list = [
        'id',
        'nombre',
        'precio',
        'descripcion',
        'tiempo',
    ]
    object_list = []
    for obj in models.Servicio.objects.all():
        object_list.append([
            obj.id,
            obj.nombre,
            obj.precio,
            obj.descripcion,
            obj.tiempo,
        ])
    context = {
        'title_list' : title_list,
        'object_list' : object_list,
        'modificar' : SERVICIO_MODIFICAR,
        'eliminar' : SERVICIO_ELIMINAR,
        'ver' : SERVICIO_VER,
        'agregar' : SERVICIO_AGREGAR,
    }
    return render(request, '_generic/lista.html', context)

#API
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductoSerializer

@api_view(['GET', 'POST'])
def producto_lista_api(request):
    match request.method:
        case 'GET':
            producto = models.Producto.objects.all()
            serializer = ProductoSerializer(producto, many=True)
            return Response(serializer.data)
        case 'POST':
            serializer = ProductoSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def producto_detalle_api(request, pk):
    try:
        producto = models.Producto.objects.get(pk=pk)
    except models.Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    match request.method:
        case 'GET':
            serializer = ProductoSerializer(producto)
            return Response(serializer.data)
        case 'PUT':
            serializer = ProductoSerializer(producto, data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        case 'DELETE':
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
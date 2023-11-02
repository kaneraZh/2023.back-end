from django.template.loader import render_to_string
def navbar(ventana:int = 0)->str:
    data = {'ventana' : clamp(ventana, 0, 2)}
    return render_to_string('items/navbar.html', data)
def tables(headings:list, columns:list, styles:list):
    data = {}
    data['headings'] = headings
    class column:
        style:int
        title:str
        contents:list
        def __init__(self, style:int, contents:list):
            self.style = style
            self.title = contents.pop(0)
            self.contents = contents
    cols = []
    for i in range(len(columns)):
        stl:int = i
        while(stl >= len(style)):
            stl-= len(style)
        cols.append(stl, columns[i])
    data['columns'] = cols
    return render_to_string('items/tables.html', data)
def tabs(titles:list, contents:list):
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
def tarjeta(cabecera:str, titulo:str, descripcion:str)->str:
    data = {}
    data['cabecera']    = cabecera
    data['titulo']      = titulo
    data['descripcion'] = descripcion
    return render_to_string('items/tarjeta.html', data)


from django.shortcuts import render
import portal.models as models
def main(request):
    data = {}
    data['productos'] = models.Producto.objects.all()
    data['servicios'] = models.Servicio.objects.all()
    return render(request, 'main.html', data)

def productos(request, pagina:int=0):
    data = {}
    # get productos desde 8*pagina hasta 8*pagina+8?
    # para 8 items en total
    # if aprieta producto, lleva al detalle de ese producto
    return render(request, 'productos.html', data)

def servicios(request, pagina:int=0):
    data = {}
    # get servicios desde 8*pagina hasta 8*pagina+8?
    # para 8 items en total
    # if aprieta producto, lleva al detalle de ese servicio
    return render(request, 'servicios.html', data)

def detalles(request, model):
    data = {}
    #data['modelo'] = 
    return render(request, 'detalle.html', data)

def persona(request, persona:str=''):
    data = {}
    data['persona'] = models.Persona.objects.get(persona)
    #data['productos'] = models.Producto.objects.all() productos de la persona
    #data['servicios'] = models.Servicio.objects.has() servicios de la persona
    return render(request, 'persona.html', data)

from django.shortcuts import render, redirect
from .models import Producto, Carro, Categoria

def index(request):
    return render(request, 'ventas/index.html', {})

def tienda(request):
    #Inicializacion
    Categorias = Categoria.objects.all()
    #Opciones seleccionadas
    selectCategoria = request.GET.get('categoria')
    inputNombre = request.GET.get('nombre')
    ordenarPor = request.GET.get('ordenar')
    ordenarCampo = 'valor'

    if ordenarPor!='menorprecio' and ordenarPor is not None:
        if ordenarPor == 'categoria':
            ordenarCampo = 'categoria'
        elif ordenarPor == 'mayorprecio':
            ordenarCampo = '-valor'
        elif ordenarPor=='onombre':
            ordenarCampo = 'nombre'
    
    
    Productos = Producto.objects.all().exclude(stock=0).order_by(ordenarCampo)

    if selectCategoria!='' and selectCategoria is not None:
        objCategoria = Categoria.objects.filter(nombre=selectCategoria)[0]
        Productos = Producto.objects.filter(categoria=objCategoria).order_by(ordenarCampo)

    if inputNombre!='' and inputNombre is not None:
        Productos = Producto.objects.filter(nombre__icontains=inputNombre).order_by(ordenarCampo)
    print(ordenarCampo)
    
    contexto = {
        "Productos":Productos,
        "Categorias":Categorias,
        #selected
        "selectCategoria":selectCategoria,
        "inputNombre":inputNombre,
        "ordenarPor":ordenarPor
    }
    return render(request, 'ventas/tienda.html', contexto)

def producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'ventas/producto.html', {"producto":producto})

def añadir(request, pk):

    return render(request, 'ventas/producto.html', {"producto":producto})

def carro(request):

    return render(request, 'ventas/carro.html', {})

from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import Producto, Carro, Categoria
from .forms import UserCreateForm

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
    usuario=User(pk=request.user.pk)
    producto = Producto.objects.get(pk=pk)
    existe = Carro.objects.filter(usuario=usuario)
    nr=len(existe)
    if nr!=0:
        existe[0].productos.add(producto)
        existe.save()
    else:
        User
        nuevo = Carro(usuario=usuario)
        nuevo.save()
        nuevo.productos.add(producto)
        nuevo.save()

    return render(request, 'ventas/producto.html', {"producto":producto})

def carro(request):
    user=request.user
    carro = Carro.objects.filter(usuario=user)
    return render(request, 'ventas/carro.html', {"carro":carro})

def registrarme(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("tienda")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "ventas/registrarme.html",
                          context={"form":form})

    form = UserCreateForm
    return render(request = request,
                  template_name = "ventas/registrarme.html",
                  context={"form":form})

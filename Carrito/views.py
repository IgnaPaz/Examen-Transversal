from django.shortcuts import render, redirect, get_object_or_404
from .models import Catalogo
from .forms import CatalogoForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from .forms import RegistroForm
from django.contrib.auth.decorators import permission_required

# Listar Catalogo
@permission_required('app.can_access_catalogo_crud', raise_exception=True)
def catalogo_list(request):
    catalogos = Catalogo.objects.all()
    form = CatalogoForm()
    return render(request, 'carrito/listar_catalogo.html', {'catalogos': catalogos, 'form': form, 'action': 'list'})
# -----------------------------------------------------

# Crear Catalago
@permission_required('app.can_create_catalogo', raise_exception=True)
def catalogo_create(request):
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_list')
    else:
        form = CatalogoForm()
    return render(request, 'carrito/crear_catalogo.html', {'form': form, 'action': 'create'})
# --------------------------------

# Modificar Catalogo
@permission_required('app.can_change_catalogo', raise_exception=True)
def catalogo_update(request, pk):
    catalogo = get_object_or_404(Catalogo, pk=pk)
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES, instance=catalogo)
        if form.is_valid():
            form.save()
            return redirect('catalogo_list')
    else:
        form = CatalogoForm(instance=catalogo)
    return render(request, 'carrito/modificar_catalogo.html', {'form': form, 'action': 'update', 'catalogo': catalogo})
# --------------------------------

# Eliminar Catalogo
@permission_required('app.can_delete_catalogo', raise_exception=True)
def catalogo_delete(request, pk):
    catalogo = get_object_or_404(Catalogo, pk=pk)
    if request.method == 'POST':
        catalogo.delete()
        return redirect('catalogo_list')
    return render(request, 'carrito/eliminar_catalogo.html', {'catalogo': catalogo, 'action': 'delete'})
# -------------------------------------


# Detalle Catalogo
@permission_required('app.can_view_catalogo', raise_exception=True)
def detalle_catalogo(request, pk):
    catalogo = get_object_or_404(Catalogo, pk=pk)
    return render(request, 'detalle_catalogo.html', {'catalogo': catalogo})
# --------------------------------------


# Vistas Generales
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            user = authenticate(request, username=correo, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('carrito')  # Redirigir a la página de inicio
            else:
                form.add_error(None, 'Correo o contraseña incorrectos')
    else:
        form = LoginForm()

    return render(request, 'carrito/iniciar.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()

    return render(request, 'carrito/registrar.html', {'form': form})

def nueva_iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            user = authenticate(request, username=correo, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirigir a la página de inicio
            else:
                form.add_error(None, 'Correo o contraseña incorrectos')
    else:
        form = LoginForm()

    return render(request, 'carrito/iniciar.html', {'form': form})


def carrito_view(request):
    catalogos = Catalogo.objects.all()
    return render(request, 'carrito.html', {'catalogos': catalogos})

def empleados(request):
    return render(request, 'carrito/empleados.html',{})

def index(request):
    return render(request, 'carrito/index.html', {})

def novios(request):
    return render(request, 'carrito/novios.html', {})

def novias(request):
    return render(request, 'carrito/novias.html', {})


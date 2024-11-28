# Librerias unicas de Django
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm # formularios de usuario y autenticacion
from django.contrib.auth import login, logout, authenticate # Necesario para crear 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required # Login requerido

# Librerias de Django Rest Framework
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *
from .form import *

#--------------- System form Log -------------
# Vista Inicio
def home(request):
    return render(request,'home.html')

# Vista Registro
def signup(request):
    if request.method == 'GET':
        return render(request, 'sign/signup.html', {"form": CustomUserForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'sign/signup.html', {"form": CustomUserForm, "error": "Este usuario ya existe."})

        return render(request, 'sign/signup.html', {"form": CustomUserForm, "error": "Las contraseñas no coinciden."})

# Vista Login
def signin(request):
    if request.method == 'GET':
        return render(request, 'sign/signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sign/signin.html', {'form':AuthenticationForm, 'error':'El usuario no existe'})
        
        login(request, user)
        return redirect('home')
# Funcionalidad Logout
@login_required
def signout(request):
    logout(request)
    return redirect('home')

# ---------------- API ----------------
# Configuración de filtrado especificando los campos en filterset_fields
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all() #Todos los registros de clientes
    serializer_class = ClienteSerializer #Serializador que se usa para la vista
    filter_backends = [DjangoFilterBackend] #Configuramos el backend de filtros
    filterset_fields = ['genero', 'active', 'nivel_de_satisfaccion'] #Campos filtrables


# ---------------- Templates ----------------
# Listar todos los clientes
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()  # Consulta para obtener todos los clientes
    return render(request, 'clientes/list.html', {'clientes': clientes})


# Crear un nuevo cliente
@login_required
def cliente_create(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes/form.html', {'form': form, 'title': 'Agregar Cliente'})

# Editar un cliente existente
@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes/form.html', {'form': form, 'title': 'Editar Cliente'})

# Eliminar un cliente
@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/confirm_delete.html', {'cliente': cliente})
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'clientes',ClienteViewSet) # Ruta /api/clientes/

urlpatterns = [
    path('api/', include(router.urls)), #Incluye las rutas generadas por el router
    # Rutas Home - Login - Register
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='logout'),
    # Rutas Templates
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/create', cliente_create, name='cliente_create'),
    path('clientes/update/<int:pk>', cliente_update, name='cliente_update'),
    path('clientes/delete/<int:pk>', cliente_delete, name='cliente_delete'),
]
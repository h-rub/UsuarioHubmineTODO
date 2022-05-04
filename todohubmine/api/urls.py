from django.urls import path
from .views import UsuarioView

urlpatterns = [
    #path('usuarios/registro',UsuarioView.as_view(), name='usuarios_list')
    path('auth/register',UsuarioView.as_view(), name='usuarios_list')
]
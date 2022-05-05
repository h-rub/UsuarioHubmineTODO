from django.urls import path
from .views import UsuarioView, TaskView

urlpatterns = [
    #path('usuarios/registro',UsuarioView.as_view(), name='usuarios_list')
    path('auth/register',UsuarioView.as_view(), name='usuarios_list'),
    path('task/register',TaskView.as_view(), name='task_list')
]
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.hashers import make_password
from .models import Usuarios
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class UsuarioView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """def get(self, request):
        usuarios = list(Usuarios.objects.values())
        if len(usuarios)>0:
            datos={'mensaje':'Exito', 'Usuarios': usuarios}
        else:
            datos={'mensaje':'Sin Éxito'}
        return JsonResponse(datos)  """

    def post(self, request):
        if request.method == 'POST':
            datos={'mensaje':'Exito'}
            jd = json.loads(request.body)
            Usuarios.objects.create(nombre=jd['nombre'],apellidos=jd['apellidos'],email=jd['email'],password=make_password(jd['password']))
            return JsonResponse(datos)
        else:
            datos={'mensaje':'Aquí se registran usuarios'}
            return JsonResponse(datos)  

    def put(self, request):
        pass

    def delete(self, request):
        pass
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.hashers import make_password
from .models import Usuarios
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class UsuarioView(View):
    
    #Esta función corrige el error por csrf, se puede omitir cuando en el formulario se agrega csrf token
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """
        Con esta función se pueden registrar usuarios en la base de datos, recibe un JSON con los
        atributos: 'name','last_name','email','password'
        La contraseña se encripta con la función make_password()
        Al ser usada con el método POST y con los datos del JSON correctos,
        Retorna un estado 200 y el mensaje "Exito"
        La ruta utilizada es '/api/auth/register'
        """
        if request.method == 'POST':
            jd = json.loads(request.body)
            Usuarios.objects.create(name=jd['name'],last_name=jd['last_name'],email=jd['email'],
            password=make_password(jd['password']))
            datos={'mensaje':'Exito'}
            return JsonResponse(datos) 
        else:
            datos={'mensaje':'Aquí se registran usuarios'}
            return JsonResponse(datos)  
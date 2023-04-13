#PYTHON

#DJANGO
from django.views.generic import TemplateView
from django.http import JsonResponse

#limitador de django
from django_ratelimit.decorators import ratelimit

#REST-FRAMEWORK
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import throttle_classes
#otro estrangulador de peticiones
from .throttling import AnonymousUserThrottle

#models local
from .models import DatosHome




# Create your views here.


@throttle_classes([AnonRateThrottle])
class HomePageView(TemplateView):
    template_name = "home/index.html"
        
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)   
 
 
@ratelimit(key='ip', rate='2/h')
@throttle_classes([AnonRateThrottle])       
def numero_wsp(request):
    
    foo = DatosHome.objects.last()   
    foo.contador_clicks_wthasapp += 1
    foo.save()
    
    if foo.contador_clicks_wthasapp % 2 == 0:
        url_wsp = "https://api.whatsapp.com/send/?phone=5493512115781&text=Hola+Maida%21+quisiera+realizar+una+consulta%2C+soy+mayor+de+18+a%C3%B1os.&type=phone_number&app_absent=0"
    else:
        url_wsp = "https://wa.me/5493512520142?text=Hola%20Maida!%20quisiera%20realizar%20una%20consulta,%20soy%20mayor%20de%2018%20a%C3%B1os."
    
    data = {"url_wsp": url_wsp}
    
    return JsonResponse(data)


    
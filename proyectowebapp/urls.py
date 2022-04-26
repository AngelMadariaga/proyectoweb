from django.urls import path
from.views import home, blog, formulario


from django.contrib import admin


urlpatterns = [

 url(r'admin', admin.site.urls ),
 url(r'usuario' , include('apps.usuario.urls', namespace="usuario")),
 
     
    path('' ,views.home , name="home" ),
    path('registro' ,views.registro , name="registro" ),
    path('conctatos' ,views.conctatos , name="conctatos" ),
    path('blog' ,views.blog , name="blog" ),
    
]

from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationFrom
from django.views-from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class registriousuario(creataview):
    .model= user
    template_name="usuario/registrar.html"
    from_class = UserCreationForm
    success_url =reverse_lazy('mascotas:mascota_lista')

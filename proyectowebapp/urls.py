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
    
    

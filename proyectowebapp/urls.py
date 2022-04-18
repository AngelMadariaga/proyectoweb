from django.urls import path


from proyectowebapp import views

urlpatterns = [
    
    path('' ,views.home , name="home" ),
    path('registro' ,views.registro , name="registro" ),
    path('conctatos' ,views.conctatos , name="conctatos" ),
    path('blog' ,views.blog , name="blog" ),
    
]

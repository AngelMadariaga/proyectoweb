from django.urls import path


from proyectoapp import views

urlpatterns = [
    
    path('' ,views.home , name="home" ),
    path('ayuda' ,views.ayuda , name="ayuda" ),
    path('registro' ,views.registro , name="registro" ),
    path('conctatos' ,views.conctatos , name="conctatos" ),
    path('blog' ,views.blog , name="blog" ),
    
]

from django.shortcuts import render , HttpResponse 

# Create your views here.

def home(request):
    
    return render (request, "proyectowebapp/inicio.html")
    
def registro(request):
    return render (request, "proyectowebapp/formulario.html")


def ayuda (request):
    
     return render  (request, "proyectowebapp/blog.html")   



def conctatos  (request):
    
    return httpresponse ("conctatos ")

def blog  (request):
    
    return render (request, "proyectowebapp/blog.html")

def menu(request):
    
    return render (reques, "proyectowebapp/menu.html")
    


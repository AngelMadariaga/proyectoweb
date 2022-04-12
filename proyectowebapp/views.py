from django.shortcuts import render , httpresponse

# Create your views here.

def home(request):
    
    return render (request, "proyectowebapp/inicio.html")
    
 def registro(request):
        
     return render (request, "proyectowebapp/registro.html")


def ayuda (request):
    
    return httpresponse ("registro ")    



def conctatos  (request):
    
    return httpresponse ("conctatos ")

def blog  (request):
    
    return render (request, "proyectowebapp/blog.html")
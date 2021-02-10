from django.shortcuts import render

# Create your views here.
layout = """

"""
def cursos(request):
    return render(request,'cursos.html',{
        'titulo':'cursos'
    })

def carreras(request):
 
   return render(request,'carreras.html',{
       'titulo':'carreras'
    })
def crearcursos(request):
    
   return render(request,'create_cursos.html',{
       'titulo':'Crear Cursos'
    })

def crearcarreras(request):
    
   return render(request,'create_carreras.html',{
       'titulo':'Crear Carreras'
    })

def index(request):
 
   return render(request,'index.html',{
       'titulo':'index'
    })


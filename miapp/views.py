from django.shortcuts import render,redirect
from miapp.models import Curso,Carrera
from django.db.models import Q
from django.contrib import messages
from miapp.forms import form_carrera,form_carrera2

# Create your views here.
layout = """

"""
def cursos(request):
    cur = Curso.objects.all()
    return render(request,'cursos.html',{
        'titulo':'cursos',
        'cursos':cur
    })


def crearcursos(request):
    if request.method == 'POST':
        formulario = form_carrera(request.POST)
        if formulario.is_valid():
            dato = formulario.cleaned_data
            codigo = dato['codigo']
            nombre = dato['nombre']
            hora = dato['hora']
            crerditos = dato['creditos']
            estado = dato['estado']

        cu = Curso(codigo=codigo,nombre=nombre,hora=hora,creditos=crerditos,estado=estado)
        cu.save()

        messages.success(request,f"Se agrego la carrera correctamente {cu.nombre}")
        return redirect('cursos')
    else:
        formulario=form_carrera()
    return render(request,"create_cursos.html",{'form':formulario})
# ____________________________________________________________________________________________
def carreras(request):
    ca =Carrera.objects.all()
    return render(request,'carreras.html',{
       'titulo':'carreras',
       'carreras':ca
    })


def crearcarreras(request):
    if request.method=='POST':
        formulario = form_carrera2(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos['nombre']
            nombrecorto = datos['nombrecorto']
            estado = datos['estado']

            care = Carrera(nombre=nombre,estado=estado,nombrecorto=nombrecorto)
            care.save()

            messages.success(request,f"Se agrego {care.nombre}")

            return redirect('carreras')
    else:
        formulario = form_carrera2()
    return render(request,'create_carreras.html', {
       'titulo':'Crear Carreras',
       'form':formulario
    })


def eliminar_curso(request,id):
    a = Curso.objects.get(id=id)
    a.delete()
    return redirect('cursos')















def index(request):
 
   return render(request,'index.html',{
       'titulo':'index'
    })


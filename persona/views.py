from django import template
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader
from persona.models import Ciudad, Persona, Tdocumento
from persona.forms import CiudadForm, PersonaForm, TdocumentoForm
from django.urls import reverse

# Create your views here.

def index(request):
    ciudades = Ciudad.objects.all()
    template = loader.get_template('persona/index.html')
    context = {
        'ciudades':ciudades,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ciudades(request):
    ciudades = Ciudad.objects.all()
    template = loader.get_template('persona/ciudades.html')
    context = {'ciudades': ciudades,}
    return HttpResponse(template.render(context, request))

def tdocumento(request):
    tdocumento = Tdocumento.objects.all()
    template = loader.get_template('persona/tdocumento.html')
    context = {'tdocumento': tdocumento,}
    return HttpResponse(template.render(context, request))    

def new_tdocumento(request):
    #se ejecuta cuando el usuario envia el formulario con lo datos
    if request.method == 'POST':
        #Crea una instancia del autor
        form = TdocumentoForm(request.POST)
        #Evaluamos si el formulario es correcto, lo guardamos y redireccionamos
        if form.is_valid():
            #Obtenemos lo datos del formulario
            nombrex = form.cleaned_data['nombre']
            descripcionx = form.cleaned_data['descripcion']
            tdocumento = Tdocumento(nombre=nombrex, descripcion = descripcionx)
            tdocumento.save()
            return HttpResponseRedirect(reverse('tdocumento'))
    
    else:
        #Se ejecuta cuando el usuario va a llenar el formulario
        form = TdocumentoForm()
    

    return render(request, 'persona/create_tdocumento.html', {'form':form})


def personas(request):
    personas = Persona.objects.all()
    template = loader.get_template('persona/personas.html')
    context = {'personas': personas, }
    return HttpResponse(template.render(context, request))

def new_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            nombrex = form.cleaned_data['nombre']
            descripcionx = form.cleaned_data['descripcion']
            ciudad = Ciudad(nombre=nombrex, descripcion = descripcionx)
            ciudad.save()
            return HttpResponseRedirect(reverse('ciudades'))
    
    else:
        form = CiudadForm()
    

    return render(request, 'persona/create_ciudades.html', {'form':form})


def new_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            docd = Tdocumento.objects.get()
            ciudadx = Ciudad.objects.get()
            nombrex = form.cleaned_data['nombres']
            apellidox = form.cleaned_data['apellidos']
            documentox = form.cleaned_data['documento']
            fechanacimientox = form.cleaned_data['fechanacimiento']
            emailx = form.cleaned_data['email']
            telefonox = form.cleaned_data['telefono']
            usuariox = form.cleaned_data['usuario']
            passwordx = form.cleaned_data['password']
            persona = Persona(idtipoDocumento= docd, ciudad= ciudadx, nombres=nombrex, apellidos = apellidox, documento =documentox, fechanacimiento=fechanacimientox, email = emailx,telefono=telefonox, usuario=usuariox,password=passwordx)
            persona.save()
            return HttpResponseRedirect(reverse('personas'))

    else:
        form = PersonaForm()

    return render(request, 'persona/create_personas.html', {'form': form})

def edit_persona(request, id_persona):
    persona = Persona.objects.filter(id=id_persona).first()
    form = PersonaForm(instance=persona)
    return render(request, "persona/edit_personas.html", {'form': form, "persona":persona})


def actualizar_persona(request, id_persona):
    persona = Persona.objects.get(pk=id_persona)
    form = PersonaForm(request.POST, instance=persona)
    if form.is_valid():
        form.save()
    personas = Persona.objects.all()
    template = loader.get_template('persona/personas.html')
    context = {'personas': personas, }
    return HttpResponse(template.render(context, request))

def eliminar_tdocumento(request, id_tdocumento):
    tdocumento = Tdocumento.objects.get(pk=id_tdocumento)
    tdocumento.delete()
    tdocumento = Tdocumento.objects.all()
    template = loader.get_template('persona/tdocumento.html')
    context = {
        'tdocumento': tdocumento,
        'mensaje' : 'OK',
        }
    return HttpResponse(template.render(context, request))

def eliminar_persona(request, id_persona):
    persona = Persona.objects.get(pk=id_persona)
    persona.delete()
    personas = Persona.objects.all()
    template = loader.get_template('persona/personas.html')
    context = {
        'personas': personas,
        'mensaje' : 'OK',
        }
    return HttpResponse(template.render(context, request))

def eliminar_ciudad(request, id_ciudad):
    ciudad = Ciudad.objects.get(pk=id_ciudad)
    ciudad.delete()
    ciudades = Ciudad.objects.all()
    template = loader.get_template('persona/ciudades.html')
    context = {
        'ciudades': ciudades,
        'mensaje' : 'OK',
        }
    return HttpResponse(template.render(context, request))
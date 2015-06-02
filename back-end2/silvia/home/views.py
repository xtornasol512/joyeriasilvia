# -*- coding: utf-8 -*-
#http y redireccionamientos
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301

#autentificacion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from almacen.models import Joya
from temporales.models import CarroTemporal
from clientes.models import Cliente

def index(request):
    usuario=request.user
    if usuario.is_anonymous():
        if request.method=='POST':
            formulario=AuthenticationForm(request.POST)
            #solicitud de login por post
            if formulario.is_valid:
                usuariof=request.POST['username']
                clavef=request.POST['password']
                acceso=authenticate(username=usuariof,password=clavef)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        #Pantalla del Perfil
                        return HttpResponseRedirect('/home')
                    else:
                        error="Posiblemente tu usuario este baneado o desactivado, comunicate con el administrador"
                else:
                    error="El usuario no existe, verifique que este bien escrito"
            else:
                error="Datos invalidos en el formulario"
            ctx={'formulario':formulario, 'error':error}
            return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))
        else:
            #Login
            formulario=AuthenticationForm()
            ctx={'formulario':formulario}
            return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/home')

@login_required(login_url='/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def home_v(request):
    ctx={}
    return render_to_response('home/home.html', ctx,
                          context_instance=RequestContext(request))

@login_required(login_url='/')
def venta(request):
    error=''
    idCliente=request.GET.get('idCliente','')
    carroTems=CarroTemporal.objects.all()
    if carroTems:
        carro=carroTems[0]
    else:
        carro=None
    if idCliente:
        try:
            clien=Cliente.objects.get(id=idCliente)
        except  :
            clien=None
            error='Clave de Cliente no identificada'
        if clien:
            if carro:
                carro.cliente=clien
                carro.save()
            else:
                carro=CarroTemporal()
                carro.cliente=clien
                carro.save()
    listaJoyas=Joya.objects.filter(en_carro=True)


    ctx={'carro':carro, 'error':error,'lista':listaJoyas}
    return render_to_response('home/ventas.html', ctx,
                          context_instance=RequestContext(request))

@login_required(login_url='/')
def ventaAdd(request):
    admin = request.GET.get('admin','')
    add = request.GET.get('add','')
    dell = request.GET.get('del','')
    if admin:
        jId=None
        if add:
            jId=add
        if dell:
            jId=dell
        try:
            joya=Joya.objects.get(id=jId)
        except :
            joya=None
        if joya and add:
            joya.en_carro=True
            joya.save()
        if joya and dell:
            joya.en_carro=False
            joya.save()
        return HttpResponseRedirect('/admin/almacen/joya/')
    else:
        ctx={}
        return render_to_response('home/home.html', ctx,
                          context_instance=RequestContext(request))

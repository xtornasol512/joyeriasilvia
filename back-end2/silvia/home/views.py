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
def home(request):
    ctx={}
    return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))

@login_required(login_url='/')
def venta(request):
    ctx={}
    return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))
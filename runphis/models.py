from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class nk(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	movil = models.CharField(max_length=30)

class perfilnk(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	movil = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	codigo = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre + '- by ' + self.user.username


class cuentas(models.Model):
	correo = models.CharField(max_length=300)
	passwordi = models.CharField(max_length=300)
	codigo = models.CharField(max_length=300)
	def __str__(self):
		return self.correo

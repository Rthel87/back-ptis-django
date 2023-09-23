from django.db import models

# Create your models here.
class Rol(models.Model):
    rol = models.CharField(max_length=200)
    rango = models.IntegerField()
    borrado = models.BooleanField()
    deleted_at = models.DateTimeField()
    created_at: = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    nombre = models.CharField(max_length=254)
    apellido_paterno = models.CharField(max_length=254)
    apellido_materno = models.CharField(max_length=254)
    run = models.CharField(max_length=12)
    correo_elec = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    rol = models.ForeingKey(Rol)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Group(models.Model):
    nombre = models.CharField(max_length=254)
    proyecto = models.TextField()
    correlativo = models.IntegerField()
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    iniciales = models.CharField(max_length=3)
    usuario = models.ForeingKey(Usuario)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Stakeholder(models.Model):
    iniciales = models.CharField(max_length=3)
    usuario = models.ForeingKey(Usuario)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(Group)

class WorkingDay(models.Model):
    nombre = models.CharField(max_length=254)
    identificador = models.IntegerField()
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

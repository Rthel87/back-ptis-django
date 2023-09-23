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
    user = models.ForeingKey(User)
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

class Semester(models.Model):
    numero = models.IntegerField()
    agno = models.IntegerField()
    inicio = models.DateField()
    fin = models.DateField()
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    nombre = models.CharField(max_length=254)
    codigo = models.CharField(max_length=3)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Teacher(models.Model):
    user = models.ForeingKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Section(models.Model):
    codigo = models.CharField(10)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    working_day = models.ForeingKey(WorkingDay)
    semester = models.ForeingKey(Semester)
    course = models.ForeingKey(Course)
    teachers = models.ManyToManyField(Teacher)

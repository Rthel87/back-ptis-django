from django.db import models

# Create your models here.
class Rol(models.Model):
    rol = models.CharField(max_length=200)
    rango = models.IntegerField(unique=True)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    nombre = models.CharField(max_length=254)
    apellido_paterno = models.CharField(max_length=254)
    apellido_materno = models.CharField(max_length=254)
    run = models.CharField(max_length=12, null=True)
    correo_elec = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Group(models.Model):
    nombre = models.CharField(max_length=254)
    proyecto = models.TextField()
    correlativo = models.IntegerField()
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    iniciales = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Stakeholder(models.Model):
    iniciales = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(Group)

class WorkingDay(models.Model):
    nombre = models.CharField(max_length=254)
    identificador = models.IntegerField(unique=True)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Semester(models.Model):
    numero = models.IntegerField()
    agno = models.IntegerField()
    inicio = models.DateField()
    fin = models.DateField()
    activo = models.BooleanField(default=True)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    nombre = models.CharField(max_length=254)
    codigo = models.CharField(max_length=3, unique=True)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Section(models.Model):
    codigo = models.CharField(max_length=10)
    borrado = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    working_day = models.ForeignKey(WorkingDay, on_delete=models.PROTECT)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teachers = models.ManyToManyField(Teacher)

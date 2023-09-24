from rest_framework import serializers
from .models import Rol

deletedObj = ('id', 'borrado', 'created_at', 'updated_at', 'deleted_at')
nonDeletedObj = ('id', 'created_at', 'updated_at')

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('id', 'rol', 'rango', 'borrado', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = deletedObj

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nombre', 'apellido_paterno', 'apellido_materno', 'run', 'correo_elec', 'rol', 'borrado', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = deletedObj

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'nombre', 'proyecto', 'correlativo', 'borrado', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = deletedObj

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'iniciales', 'user', 'created_at', 'updated_at')
        read_only_fields = nonDeletedObj

class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = ('id', 'iniciales', 'user', 'groups', 'created_at', 'updated_at')
        read_only_fields = nonDeletedObj

class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = ('id', 'nombre', 'identificador', 'borrado', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = deletedObj

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'numero', 'agno', 'inicio', 'fin', 'borrado', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = deletedObj

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'nombre', 'codigo', 'borrado', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = deletedObj

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'created_at', 'updated_at')
        read_only_fields = nonDeletedObj

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'codigo', 'working_day', 'semester', 'course', 'teachers', 'borrado', 'created_at', 'updated_at', 'deleted_at')
        read_only_fields = deletedObj

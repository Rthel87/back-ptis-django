from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from .models import WorkingDay, Semester, Section
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class ListWorkingDays():
    """
    View to list all working days on de sistem
    Don't work
    """
    permission_classes = [permissions.AllowAny]

    @api_view(['GET'])
    def index(request):
        workingdays = WorkingDay.objects.filter(borrado=False)
        return Response(workingdays.values())


class ListSemesters():
    @api_view(['GET'])
    def index(request):
        semester = Semester.objects.filter(activo=True, borrado=False)
        return Response(semester.values())


class ListSections():
    permission_classes = [permissions.AllowAny]

    @api_view(['GET'])
    def index(request):
        semestre_actual = Semester.objects.filter(activo=True, borrado=False)[:1]
        secciones = Section.objects.filter(semester_id=semestre_actual[0].id, borrado=False)
        return Response(secciones.values())

class ListUsers():
    @api_view(['POST'])
    def login(request):
        try:
            usuario = User.objects.get(email=request.data['auth']['email'])
            auth = authenticate(username=usuario.username, password=request.data['auth']['password'])
            if auth is not None:
                token = RefreshToken.for_user(usuario)
                return Response({'jwt': str(token)})
            else:
                return Response({'error': 'Contraseña errónea'}, status=422)
        except ObjectDoesNotExist:
            return Response({'error': 'No existe el usuario'}, status=422)

    @api_view(['GET'])
    def user(request):
        header = request.META['HTTP_AUTHORIZATION']
        token = header.split()
        if token[0] != 'Bearer':
            return Response({'error': ''})
        
        # print(header.split())
        return Response(request.META['HTTP_AUTHORIZATION'])

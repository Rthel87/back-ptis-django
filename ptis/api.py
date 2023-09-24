from rest_framework import viewsets, permissions
from .models import Rol
from .serializers import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RolSerializer

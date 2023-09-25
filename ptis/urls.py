from rest_framework import routers
from .api import RolViewSet, UserViewSet, StudentViewSet

router = routers.DefaultRouter()

router.register('roles', RolViewSet, 'roles')
router.register('estudiantes', StudentViewSet, 'estudiantes')
router.register('usuarios', UserViewSet, 'usuarios')

urlpatterns = router.urls

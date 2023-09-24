from rest_framework import routers
from .api import RolViewSet, StudentViewSet

router = routers.DefaultRouter()

router.register('roles', RolViewSet, 'roles')
router.register('estudiantes', StudentViewSet, 'estudiantes')

urlpatterns = router.urls

from rest_framework import routers
from .api import RolViewSet

router = routers.DefaultRouter()

router.register('roles', RolViewSet, 'roles')

urlpatterns = router.urls

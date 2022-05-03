from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from tools_manager.views import MaterialViewSet, MaterialTypeViewSet, EntityViewSet, EntityTypeViewSet, UserViewSet

router = routers.SimpleRouter()
router.register('material', MaterialViewSet, basename='material')
router.register('materialtype', MaterialTypeViewSet, basename='materialtype')
router.register('entity', EntityViewSet, basename='entity')
router.register('entitytype', EntityTypeViewSet, basename='entitytype')
router.register('material', MaterialViewSet, basename='material')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

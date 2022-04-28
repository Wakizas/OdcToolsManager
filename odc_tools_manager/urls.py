from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from tools_manager.views import MaterialViewSet

router = routers.SimpleRouter()
router.register('material', MaterialViewSet, basename='material')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

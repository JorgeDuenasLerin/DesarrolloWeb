from django.urls import path, include
from rest_framework import routers
from incidencias import views

router = routers.DefaultRouter()
router.register(r'incidencia', views.IncidenciaViewSet)


from . import views

urlpatterns = [
    path('api/', include(router.urls)),
]

from django.urls import path
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]

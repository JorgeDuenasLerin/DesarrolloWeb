from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

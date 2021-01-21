from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .models import Question
from .serializers import QuestionSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer
    #permission_classes = [permissions.IsAuthenticated]

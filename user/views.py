from django.http import HttpResponse
from user.models import CustomUser
from user.forms import CustomUserCreationForm
import json
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class SignUp(APIView):
    permission_classes = ()

    def post(self, request):
        form = CustomUserCreationForm(request.data)

        if form.is_valid():
            form.save()
        
        return Response(form.is_valid())

        '''
        {
            "username": "abc"
            "password1": "enaek123",
            "password2": "enaek123",
            "name": "Keane"
        }
        '''
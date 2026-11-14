from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializer import UserSerializer

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serailizer_instance = UserSerializer(data=form_data)

        if serailizer_instance.is_valid():

            serailizer_instance.save()

            return Response(serailizer_instance.data)

        else :

            return Response(serailizer_instance.errors)
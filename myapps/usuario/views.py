from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from myapps.usuario.forms import RegistroForm
from rest_framework.views import APIView
from myapps.usuario.serializer import UserSerializer
from django.http import HttpResponse
import json

# Create your views here.

class RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('login')

class UserAPI(APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')

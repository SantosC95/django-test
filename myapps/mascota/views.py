from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapps.mascota.forms import MascotaForm
from myapps.mascota.models import Mascota
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers


# Create your views here.

def index(request):
    return render(request,'mascota/index.html')

# Funcion para crear nueva mascota
def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    else:
        form = MascotaForm()
        return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by("id") # Query set to Database
    datos = {'mascotas':mascota} # Save in a dictionary
    return render(request,'mascota/mascota_list.html', datos)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == "GET":
        form = MascotaForm(instance=mascota)
    else: 
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect("mascota:mascota_listar")
    return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request,'mascota/mascota_delete.html',{'mascota':mascota})

# VISTAS BASADAS EN CLASES
# Django cuenta con clases genericas para crear, listar, actualizar y borrar
# Clase de listado
class MascotaList(ListView):
    model = Mascota # El modelo debe ser model
    template_name = 'mascota/mascota_list.html' # deber ser template_name
    paginate_by = 2 # Paginate_by define cuantos elementos por pagina

# Clase para crear
class MascotaCreate(CreateView):
    model = Mascota # El modelo debe ser model
    form_class = MascotaForm # Debe ser form_class
    template_name = 'mascota/mascota_form.html' # deber ser template_name
    success_url = reverse_lazy('mascota:mascota_listar')

# Clase para actualizar 
class MascotaUpdate(UpdateView):
    model = Mascota # El modelo debe ser model
    form_class = MascotaForm # Debe ser form_class
    template_name = 'mascota/mascota_form.html' # deber ser template_name
    success_url = reverse_lazy('mascota:mascota_listar')

# Clase para eliminar 

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html' # deber ser template_name
    success_url = reverse_lazy('mascota:mascota_listar')

def listado (request):
    lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre', 'persona'])
    return HttpResponse(lista, content_type='application/json')
from django.conf.urls import url
from myapps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^index$',index),
	url(r'^solicitud/listar$', login_required(SolicitudList.as_view()), name='solicitud_listar'),
	url(r'^solicitud/nuevo$', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
	url(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
	url(r'^solicitud/eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()), name='solicitud_delete'),


]

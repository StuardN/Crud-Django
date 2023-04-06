from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from Crud.forms import BusesForm
from Crud.models import Buses

def Inicio(request):
    data ={
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


class BusLis(ListView):
    template_name = "buses/listBus.html"
    context_object_name = 'buses'
    model = Buses

    # queryset = Cliente.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancelar_url'] = '/'
        context['crear_url'] = '/crearBuses'
        context['titulo'] = 'LISTADO DE LOS BUSES'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearBus(CreateView):
    model = Buses
    template_name = "buses/crearBus.html"
    success_url = reverse_lazy('listaBuses')
    form_class = BusesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'NUEVO BUS'
        context['url_anterior'] = ''
        context['listar_url'] = '/'
        return context

class ActualizarBuses(UpdateView):
    model = Buses
    template_name = "buses/crearBus.html"
    success_url = reverse_lazy('listaBuses')
    form_class = BusesForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR BUSES'
        context['listar_url'] = '/listaBuses'
        return context

class EliminarBus(DeleteView):
    model = Buses
    template_name = "buses/deleteBus.html"
    success_url = reverse_lazy('listaBuses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE BUS'
        context['listar_url'] = '/listaBuses'
        return context
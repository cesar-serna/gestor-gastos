from .models import Gasto
from .forms import GastoForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.utils import timezone
# Create your views here.
class GastoListView(LoginRequiredMixin, ListView):
    model = Gasto
    template_name = "gasto_list.html"
    context_object_name = "gastos"
    template_name = "gasto_list.html"
    
    def get_queryset(self):
        hoy = timezone.localtime()
        mes_solicitado = self.request.GET.get('mes', hoy.month)
        anio_solicitado = self.request.GET.get('anio', hoy.year)
        
        return Gasto.objects.filter(
            usuario=self.request.user,
            fecha__month=mes_solicitado,
            fecha__year=anio_solicitado
            )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        mis_gastos = self.get_queryset()
        
        total = mis_gastos.aggregate(Sum('monto'))
        
        context['total_gastado'] = total['monto__sum'] or 0
        
        return context
    
class GastoCreateView(LoginRequiredMixin, CreateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy("gasto_list")
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class GastoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gasto
    form_class = GastoForm
    template_name = "gastos/gasto_form.html"
    context_object_name = "gasto"
    success_url = reverse_lazy("gasto_list")
    
    def test_func(self):
        gasto = self.get_object()
        return gasto.usuario == self.request.user
    
class GastoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gasto
    context_object_name = "gasto"
    template_name = "gastos/gasto_confirm_delete.html"
    success_url = reverse_lazy("gasto_list")
    
    def test_func(self):
        gasto = self.get_object()
        return gasto.usuario == self.request.user
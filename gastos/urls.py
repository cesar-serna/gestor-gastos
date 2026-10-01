from django.urls import path
from . import views

urlpatterns = [
    path('', views.GastoListView.as_view(), name='gasto_list'),
    path('nuevo/', views.GastoCreateView.as_view(), name='gasto_create'),
    path('editar/<int:pk>/', views.GastoUpdateView.as_view(), name='gasto_update'),
    path('borrar/<int:pk>/', views.GastoDeleteView.as_view(), name='gasto_delete'),
]
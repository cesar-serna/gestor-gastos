from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"api/gastos", views.GastoViewSet, basename="api-gastos")

urlpatterns = [
    path('', views.GastoListView.as_view(), name='gasto_list'),
    path('nuevo/', views.GastoCreateView.as_view(), name='gasto_create'),
    path('editar/<int:pk>/', views.GastoUpdateView.as_view(), name='gasto_update'),
    path('borrar/<int:pk>/', views.GastoDeleteView.as_view(), name='gasto_delete'),
    path('', include(router.urls))
]
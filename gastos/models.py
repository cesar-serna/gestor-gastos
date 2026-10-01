from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Gasto(models.Model):
    concepto = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.concepto
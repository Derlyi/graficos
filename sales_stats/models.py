# sales_stats/models.py
from django.db import models

class SalesStatistics(models.Model):
    class Meta:
        verbose_name = "Estadísticas de Ventas"
        verbose_name_plural = "Estadísticas de Ventas"

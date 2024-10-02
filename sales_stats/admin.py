# admin.py en sales_stats
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from orders.models import Order

class SalesStatsAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('sales-statistics/', self.admin_site.admin_view(self.sales_statistics_view), name='sales_statistics'),
        ]
        return custom_urls + urls

    def sales_statistics_view(self, request):
        total_sales = sum(order.get_total_cost() for order in Order.objects.all())
        context = {
            'total_sales': total_sales,
            'opts': self.model._meta,
            'title': 'Sales Statistics'
        }
        return render(request, 'admin/orders/sales_statistics.html', context)

# Registra el modelo o la clase de administración
admin.site.register(Order, SalesStatsAdmin)

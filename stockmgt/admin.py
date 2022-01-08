from django.contrib import admin
from .models import Stock, Category
from .forms import StockCreateForm

# Register your models here.


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('category', 'item_name', 'quantity')
    list_filter = ('category', )
    form = StockCreateForm
    search_fields = ['category', 'item_name', ]


admin.site.register(Category)
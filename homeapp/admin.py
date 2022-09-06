from django.contrib import admin
from homeapp.models import Portfolio, Contact

# Register your models here.
admin.site.register([Portfolio, Contact])


class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


from django.contrib import admin
from .models import copperProduct
# Register your models here.
class copperProductAdmin(admin.ModelAdmin):
    list_display = ['prd_name','prd_qnty','prd_validity','prd_valid_upto']



admin.site.register(copperProduct,copperProductAdmin)
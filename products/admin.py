from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product
# Register your models here.

# Admin Action Functions
def change_rating(modeladmin, request, queryset):
    queryset.update(rating = 'e')
# Action description
change_rating.short_description = "Mark Selected Products as Excellent"


class ProductA(admin.ModelAdmin):
    list_display=('name','description','mfg_date')
    list_filter = ('mfg_date', )
    actions = [change_rating]
admin.site.register(Product,ProductA)
admin.site.unregister(Group)
admin.site.site_header='Modified from balaji kshirsagar'

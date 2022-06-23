from django.contrib import admin
from .models import Product, StyleOfBeer
from django.utils.safestring import mark_safe
# Register your models here.


admin.site.register(StyleOfBeer)


class ProdAdmin(admin.ModelAdmin):

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')


admin.site.register(Product, ProdAdmin)

from django.contrib import admin
from .models import Product, StyleOfBeer, Comments
from django.utils.safestring import mark_safe
# Register your models here.


admin.site.register(StyleOfBeer)


class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')


admin.site.register(Product, ProdAdmin)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating', 'postAdded')


from django.contrib import admin
from .models import Product, StyleOfBeer, Comment
from django.utils.safestring import mark_safe
# Register your models here.


admin.site.register(StyleOfBeer)


class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["preview"]
    list_display = ['name', 'imageShow', 'manufacturer', 'inStock', 'price', 'quantity']
    list_filter = ['country', 'quantity', 'price']


    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')

    def imageShow(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None

    imageShow.__name__ = "Картинка"


admin.site.register(Product, ProdAdmin)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating', 'postAdded')
    list_filter = ['product', 'postAdded']

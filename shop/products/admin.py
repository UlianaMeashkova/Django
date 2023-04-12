from django.contrib import admin

from products.models import Product, Purchase


class PurchaseAdminInline(admin.StackedInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "color", "description", "created_at")
    fields = ("title", "image", "price", "color", "description", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    inlines = (PurchaseAdminInline,)

    def save_form(self, request, form, change):

        return super().save_form(request, form, change)



@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", "created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "product__title")
    

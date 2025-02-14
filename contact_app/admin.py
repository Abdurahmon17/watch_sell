from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'message')  # Admin panelda ko‘rinadigan ustunlar

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        print(f"Yangi kontakt qo'shildi:\n"
              f"Ism: {obj.name}\n"
              f"Telefon: {obj.phone_number}\n"
              f"Email: {obj.email}\n"
              f"Xabar: {obj.message}")

admin.site.register(Contact, ContactAdmin)

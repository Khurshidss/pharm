from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Medicine, Pharmacy, PharmacyMedicine


class MedicineAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "title",
                    "medicine_type",
                    "manufacturer",
                    )
    list_filter = ("medicine_type",)
    search_fields = ("title",)

    model = Medicine


admin.site.register(Medicine, MedicineAdmin)


class PharmacyAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "name",
                    "phone_number",
                    "district",
                    "address",
                    )
    search_fields = ("name",)
    list_filter = ("district__region",)
    model = Pharmacy
    autocomplete_fields = ("district",)


admin.site.register(Pharmacy, PharmacyAdmin)


class PharmacyMedicineAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "pharmacy",
                    "medicine",
                    "price",
                    )
    search_fields = ("medicine", "pharmacy")
    list_filter = (
    "pharmacy", "pharmacy__district__region", "medicine__medicine_type")
    model = PharmacyMedicine


admin.site.register(PharmacyMedicine, PharmacyMedicineAdmin)


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    fieldsets = (
        (
            None,
            {
                "fields": ("username","password")
            },
        ),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username', 'password1',
                    'password2',),
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),

    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

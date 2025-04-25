from django.contrib import admin

from .models import UserAccount,Blog
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = UserAccount
    list_display = ('username', 'name', 'phone', 'email', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'email', 'aadhar_no', 'addhar_card', 'bank_pass_book')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'phone', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'name', 'phone', 'email')
    ordering = ('username',)

admin.site.register(UserAccount, CustomUserAdmin)

admin.site.register(Blog)
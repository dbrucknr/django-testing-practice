from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

from .models import Account

admin.site.unregister(Group)

@admin.register(Account)
class AccountAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
        'last_login'
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        superuser = request.user.is_superuser
        if not superuser:
            form.base_fields['username'].disabled = True
        return form
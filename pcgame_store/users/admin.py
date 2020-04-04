from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.urls import path
from django.urls import reverse
from django.utils.html import format_html
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    '''
    Define admin model for custom User model with no username field.
    '''

    readonly_fields = [
        'date_joined',
    ]

    fieldsets = (
        (
            None,
            {'fields': ['full_name', 'email', 'password', 'birth_date', 'phone_number', 'nationality', 'is_admin', ]}
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'full_name', 'is_admin',)
    search_fields = ('email', 'full_name')
    ordering = ('email',)


admin.site.unregister(Group)
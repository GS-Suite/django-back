from django.utils.translation import ugettext, ugettext_lazy as _
from accounts.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as UA
from django.contrib import admin
from .models import User


# Register your models here.

class UserAdmin(UA):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username','name', 'email', 'is_active',)
    list_filter = ('username','name', 'email', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','name', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','name', 'password1', 'password2', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    


### register custom user model to admin
admin.site.register(User, UserAdmin)
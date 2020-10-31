from django.contrib.auth.forms import UserCreationForm as UCrF
from django.contrib.auth.forms import UserChangeForm as UChF
from django import forms
from .models import User


class UserCreationForm(UCrF):
    class Meta(UCrF):
        model = User
        fields = ('email', 'name')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control bg-light'


class UserChangeForm(UChF):
    class Meta:
        model = User
        fields = ('email',)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control bg-light'
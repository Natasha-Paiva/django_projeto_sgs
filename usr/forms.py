# -*- coding: utf-8 -*-
from gerencia.usr.models import *
from django.forms import ModelForm, PasswordInput, CharField


class AuthUserModelForm(ModelForm):
    class Meta:
        model = AuthUser

class UserModelForm(ModelForm):
    class Meta:
        model = User

class GroupModelForm(ModelForm):
    class Meta:
        model = Group

# -*- coding: utf-8 -*-

"""
    Formulários utilizados na views.
"""

from models import *
from django.forms import ModelForm


class GrupoModelForm(ModelForm):
    """
        Formulário para adicionar um grupo.
    """
    class Meta:
        """
            A tabela do models que será usada é Grupo 
        """
        model = Grupo

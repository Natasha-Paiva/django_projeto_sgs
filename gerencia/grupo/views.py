# -*- coding: utf-8 -*-

"""
    Views da aplicação gerencia.grupo
"""

# 2010.10.07 - P/Carlos: Creio que pode ser utilizado o do projeto
from models import Grupo

# 2010.10.07 - lrodrigo - importando as configuracoes
from django.conf import settings

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required

from forms import GrupoModelForm
from utils import paginacao


@login_required(redirect_field_name='redirect_to')
def grupos(request):
    """
        Retorna lista de todas as instituições cadastradas
        paginada 20 a 20
    """
    grupos = Grupo.objects.all()
    grupos = paginacao(request, grupos)

    return render_to_response('gerencia/grupo/grupo.html',
                                {'grupos': grupos,
                                 'MEDIA_URL': settings.MEDIA_URL
                                })


@login_required(redirect_field_name='redirect_to')
def adicionar_grupo(request):
    """
        Definição:
 	        - Apresenta uma pagina para o cadastro de instituições
    """
    if request.POST:
        form = GrupoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/grupos/')
        else:
            return HttpResponse(form.errors)
    else:
        form = GrupoModelForm()
        return render_to_response('gerencia/grupo/add_grupo.html',
                                    {'form': form.as_table(),
                                     'MEDIA_URL': settings.MEDIA_URL
                                    })


@login_required(redirect_field_name='redirect_to')
def alterar_grupo(request, codigo):
    """
        Página para alterações de um instituição selecionada
    """
    grupo = get_object_or_404(Grupo, pk=codigo)
    form = GrupoModelForm(request.POST, instance=grupo)
    if form.is_valid():
        grupo = form.save()
        return HttpResponseRedirect('/grupos/')
    else:
        return HttpResponse(form.errors)

def alterar(request, codigo):
    """
        View que dá suporte a view alterar_grupo
    """
    grupo = get_object_or_404(Grupo, pk=codigo)
    form = GrupoModelForm(instance=grupo)

    return render_to_response('gerencia/grupo/alterar_grupo.html',
                                {'grupo': grupo,
                                 'form': form,
                                 'MEDIA_URL': settings.MEDIA_URL
                                })

@login_required(redirect_field_name='redirect_to')
def apagar_grupo(request, codigo):
    """
        Apagar uma instituição previamente selecionada
    """
    grupo = get_object_or_404(Grupo, pk=codigo)
    grupo.delete()
    return HttpResponseRedirect('/grupos/')



@login_required(redirect_field_name='redirect_to')
def dados_grupo(request, codigo):
    """
        Exibe os dados de uma instituição previamente
        escolhida
    """
    grupo = get_object_or_404(Grupo, pk=codigo)

    return render_to_response('gerencia/grupo/dados_grupo.html',
                                {'grupo': grupo,
                                 'MEDIA_URL': settings.MEDIA_URL
                                })

#Buscas

@login_required(redirect_field_name='redirect_to')
def search(request):
    """
      Procura por uma determinada instituição
    """
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(descricao__icontains=query) |
            Q(nome__icontains=query)
        )
        results = grupo.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("gerencia/grupo/grupo_busca.html", {
        "results": results,
        "query": query,
        'MEDIA_URL': settings.MEDIA_URL
    })

# -*- coding: utf-8 -*-
# Create your views here.

from gerencia.usr.models import *

from django.conf import settings
from django.template import Context, loader
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django import forms
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,  UserManager
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.db.models import Q

#from forms import AuthUserModelForm, UserModelForm, GroupModelForm

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/main_page/')
        else:
            print 'Conta não existe.'
    else:
        print 'Login ou senha invalida.'

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')

def main_page(request):
    template = loader.get_template('default.html')
    variables = Context({ 'user': request.user, 'MEDIA_URL': settings.MEDIA_URL})
    output = template.render(variables)
    return HttpResponse(output)

@login_required(redirect_field_name='redirect_to')
def mostra_dados_user(request, id):
    user = get_object_or_404(User, pk=id)

    f = UserModelForm(instance=user)

    return render_to_response('gerencia/user_dados.html', {'form':f.as_table(), 'id':id, 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def index(request):
    user = AuthUser.objects.all() #Pegamos todos os hosts cadastrados
    paginator = Paginator(user, 20)

    try:
        page = int(request.GET.get('page', '1'))

    except ValueError:
        page = 1


    try:
        lista1 = paginator.page(page)

    except (EmptyPage, InvalidPage):
        lista1= paginator.page(paginator.num_pages)

    t = loader.get_template('gerencia/userindex.html') #indica o template
    c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL}) #cria uma variável “lista” para o template
    return HttpResponse(t.render(c)) #renderiza o template


@login_required(redirect_field_name='redirect_to')
def add_user(request):
    if request.POST:
        f = UserModelForm(request.POST)
        if f.is_valid():
            c = f.save()
            return HttpResponseRedirect('/userindex/')
        else:
            return HttpResponse(f.errors)
    else:
        f = UserModelForm()
        return render_to_response('gerencia/adicionar_user.html', {'form':f.as_table(), 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def alterar_user(request, id):
    user= get_object_or_404(User, pk=id)
    f = UserModelForm(request.POST, instance=user)
    if f.is_valid():
        user= f.save()
        return HttpResponseRedirect('/userindex/')
    else:
        return HttpResponse(f.errors)

@login_required(redirect_field_name='redirect_to')
def apagar_user(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return HttpResponseRedirect('/userindex/')



###############
###### Parte do grupo
###############
@login_required(redirect_field_name='redirect_to')
def mostra_dados_group(request, id):
    group = get_object_or_404(Group, pk=id)

    f = GroupModelForm(instance=group)

    return render_to_response('gerencia/group_dados.html', {'form':f.as_table(), 'id':id, 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def group_index(request):
    group = AuthGroup.objects.all() #Pegamos todos os hosts cadastrados
    paginator = Paginator(group, 20)

    try:
        page = int(request.GET.get('page', '1'))

    except ValueError:
        page = 1


    try:
        lista1 = paginator.page(page)

    except (EmptyPage, InvalidPage):
        lista1= paginator.page(paginator.num_pages)

    t = loader.get_template('gerencia/groupindex.html') #indica o template
    c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL}) #cria uma variável “lista” para o template
    return HttpResponse(t.render(c)) #renderiza o template


@login_required(redirect_field_name='redirect_to')
def add_group(request):
    if request.POST:
        f = GroupModelForm(request.POST)
        if f.is_valid():
            c = f.save()
            return HttpResponseRedirect('/userindex/')
        else:
            return HttpResponse(f.errors)
    else:
        f = GroupModelForm()
        return render_to_response('gerencia/adicionar_group.html', {'form':f.as_table(), 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def alterar_group(request, id):
    group= get_object_or_404(Group, pk=id)
    f = GroupModelForm(request.POST, instance=group)
    if f.is_valid():
        group= f.save()
        return HttpResponseRedirect('/userindex/')
    else:
        return HttpResponse(f.errors)

@login_required(redirect_field_name='redirect_to')
def apagar_group(request, id):
    group = get_object_or_404(Group, pk=id)
    group.delete()
    return HttpResponseRedirect('/userindex/')


##
#Buscas
##
@login_required(redirect_field_name='redirect_to')
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(username__icontains=query) |
            Q(email__icontains=query)
        )
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("gerencia/userbusca.html", {
        "results": results,
        "query": query,
        'MEDIA_URL': settings.MEDIA_URL
    })


class AuthUserModelForm(ModelForm):
    class Meta:
        model = AuthUser

class UserModelForm(ModelForm):
    class Meta:
        model = User

class GroupModelForm(ModelForm):
    class Meta:
        model = Group

# -*- coding: utf-8 -*-

from gerencia.hosts2.models import *
from django.conf import settings

from django.template import Context, loader
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(redirect_field_name='redirect_to')
def index(request):
    hosts = Hosts.objects.all() #Pegamos todos os hosts cadastrados
    paginator = Paginator(hosts, 20)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        lista1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista1= paginator.page(paginator.num_pages)

    t = loader.get_template('gerencia/hosts2/hosts_index.html')
    c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL})
    return HttpResponse(t.render(c))


@login_required(redirect_field_name='redirect_to')
def adicionar_host(request):
    if request.POST:
        f = HostsModelForm(request.POST)
        if f.is_valid():
            c = f.save()
            return HttpResponseRedirect('/hostsindex/')
        else:
            return HttpResponse(f.errors)
    else:
        f = HostsModelForm()
        return render_to_response('gerencia/hosts2/adicionar_hosts.html', {'form': f.as_table(),'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def alterar_host(request, codigo):
    host = get_object_or_404(Hosts, pk = codigo)

    form = HostsModelForm(request.POST, instance = host)
    if form.is_valid():
        host = form.save()
        return HttpResponseRedirect('/hostsindex/')
    else:
        return HttpResponse(form.errors)

@login_required
def host_alterar(request, codigo):
    host = get_object_or_404(Hosts, pk = codigo)
    form = HostsModelForm(instance = host)

    return render_to_response('gerencia/hosts2/alterar_host.html', {'host': host, 'form': form, 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def apagar_host(request, codigo):
    hosts = get_object_or_404(Hosts, pk = codigo)
    hosts.delete()
    return HttpResponseRedirect('/hostsindex/')

@login_required(redirect_field_name='redirect_to')
def mostra_dados_host(request, codigo):
    host = get_object_or_404(Hosts, pk = codigo)

    form = HostsModelForm(instance = host)

    return render_to_response('gerencia/hosts2/dados_host.html', {'form':form.as_table(), 'host': host, 'codigo':codigo, 'MEDIA_URL': settings.MEDIA_URL})


@login_required(redirect_field_name='redirect_to')
def index_tipohost(request):
    tipohost = Tipohost.objects.all() #Pegamos todos os hosts cadastrados
    paginator = Paginator(tipohost, 20)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        lista1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista1= paginator.page(paginator.num_pages)

    t = loader.get_template('gerencia/hosts2/tipo_host.html')
    c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL})
    return HttpResponse(t.render(c))

@login_required(redirect_field_name='redirect_to')
def adicionar_tipohost(request):
    if request.POST:
        f = TipohostModelForm(request.POST)
        if f.is_valid():
            c = f.save()
            return HttpResponseRedirect('/tipohost/')
        else:
            return HttpResponse(f.errors)
    else:
        f = TipohostModelForm()
        return render_to_response('gerencia/hosts2/adicionar_tipo_host.html', {'form': f.as_table(), 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def alterar_tipo_host(request, codigo):
    tipohost = get_object_or_404(Tipohost, pk = codigo)

    f = TipohostModelForm(request.POST, instance=tipohost)
    if f.is_valid():
        tipohost = f.save()
        return HttpResponseRedirect('/tipohost/')
    else:
        return HttpResponse(f.errors)

@login_required
def tipo_host_alterar(request, codigo):
    tipo = get_object_or_404(Tipohost, pk = codigo)
    form = TipohostModelForm(instance = tipo)

    return render_to_response('gerencia/hosts2/alterar_tipo_host.html',
                                {'tipo': tipo,
                                 'form': form,
                                 'MEDIA_URL': settings.MEDIA_URL
                                })

@login_required(redirect_field_name='redirect_to')
def apagar_tipohost(request, codigo):
    tipohost = get_object_or_404(Tipohost, pk=codigo)
    tipohost.delete()
    return HttpResponseRedirect('/tipohost/')

@login_required(redirect_field_name='redirect_to')
def mostra_dados_tipohost(request, codigo):
    tipo = get_object_or_404(Tipohost, pk = codigo)

    form = TipohostModelForm(instance = tipo)

    return render_to_response('gerencia/hosts2/tipo_host_dados.html', {'tipo': tipo, 'form': form.as_table(), 'codigo':codigo, 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def index_imagem(request):
    imagem = Imagem.objects.all()
    paginator = Paginator(imagem, 20)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        lista1 = paginator.page(page)

    except (EmptyPage, InvalidPage):
        lista1= paginator.page(paginator.num_pages)

    t = loader.get_template('gerencia/hosts2/imagem.html')
    c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL})
    return HttpResponse(t.render(c))

@login_required(redirect_field_name='redirect_to')
def adicionar_imagem(request):
    if request.POST:
        f = ImagemModelForm(request.POST)
        if f.is_valid():
            c = f.save()
            return HttpResponseRedirect('/imagem/')
        else:
            return HttpResponse(f.errors)
    else:
        f = ImagemModelForm()
        return render_to_response('gerencia/hosts2/adicionar_imagem.html', {'form': f.as_table(), 'MEDIA_URL': settings.MEDIA_URL})

@login_required(redirect_field_name='redirect_to')
def alterar_imagem(request, codigo):
    imagem = get_object_or_404(Imagem, pk = codigo)

    f = ImagemModelForm(request.POST, instance = imagem)
    if f.is_valid():
        imagem = f.save()
        return HttpResponseRedirect('/imagem/')
    else:
        return HttpResponse(f.errors)

@login_required(redirect_field_name='redirect_to')
def apagar_imagem(request, codigo):
    imagem = get_object_or_404(Imagem, pk = codigo)
    imagem.delete()
    return HttpResponseRedirect('/imagem/')

@login_required(redirect_field_name='redirect_to')
def mostra_dados_imagem(request, codigo):
    imagem = get_object_or_404(Imagem, pk = codigo)

    f = ImagemModelForm(instance=imagem)

    return render_to_response('gerencia/hosts2/imagem_dados.html', {'form': f.as_table(), 'codigo':codigo, 'MEDIA_URL': settings.MEDIA_URL})

class HostsModelForm(ModelForm):
    class Meta:
        model = Hosts

class TipohostModelForm(ModelForm):
    class Meta:
        model = Tipohost

class ImagemModelForm(ModelForm):
    class Meta:
        model = Imagem

class SnmpinterfacesForm(ModelForm):
    class Meta:
        model = Snmpinterfaces

class SnmpsysForm(ModelForm):
    class Meta:
        model = Snmpsys

class SnmpcpuForm(ModelForm):
    class Meta:
        model = Snmpcpu

class SnmphdForm(ModelForm):
    class Meta:
        model = Snmphd

#Buscas

@login_required(redirect_field_name='redirect_to')
def busca(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fqdn__icontains=query) |
            Q(vlip__icontains=query)
        )
        results = Hosts.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response("gerencia/hosts2/busca.html",
                                {
                                    "results": results,
                                    "query": query,
                                    "MEDIA_URL": settings.MEDIA_URL
                                })


# Relatórios

#@login_required(redirect_field_name='redirect_to')
def relatorioindex(request):
    t = loader.get_template('gerencia/hosts2/snmp_index.html')
    c = Context ({'MEDIA_URL': settings.MEDIA_URL})
    return HttpResponse(t.render(c))


#@login_required(redirect_field_name='redirect_to')
def sys(request):
	sys = Snmpsys.objects.all()
	paginator = Paginator(sys, 15)

	try:
	  page = int(request.GET.get('page', '1'))
	except ValueError:
	  page = 1

	try:
	  lista1 = paginator.page(page)
	except (EmptyPage, InvalidPage):
	  lista1= paginator.page(paginator.num_pages)

	t = loader.get_template('gerencia/hosts2/hosts_sys.html') #indica o template
	c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL}) #cria uma variável “lista” para o template
	return HttpResponse(t.render(c)) #renderiza o template



#@login_required(redirect_field_name='redirect_to')
def hostsinterfaces(request):
    interface= Snmpinterfaces.objects.all()
    paginator = Paginator(interface, 20)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        lista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista= paginator.page(paginator.num_pages)


    t = loader.get_template('gerencia/hosts2/hosts_interfaces.html') #indica o template
    c = Context ({'lista': lista, 'MEDIA_URL': settings.MEDIA_URL}) #cria uma variável “lista” para o template
    return HttpResponse(t.render(c)) #renderiza o template

#@login_required(redirect_field_name='redirect_to')
def cpu(request):
	cpu = Snmpcpu.objects.all()
	paginator = Paginator(cpu, 20)

	try:
	  page = int(request.GET.get('page', '1'))
	except ValueError:
	  page = 1

	try:
	  lista1 = paginator.page(page)
	except (EmptyPage, InvalidPage):
	  lista1= paginator.page(paginator.num_pages)

	t = loader.get_template('gerencia/hosts2/cpu.html') #indica o template
	c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL}) #cria uma variável “lista” para o template
	return HttpResponse(t.render(c)) #renderiza o template

#@login_required(redirect_field_name='redirect_to')
def hd(request):
	hd = Snmphd.objects.all()
	paginator = Paginator(hd, 20)

	try:
	  page = int(request.GET.get('page', '1'))
	except ValueError:
	  page = 1

	try:
	  lista1 = paginator.page(page)
	except (EmptyPage, InvalidPage):
	  lista1= paginator.page(paginator.num_pages)

	t = loader.get_template('gerencia/hosts2/hd.html') #indica o template
	c = Context ({'lista': lista1, 'MEDIA_URL': settings.MEDIA_URL}) #cria uma variável “lista” para o template
	return HttpResponse(t.render(c)) #renderiza o template

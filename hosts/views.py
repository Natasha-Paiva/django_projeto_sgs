# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

import time
import datetime

from time import gmtime
from datetime import date

from models import Hosts, Redes, Usr
from utils import paginacao, nome_redes, trata_dados_do_host, define_filtro


def hosts(request, pagina = 0):

    filtro = request.GET.get('filtro', None)
    hosts = define_filtro(request)

    i = 0
    while i < len(hosts):
        # Acrescentando a hosts o índice dsrede que foi pego na tabela Redes
        hosts[i]['dsrede'] = \
            Redes.objects.values("dsrede").filter(cdrede = hosts[i]['cdrede'])
        hosts[i]['dsrede'] = hosts[i]['dsrede'][0]['dsrede']
        i = i + 1

    rede = list()
    hosts = paginacao(request, hosts)
    redes = nome_redes(request)

    return render_to_response ("hosts/hosts.html",
        {'hosts': hosts,
         'rede': rede,
         'redes': redes,
         'filtro': filtro,
         'MEDIA_URL': settings.MEDIA_URL})

def relatorio_uptime(request):

    filtro = request.GET.get('filtro', None)
    rede = list()

    hosts = define_filtro(request).filter(dsstatus = 1)
    for host in hosts:
        try:
            uptime = gmtime(host["tmanterior"])
            #hora_atual = int(time.time())
            #host["minutos"] = hora_atual - host["tmanterior"]

            agora = datetime.datetime.now()
            anterior = time.localtime(host["tmanterior"])

            host["tempo"] = date(agora.year, agora.month, agora.day) - date(anterior.tm_year, anterior.tm_mon, anterior.tm_mday)
            host["tempo"] = str(host["tempo"]).replace("0", "").replace("days,", "dias").replace(":","").replace("day,", "dia")
            host.save()
        except:
            pass

    i = 0
    while i < len(hosts):
        # Acrescentando a hosts o índice dsrede que foi pego na tabela Redes
        hosts[i]['dsrede'] = \
            Redes.objects.values("dsrede").filter(cdrede = hosts[i]['cdrede'])
        hosts[i]['dsrede'] = hosts[i]['dsrede'][0]['dsrede']
        i = i + 1

    hosts = paginacao(request, hosts)
    redes = nome_redes(request)

    return render_to_response ("hosts/uptime.html",
        {"hosts": hosts,
         "uptime": uptime,
         "rede": rede,
         "redes": redes,
         "filtro": filtro,
         "MEDIA_URL": settings.MEDIA_URL})

def relatorio_downtime(request):

    filtro = request.GET.get('filtro', None)
    rede = list()
    hosts = define_filtro(request).filter(dsstatus=0)
    for host in hosts:
        try:
            #hora_atual = int(time.time())
            #host["minutos"] = hora_atual - host["tmatual"]
            downtime = gmtime(host["tmatual"])

            agora = datetime.datetime.now()
            atual = time.localtime(host["tmatual"])

            host["tempo"] = date(agora.year, agora.month, agora.day) - date(atual.tm_year, atual.tm_mon, atual.tm_mday)
            host["tempo"] = str(host["tempo"]).replace("0", "").replace("days,", "dias").replace(":","")
            host.save()

        except:
            pass

    i = 0
    while i < len(hosts):
        # Acrescentando a hosts o índice dsrede que foi pego na tabela Redes
        hosts[i]['dsrede'] = \
            Redes.objects.values("dsrede").filter(cdrede = hosts[i]['cdrede'])
        hosts[i]['dsrede'] = hosts[i]['dsrede'][0]['dsrede']
        i = i + 1

    redes = nome_redes(request)
    hosts = paginacao(request, hosts)

    return render_to_response ("hosts/downtime.html",
        {"hosts": hosts,
         "downtime": downtime,
         "rede": rede,
         "redes": redes,
         "filtro": filtro,
         "MEDIA_URL": settings.MEDIA_URL })

def relatorio_ativacao(request):

    filtro = request.GET.get('filtro', None)
    rede = list()

    hosts = define_filtro(request)
    for host in hosts:
        try:
            agora = date.today()
            inicial = time.localtime(host["tminicial"])
            host["tminicial"] = gmtime(host["tminicial"])

            host["tempo"] = date(agora.year, agora.month, agora.day) - date(inicial.tm_year, inicial.tm_mon, inicial.tm_mday)
            host["tempo"] = str(host["tempo"]).replace("0", "").replace("days,", "dias").replace(":","")
            host.save()
        except:
            pass

    i = 0
    while i < len(hosts):
        # Acrescentando a hosts o índice dsrede que foi pego na tabela Redes
        hosts[i]['dsrede'] = \
            Redes.objects.values("dsrede").filter(cdrede = hosts[i]['cdrede'])
        hosts[i]['dsrede'] = hosts[i]['dsrede'][0]['dsrede']
        i = i + 1

    redes = nome_redes(request)
    hosts = paginacao(request, hosts)


    return render_to_response ("hosts/ativacao.html",
        {"hosts": hosts,
         "rede": rede,
         "redes": redes,
         "filtro": filtro,
         "MEDIA_URL": settings.MEDIA_URL})

def relatorio_status(request):

    filtro = request.GET.get('filtro', None)
    rede = list()

    hosts = define_filtro(request)
    for host in hosts:
        host["tmanterior"] = gmtime(host["tmanterior"])

    i = 0
    while i < len(hosts):
        # Acrescentando a hosts o índice dsrede que foi pego na tabela Redes
        hosts[i]['dsrede'] = \
            Redes.objects.values("dsrede").filter(cdrede = hosts[i]['cdrede'])
        hosts[i]['dsrede'] = hosts[i]['dsrede'][0]['dsrede']
        i = i + 1

    redes = nome_redes(request)
    hosts = paginacao(request, hosts)


    return render_to_response ("hosts/status.html",
    {"hosts": hosts,
     "rede": rede,
     "redes": redes,
     "filtro": filtro,
     "MEDIA_URL": settings.MEDIA_URL})

def mapa_simples(request):
    filtro = request.GET.get('filtro', None)
    rede = list()

    hosts = define_filtro(request)

    i = 0
    while i < len(hosts):
        # Acrescentando a hosts o índice dsrede que foi pego na tabela Redes
        hosts[i]['dsrede'] = \
            Redes.objects.values("dsrede").filter(cdrede = hosts[i]['cdrede'])
        hosts[i]['dsrede'] = hosts[i]['dsrede'][0]['dsrede']
        i = i + 1

    redes = nome_redes(request)
    hosts = paginacao(request, hosts)

    return render_to_response ("hosts/mapa_simples.html",
        {'hosts': hosts,
         'redes': redes,
         'filtro': filtro,
         'MEDIA_URL': settings.MEDIA_URL})

def mapa_grupo(request):

    return render_to_response ("hosts/mapa_grupo.html", {
                                               'MEDIA_URL': settings.MEDIA_URL})

def host(request, codigoHost):
    # SELECT * FROM Hosts WHERE cdhost = codigoHost
    # Se não existir nada lança 404.
    host = get_object_or_404(Hosts, pk = codigoHost)

    host = trata_dados_do_host(host)
    redes = nome_redes(request)

    return render_to_response ("hosts/dadosHost.html",
        {"host": host,
         "redes": redes,
         "MEDIA_URL": settings.MEDIA_URL})

def main_page(request):

    template = loader.get_template("principal.html")
    variaveis = Context({'user': request.user})
    output = template.render(variaveis)

    return HttpResponse(output)

def busca(request):
    query = request.GET.get('termoBuscado', '')
    if query:
        qset = (
            Q(dsfqdn__icontains=query) |
            Q(vlip__icontains=query)
        )
        hosts = Hosts.objects.filter(qset).distinct()
    else:
        hosts = []

    return render_to_response('hosts/busca.html',
                                    {'hosts': hosts,
                                     'query': query,
                                     'MEDIA_URL': settings.MEDIA_URL})

def ordena_tipo(request):
    hosts = Hosts.objects.values("cdrede",
                                 "dsstatus",
                                 "dsfqdn",
                                 "vlip",
                                 "cdtipohost",
                                 "cdhost")

    hosts = hosts.ordena_by("cdtipohost")

    i = 0
    while i < len(hosts):
        # Acrescentando a hosts o índice dsrede que foi pego na tabela Redes
        hosts[i]['dsrede'] = \
            Redes.objects.values("dsrede").filter(cdrede = hosts[i]['cdrede'])
        hosts[i]['dsrede'] = hosts[i]['dsrede'][0]['dsrede']
        i = i + 1

    rede = list()
    hosts = paginacao(request, hosts)
    redes = nome_redes(request)

    return render_to_response("hosts/hosts.html",
        {'hosts': hosts,
         'redes': redes,
         'rede': rede,
         'MEDIA_URL': settings.MEDIA_URL})

def default(request):

  return render_to_response("hosts/principal.html",
                                {'MEDIA_URL': settings.MEDIA_URL})

def creditos(request):

  return render_to_response("hosts/creditos.html",
                                {'MEDIA_URL': settings.MEDIA_URL })

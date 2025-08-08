# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from time import gmtime
from models import Redes, Hosts


def define_filtro(request):

    filtro = request.GET.get('filtro', None)

    redes = Redes.objects.values("cdrede")
    hosts = Hosts.objects.values("cdrede",
         "dsstatus",
         "dsfqdn",
         "vlip",
         "tminicial",
         "cdhost",
         "cdtipohost",
         "tmatual",
         "statusmon",
         "tmanterior"
        )

    if filtro is None:
        return hosts

    filtros_possiveis = {
        'ativos': {'dsstatus': 1},
        'inativos': {'dsstatus': 0},
        'ativosderede': {'cdtipohost': 1},
        'workstations': {'cdtipohost': 2},
        'servidores': {'cdtipohost': 3},
        'indefinidos': {'cdtipohost': 4},
        'ativosderede_ativos': {'cdtipohost': 1, 'dsstatus': 1},
        'ativosderede_inativos': {'cdtipohost': 1, 'dsstatus': 0},
        'workstations_ativos': {'cdtipohost': 2, 'dsstatus': 1},
        'workstations_inativos': {'cdtipohost': 2, 'dsstatus': 0},
        'servidores_ativos': {'cdtipohost': 3, 'dsstatus': 1},
        'servidores_inativos': {'cdtipohost': 3, 'dsstatus': 0},
        'indefinido_ativos': {'cdtipohost': 4, 'dsstatus': 1},
        'indefinido_inativos': {'cdtipohost': 4, 'dsstatus': 0},
        }

    for rede in redes:
        filtros_possiveis[str(rede["cdrede"])+"_ativos"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 1}
        filtros_possiveis[str(rede["cdrede"])+"_inativos"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 0}
        filtros_possiveis[str(rede["cdrede"])+"_indefinidos"] = \
            {"cdrede": rede['cdrede'], "cdtipohost": None}
        filtros_possiveis[str(rede["cdrede"])+"_ativosderede"] = \
            {"cdrede": rede['cdrede'], "cdtipohost": 1}
        filtros_possiveis[str(rede["cdrede"])+"_workstations"] = \
            {"cdrede": rede['cdrede'], "cdtipohost": 2}
        filtros_possiveis[str(rede["cdrede"])+"_servidores"] = \
            {"cdrede": rede['cdrede'], "cdtipohost": 3}
        filtros_possiveis[str(rede["cdrede"])+"_ativos_ativosderede"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 1, 'cdtipohost': 1}
        filtros_possiveis[str(rede["cdrede"])+"_inativos_ativosderede"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 0, "cdtipohost": 1}
        filtros_possiveis[str(rede["cdrede"])+"_ativos_workstations"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 1, 'cdtipohost': 2}
        filtros_possiveis[str(rede["cdrede"])+"_inativos_workstations"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 0, "cdtipohost": 2}
        filtros_possiveis[str(rede["cdrede"])+"_ativos_servidores"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 1, 'cdtipohost': 3}
        filtros_possiveis[str(rede["cdrede"])+"_inativos_servidores"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 0, "cdtipohost": 3}
        filtros_possiveis[str(rede["cdrede"])+"_ativos_indefinidos"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 1, 'cdtipohost': None}
        filtros_possiveis[str(rede["cdrede"])+"_inativos_indefinidos"] = \
            {"cdrede": rede['cdrede'], "dsstatus": 0, "cdtipohost": None}

    try:
        filtro = int(filtro)
        return hosts.filter(cdrede=filtro)
    except ValueError:
        if filtro in filtros_possiveis:
            return hosts.filter(**filtros_possiveis[filtro])
        raise Http404

def host(request, codigoHost):
  # SELECT * FROM Hosts WHERE cdhost = codigoHost
  # Se não existir nada lança 404.
  host = get_object_or_404(Hosts, pk = codigoHost)

  host = trata_dados_do_host(host)
  redes = nome_redes(request)

def paginacao(request, hosts):
	#for i in range(len(hosts)):
	  #hosts[i]['vlip'] = hosts[i]['vlip'].replace(".", " ")

	paginacao = Paginator(hosts, 20)

	try:
		pagina = int(request.GET.get('pagina', '1'))
	except ValueError:
		pagina = 1

	try:
		hosts = paginacao.page(pagina)
	except (EmptyPage, InvalidPage):
		hosts = paginacao.page(paginacao.num_pages)

	return hosts

def nome_redes(request):
	#SELECT cdRede, dsRede FROM Redes;
	redes = Redes.objects.values('cdrede', 'dsrede')

	return redes

def trata_dados_do_host(host):
    host.tminicial = gmtime(host.tminicial)
    host.tmatual = gmtime(host.tmatual)
    host.tmanterior = gmtime(host.tmanterior)

    if host.dsstatus == 1:
        host.dsstatus = "Ativo"
    else:
        host.dsstatus = "Inativo"

    if host.statusmon == 1:
        host.statusmon = "Ativo"
    else:
        host.statusmon = "Inativo"

    if host.dsmudancastatus == 1:
        host.dsmudancastatus = "Ativo"
    else:
        host.dsmudancastatus = "Inativo"

    if host.snmp == 1:
        host.snmp = "Ativo"
    else:
        host.snmp = "Inativo"

    return host

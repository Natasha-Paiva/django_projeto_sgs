# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf               import settings

# Uncomment the next two lines to enable the admin:
from django.contrib 		import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^simges/', include('simges.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    (r'^$', 'gerencia.usr.views.main_page'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
            {'template_name': 'registration/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
            {'template_name': 'registration/logout.html'}),


    #relatórios
    #(r'^$', 'hosts.views.default'),
    (r'^hosts/$', 'hosts.views.hosts'),
    (r'^ordena_tipo/$', 'hosts.views.ordena_tipo'),
    (r'^equipe/$', 'hosts.views.creditos'),
    (r'^uptime/$', 'hosts.views.relatorio_uptime'),
    (r'^downtime/$', 'hosts.views.relatorio_downtime'),
    (r'^ativacao/$', 'hosts.views.relatorio_ativacao'),
    (r'^status/$', 'hosts.views.relatorio_status'),
    (r'^mapasimples/$', 'hosts.views.mapa_simples'),
    (r'^mapagrupo/$',    'hosts.views.mapa_grupo'),
    (r'^host/(?P<codigoHost>[\d]+)/$', 'hosts.views.host'),
    (r'^hosts/busca/', 'hosts.views.busca'),

    ##
    # Gerencia
    ##

    # Grupo
    (r'^grupos/$', 'gerencia.grupo.views.grupos'),
    (r'^adicionar_grupo/$', 'gerencia.grupo.views.adicionar_grupo'),
    (r'^apagar_grupo/(?P<codigo>\d+)/$', 'gerencia.grupo.views.apagar_grupo'),
    (r'^dados_grupo/(?P<codigo>\d+)/$', 'gerencia.grupo.views.dados_grupo'),
    (r'^alterar_grupo/(?P<codigo>\d+)/$', 'gerencia.grupo.views.alterar_grupo'),
    (r'^grupo_alterar/(?P<codigo>\d+)/$', 'gerencia.grupo.views.alterar'),

    # Latencia
    (r'^latencia/$', 'gerencia.latencia.views.latencia'),
    (r'^adicionar_latencia/$', 'gerencia.latencia.views.adicionar_latencia'),
    (r'^busca_latencia/$', 'gerencia.latencia.views.search'),
    (r'^busca_hosts_latencia/$', 'gerencia.latencia.views.busca_hosts'),
    (r'^apagar_latencia/(?P<codigo>\d+)/$', 'gerencia.latencia.views.apagar_latencia'),
    (r'^dados_latencia/(?P<codigo>\d+)/$', 'gerencia.latencia.views.dados_latencia'),
    (r'^alterar_latencia/(?P<codigo>\d+)/$', 'gerencia.latencia.views.alterar_latencia'),
    (r'^latencia_alterar/(?P<codigo>\d+)/$', 'gerencia.latencia.views.alterar'),

    # Throughput
    (r'^throughput/$', 'gerencia.throughput.views.throughput'),
    (r'^adicionar_throughput/$', 'gerencia.throughput.views.adicionar_throughput'),
    (r'^busca_throughput/$', 'gerencia.throughput.views.search'),
    (r'^busca_hosts_throughput/$', 'gerencia.latencia.views.busca_hosts'),
    (r'^dados_throughput/(?P<codigo>\d+)/$', 'gerencia.throughput.views.dados_throughput'),
    (r'^alterar_throughput/(?P<codigo>\d+)/$', 'gerencia.throughput.views.alterar_throughput'),
    (r'^throughput_alterar/(?P<codigo>\d+)/$', 'gerencia.throughput.views.alterar'),
    (r'^apagar_throughput/(?P<codigo>\d+)/$', 'gerencia.throughput.views.apagar_throughput'),

    # Gerencia das instituicoes sobre monitoramento
    (r'^instituicaoindex/$',
            'gerencia.instituicao.views.index'),
    (r'^adicionar_instituicao/$',
            'gerencia.instituicao.views.adicionar_instituicao'),
    (r'^mostra_dados_instituicao/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.mostra_dados_instituicao'),
    (r'^apagar_instituicao/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.apagar_instituicao'),
    (r'^alterar_instituicao/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.alterar_instituicao'),
    (r'^instituicao_alterar/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.alterar'),
    (r'^inst_busca/$',
            'gerencia.instituicao.views.search'),

    #Gerencia das redes
    #(r'^rede/$', 'gerencia.redes.views.inicialrede'),
    (r'^redesindex/$',
            'gerencia.redes.views.index'),
    (r'^adicionar_rede/$',
            'gerencia.redes.views.adicionar_redes'),
    (r'^mostra_dados_rede/(?P<codigo>\d+)/$',
            'gerencia.redes.views.mostra_dados_rede'),
    (r'^apagar_rede/(?P<codigo>\d+)/$',
            'gerencia.redes.views.apagar_rede'),
    (r'^alterar_rede/(?P<codigo>\d+)/$',
            'gerencia.redes.views.alterar_rede'),
    (r'^rede_alterar/(?P<codigo>\d+)/$',
            'gerencia.redes.views.alterar'),
    (r'^redes_busca/$',
            'gerencia.redes.views.search'),

    # Gerenciamento dos Hosts detectados via icmp
    (r'^hostsindex/$',
            'gerencia.hosts2.views.index'),
    (r'^adicionar_host/$',
            'gerencia.hosts2.views.adicionar_host'),
    (r'^mostra_dados_host/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.mostra_dados_host'),
    (r'^apagar_host/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.apagar_host'),
    (r'^alterar_host/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.alterar_host'),
    (r'^host_alterar/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.host_alterar'),
    (r'^hostsinterfaces/$',
            'gerencia.hosts2.views.hostsinterfaces'),
    (r'^hostssys/$',
            'gerencia.hosts2.views.sys'),
    (r'^host_busca/$',
            'gerencia.hosts2.views.busca'),

    #ESTACAO DE TRABALHO
    (r'^estsys/$', 'gerencia.estacaodetrabalho.views.index'),
    (r'^esttemperatura/$', 'gerencia.estacaodetrabalho.views.temperatura'),
    (r'^esthd/$', 'gerencia.estacaodetrabalho.views.hd'),

    #USER
    (r'^userindex/$',
            'gerencia.usr.views.index'),
    (r'^add_user/$',
            'gerencia.usr.views.add_user'),
    (r'^mostra_dados_user/(?P<id>\d+)/$',
            'gerencia.usr.views.user_details'),
    (r'^apagar_user/(?P<id>\d+)/$',
            'gerencia.usr.views.apagar_user'),
    (r'^alterar_user/(?P<id>\d+)/$',
            'gerencia.usr.views.alterar_user'),
    (r'^alterar/(?P<id>\d+)/$',
            'gerencia.usr.views.alterar'),
    (r'^user_busca/$',
            'gerencia.usr.views.search'),

    #Grupos
    (r'^groupindex/$',
            'gerencia.usr.views.group_index'),
    (r'^add_group/$',
            'gerencia.usr.views.add_group'),
    (r'^mostra_dados_group/(?P<id>\d+)/$',
            'gerencia.usr.views.mostra_dados_group'),
    (r'^apagar_group/(?P<id>\d+)/$',
            'gerencia.usr.views.apagar_group'),
    (r'^alterar_group/(?P<id>\d+)/$',
            'gerencia.usr.views.alterar_group'),

    #TipoHost
    (r'^tipohost/$',
            'gerencia.hosts2.views.index_tipohost'),
    (r'^adicionar_tipohost/$',
            'gerencia.hosts2.views.adicionar_tipohost'),
    (r'^mostra_dados_tipohost/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.mostra_dados_tipohost'),
    (r'^apagar_tipohost/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.apagar_tipohost'),
    (r'^alterar_tipohost/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.alterar_tipo_host'),
    (r'^tipo_host_alterar/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.tipo_host_alterar'),

    #IMAGEM
    (r'^imagem/$',
            'gerencia.hosts2.views.index_imagem'),
    (r'^adicionar_imagem/$',
            'gerencia.hosts2.views.adicionar_imagem'),
    (r'^mostra_dados_imagem/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.mostra_dados_imagem'),
    (r'^apagar_imagem/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.apagar_imagem'),
    (r'^alterar_imagem/(?P<codigo>\d+)/$',
            'gerencia.hosts2.views.alterar_imagem'),

    #TipoInstituição
    (r'^tipoinst/$',
            'gerencia.instituicao.views.index_tipoinst'),
    (r'^adicionar_tipoinst/$',
            'gerencia.instituicao.views.adicionar_tipo'),
    (r'^mostra_dados_tipoinst/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.mostra_dados_tipo'),
    (r'^apagar_tipo/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.apagar_tipo'),
    (r'^alterar_tipoinst/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.alterar_tipoinst'),
    (r'^tipo_alterar/(?P<codigo>\d+)/$',
            'gerencia.instituicao.views.alterar_tipo'),

    #SNMP
    (r'^snmpindex/$',
            'gerencia.snmp.views.index'),
    (r'^adicionar_snmp/$',
            'gerencia.snmp.views.adicionar_snmp'),
    (r'^mostra_dados_snmp/(?P<codigo>\d+)/$',
            'gerencia.snmp.views.mostra_dados_snmp'),
    (r'^apagar_snmp/(?P<codigo>\d+)/$',
            'gerencia.snmp.views.apagar_snmp'),
    (r'^alterar_snmp/(?P<codigo>\d+)/$',
            'gerencia.snmp.views.alterar_snmp'),

    #Gerencia SNMP Index
    (r'^relatorio_snmp_index/$',
            'gerencia.hosts2.views.relatorioindex'),
    (r'^snmp_cpu/$',
            'gerencia.hosts2.views.cpu'),
    (r'^snmp_hd/$',
            'gerencia.hosts2.views.hd'),

    #i18n/
    (r'^i18n/', include('django.conf.urls.i18n')),

    #arquivos estaticos
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/(.*)', admin.site.root),
)

if settings.LOCAL:
    urlpatterns += patterns(''
        (r'^media/(.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Acao(models.Model):
    cdacao = models.IntegerField(primary_key=True, db_column='cdAcao') # Field name made lowercase.
    dsacao = models.CharField(max_length=30, db_column='dsAcao', blank=True) # Field name made lowercase.
    dsscript = models.CharField(max_length=300, db_column='dsScript', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'acao'

class Alerta(models.Model):
    cdalerta = models.IntegerField(primary_key=True, db_column='cdAlerta') # Field name made lowercase.
    dstipo = models.CharField(max_length=60, db_column='dsTipo', blank=True) # Field name made lowercase.
    dsalvo = models.CharField(max_length=36, db_column='dsAlvo', blank=True) # Field name made lowercase.
    cdacao = models.ForeignKey(Acao, null=True, db_column='cdAcao', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'alerta'

class AlertaDownConfig(models.Model):
    codigo = models.IntegerField(primary_key=True)
    alerta1 = models.IntegerField()
    alerta2 = models.IntegerField()
    alerta3 = models.IntegerField()
    class Meta:
        db_table = u'alerta_down_config'

class AlertaSmtp(models.Model):
    cd = models.IntegerField(primary_key=True)
    dsalerta = models.CharField(max_length=300, db_column='dsAlerta') # Field name made lowercase.
    email = models.CharField(max_length=600)
    class Meta:
        db_table = u'alerta_smtp'

class AnaliseDownHistorico(models.Model):
    cd = models.IntegerField(primary_key=True)
    tmpostagem = models.CharField(max_length=300, db_column='tmPostagem') # Field name made lowercase.
    hostsdesligados = models.TextField(db_column='hostsDesligados', blank=True) # Field name made lowercase.
    qttempo = models.CharField(max_length=300, db_column='qtTempo') # Field name made lowercase.
    class Meta:
        db_table = u'analise_down_historico'

class AnaliseUpHistorico(models.Model):
    cd = models.IntegerField(primary_key=True)
    tmpostagem = models.CharField(max_length=300, db_column='tmPostagem') # Field name made lowercase.
    hostsligados = models.CharField(max_length=300, db_column='hostsLigados') # Field name made lowercase.
    qttempo = models.CharField(max_length=300, db_column='qtTempo') # Field name made lowercase.
    class Meta:
        db_table = u'analise_up_historico'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(unique=True)
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type_id = models.IntegerField()
    codename = models.CharField(unique=True, max_length=300)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90, blank=True)
    first_name = models.CharField(max_length=90, blank=True)
    last_name = models.CharField(max_length=90, blank=True)
    email = models.CharField(max_length=225, blank=True)
    password = models.CharField(max_length=384, blank=True)
    is_staff = models.IntegerField(null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    is_superuser = models.IntegerField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    group_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_user_permissions'

class Dadosvarredurasespecificas(models.Model):
    cddados = models.IntegerField(primary_key=True, db_column='cdDados') # Field name made lowercase.
    cdoid = models.IntegerField(db_column='cdOid') # Field name made lowercase.
    vloid = models.IntegerField(db_column='vlOid') # Field name made lowercase.
    cdhostvarredura = models.IntegerField(db_column='cdHostVarredura') # Field name made lowercase.
    dstimestampcoleta = models.CharField(max_length=120, db_column='dsTimestampColeta') # Field name made lowercase.
    class Meta:
        db_table = u'dadosVarredurasEspecificas'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=300)
    model = models.CharField(unique=True, max_length=300)
    class Meta:
        db_table = u'django_content_type'

class DjangoFlatpage(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=300)
    title = models.CharField(max_length=600)
    content = models.TextField()
    enable_comments = models.IntegerField()
    template_name = models.CharField(max_length=210)
    registration_required = models.IntegerField()
    class Meta:
        db_table = u'django_flatpage'

class DjangoFlatpageSites(models.Model):
    id = models.IntegerField(primary_key=True)
    flatpage_id = models.IntegerField(unique=True)
    site_id = models.IntegerField()
    class Meta:
        db_table = u'django_flatpage_sites'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class DumpArp(models.Model):
    codigo = models.IntegerField(primary_key=True)
    protocolo = models.CharField(max_length=45, blank=True)
    tempo = models.CharField(max_length=45, blank=True)
    servico = models.CharField(max_length=45, blank=True)
    iporigem = models.CharField(max_length=45, db_column='ipOrigem', blank=True) # Field name made lowercase.
    ipdestino = models.CharField(max_length=45, db_column='ipDestino', blank=True) # Field name made lowercase.
    ipcoletor = models.CharField(max_length=135, db_column='ipColetor', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dump_arp'

class DumpIp(models.Model):
    codigo = models.IntegerField(primary_key=True)
    protocolo = models.CharField(max_length=90, blank=True)
    tempo = models.CharField(max_length=90, blank=True)
    iporigem = models.CharField(max_length=90, db_column='ipOrigem', blank=True) # Field name made lowercase.
    ipdestino = models.CharField(max_length=90, db_column='ipDestino', blank=True) # Field name made lowercase.
    complemento = models.CharField(max_length=90, blank=True)
    ipcoletor = models.CharField(max_length=135, db_column='ipColetor', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dump_ip'

class DumpIpv6(models.Model):
    codigo = models.IntegerField(primary_key=True)
    protocolo = models.CharField(max_length=45, blank=True)
    tempo = models.CharField(max_length=45, blank=True)
    macorigem = models.CharField(max_length=45, db_column='macOrigem', blank=True) # Field name made lowercase.
    macdestino = models.CharField(max_length=45, db_column='macDestino', blank=True) # Field name made lowercase.
    servico = models.CharField(max_length=45, blank=True)
    ipcoletor = models.CharField(max_length=180, db_column='ipColetor', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dump_ipv6'

class DumpStp(models.Model):
    codigo = models.IntegerField(primary_key=True)
    protocolo = models.CharField(max_length=45, blank=True)
    tempo = models.CharField(max_length=45, blank=True)
    servico = models.CharField(max_length=45, blank=True)
    mac = models.CharField(max_length=45, blank=True)
    ipcoletor = models.CharField(max_length=180, db_column='ipColetor', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dump_stp'

class Hospeda(models.Model):
    cdhost = models.ForeignKey(Hosts, null=True, db_column='cdHost', blank=True) # Field name made lowercase.
    cdservico = models.ForeignKey(Servicos, null=True, db_column='cdServico', blank=True) # Field name made lowercase.
    dsstatusalerta = models.CharField(max_length=90, db_column='dsStatusAlerta', blank=True) # Field name made lowercase.
    dsstatus = models.CharField(max_length=36, db_column='dsStatus', blank=True) # Field name made lowercase.
    cdhospeda = models.IntegerField(primary_key=True, db_column='cdHospeda') # Field name made lowercase.
    cdalerta = models.ForeignKey(Alerta, db_column='cdAlerta') # Field name made lowercase.
    class Meta:
        db_table = u'hospeda'

class Hostanalises(models.Model):
    cdanalise = models.IntegerField(primary_key=True, db_column='cdAnalise') # Field name made lowercase.
    status = models.IntegerField(null=True, blank=True)
    tmanalise = models.IntegerField(null=True, db_column='tmAnalise', blank=True) # Field name made lowercase.
    dados = models.TextField(blank=True)
    class Meta:
        db_table = u'hostAnalises'

class Hostcaminho(models.Model):
    id = models.IntegerField(primary_key=True)
    id_host = models.IntegerField()
    tmstamp = models.IntegerField(db_column='tmStamp') # Field name made lowercase.
    caminho = models.TextField()
    class Meta:
        db_table = u'hostCaminho'

class Hostlatencia(models.Model):
    id = models.IntegerField(primary_key=True)
    cdhost = models.IntegerField(db_column='cdHost') # Field name made lowercase.
    tmstamp = models.IntegerField(db_column='tmStamp') # Field name made lowercase.
    latencia = models.IntegerField()
    class Meta:
        db_table = u'hostLatencia'

class Hostmapa(models.Model):
    cdhostmapa = models.IntegerField(primary_key=True, db_column='cdHostMapa') # Field name made lowercase.
    cdmapa = models.ForeignKey(Mapa, null=True, db_column='cdMapa', blank=True) # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, null=True, db_column='cdHost', blank=True) # Field name made lowercase.
    dslinha = models.FloatField(null=True, db_column='dsLinha', blank=True) # Field name made lowercase.
    dscoluna = models.FloatField(null=True, db_column='dsColuna', blank=True) # Field name made lowercase.
    cdimagem = models.ForeignKey(Imagem, null=True, db_column='cdImagem', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hostMapa'

class Hostvarredura(models.Model):
    cdhostvarredura = models.IntegerField(primary_key=True, db_column='cdHostVarredura') # Field name made lowercase.
    cdvarredura = models.IntegerField(null=True, db_column='cdVarredura', blank=True) # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, null=True, db_column='cdHost', blank=True) # Field name made lowercase.
    dsstatus = models.CharField(max_length=120, db_column='dsStatus', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hostVarredura'

class Hosts(models.Model):
    cdhost = models.IntegerField(primary_key=True, db_column='cdHost') # Field name made lowercase.
    dsfqdn = models.CharField(max_length=300, db_column='dsFQDN', blank=True) # Field name made lowercase.
    cdrede = models.ForeignKey(Redes, null=True, db_column='cdRede', blank=True) # Field name made lowercase.
    cdtipohost = models.ForeignKey(Tipohost, null=True, db_column='cdTipoHost', blank=True) # Field name made lowercase.
    cdimagem = models.ForeignKey(Imagem, null=True, db_column='cdImagem', blank=True) # Field name made lowercase.
    cdhosthospedeiro = models.IntegerField(null=True, db_column='cdHostHospedeiro', blank=True) # Field name made lowercase.
    cdswvirtualizacao = models.ForeignKey(Swvirtualizacao, null=True, db_column='cdSwVirtualizacao', blank=True) # Field name made lowercase.
    cdsnmp = models.ForeignKey(Snmp, null=True, db_column='cdSnmp', blank=True) # Field name made lowercase.
    vlip = models.CharField(max_length=45, db_column='vlIP') # Field name made lowercase.
    statusmon = models.IntegerField(null=True, db_column='statusMon', blank=True) # Field name made lowercase.
    dslocalizacao = models.CharField(max_length=180, db_column='dsLocalizacao', blank=True) # Field name made lowercase.
    nmusuario = models.CharField(max_length=300, db_column='nmUsuario', blank=True) # Field name made lowercase.
    dstipohost = models.IntegerField(null=True, db_column='dsTipoHost', blank=True) # Field name made lowercase.
    tminicial = models.IntegerField(null=True, db_column='tmInicial', blank=True) # Field name made lowercase.
    tmatual = models.IntegerField(null=True, db_column='tmAtual', blank=True) # Field name made lowercase.
    tmanterior = models.IntegerField(null=True, db_column='tmAnterior', blank=True) # Field name made lowercase.
    dsstatus = models.IntegerField(null=True, db_column='dsStatus', blank=True) # Field name made lowercase.
    dsstatusanterior = models.IntegerField(null=True, db_column='dsStatusAnterior', blank=True) # Field name made lowercase.
    dsmudancastatus = models.IntegerField(null=True, db_column='dsMudancaStatus', blank=True) # Field name made lowercase.
    snmp = models.IntegerField(null=True, blank=True)
    snmpcomunidade = models.CharField(max_length=180, db_column='snmpComunidade', blank=True) # Field name made lowercase.
    mrtg = models.IntegerField(null=True, blank=True)
    globus = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'hosts'

class Hostshistorico(models.Model):
    cdhistorico = models.IntegerField(primary_key=True, db_column='cdHistorico') # Field name made lowercase.
    vlip = models.CharField(max_length=48, db_column='vlIp', blank=True) # Field name made lowercase.
    tmstamp = models.IntegerField(null=True, db_column='tmStamp', blank=True) # Field name made lowercase.
    dsstatus = models.IntegerField(null=True, db_column='dsStatus', blank=True) # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, null=True, db_column='cdHost', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hostsHistorico'

class Hostshistoricoanalise(models.Model):
    cdanalise = models.IntegerField(primary_key=True, db_column='cdAnalise') # Field name made lowercase.
    vlip = models.CharField(max_length=48, db_column='vlIP', blank=True) # Field name made lowercase.
    fqdn = models.CharField(max_length=120, blank=True)
    portas = models.CharField(max_length=900, blank=True)
    so = models.CharField(max_length=90, blank=True)
    versao = models.CharField(max_length=90, blank=True)
    mac = models.CharField(max_length=54, blank=True)
    uptime = models.CharField(max_length=30, blank=True)
    tipo = models.CharField(max_length=60, blank=True)
    distrede = models.IntegerField(null=True, db_column='distRede', blank=True) # Field name made lowercase.
    pathrede = models.CharField(max_length=600, db_column='pathRede', blank=True) # Field name made lowercase.
    serviceinfo = models.CharField(max_length=180, db_column='serviceInfo', blank=True) # Field name made lowercase.
    timestamp = models.IntegerField(null=True, db_column='timeStamp', blank=True) # Field name made lowercase.
    tempogasto = models.CharField(max_length=30, db_column='tempoGasto', blank=True) # Field name made lowercase.
    cdhost = models.IntegerField(null=True, db_column='cdHost', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hostsHistoricoAnalise'

class Imagem(models.Model):
    cdimagem = models.IntegerField(primary_key=True, db_column='cdImagem') # Field name made lowercase.
    tipohost = models.CharField(max_length=60, db_column='tipoHost', blank=True) # Field name made lowercase.
    dsarquivo = models.CharField(max_length=60, db_column='dsArquivo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'imagem'

class Instituicao(models.Model):
    cdinst = models.IntegerField(primary_key=True, db_column='cdInst') # Field name made lowercase.
    dsinst = models.CharField(max_length=900, db_column='dsInst', blank=True) # Field name made lowercase.
    tipo = models.CharField(max_length=90, blank=True)
    nome = models.CharField(max_length=90, blank=True)
    cdrede = models.IntegerField(null=True, db_column='cdRede', blank=True) # Field name made lowercase.
    cdtipoinst = models.ForeignKey(Tipoinst, null=True, db_column='cdTipoInst', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'instituicao'

class Iperfagendamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    horacoleta = models.DateTimeField(null=True, db_column='horaColeta', blank=True) # Field name made lowercase.
    hostcliente = models.CharField(max_length=240, db_column='hostCliente', blank=True) # Field name made lowercase.
    hostservido = models.CharField(max_length=240, db_column='hostServido', blank=True) # Field name made lowercase.
    protocolo = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'iperfAgendamento'

class Latencia(models.Model):
    cdlatencia = models.IntegerField(primary_key=True, db_column='cdLatencia') # Field name made lowercase.
    cdhost = models.IntegerField(null=True, db_column='cdHost', blank=True) # Field name made lowercase.
    statusmon = models.IntegerField(null=True, db_column='statusMon', blank=True) # Field name made lowercase.
    tminicial = models.CharField(max_length=405, db_column='tmInicial', blank=True) # Field name made lowercase.
    destino = models.TextField(blank=True)
    repeticao = models.IntegerField(null=True, blank=True)
    vezes = models.IntegerField(null=True, blank=True)
    protocolo = models.CharField(max_length=408, blank=True)
    class Meta:
        db_table = u'latencia'

class Latenciahistorico(models.Model):
    cdhistorico = models.IntegerField(primary_key=True, db_column='cdHistorico') # Field name made lowercase.
    cdhost = models.IntegerField(null=True, db_column='cdHost', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    vllatencia = models.CharField(max_length=30, db_column='vlLatencia', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'latenciaHistorico'

class Mapa(models.Model):
    cdmapa = models.IntegerField(primary_key=True, db_column='cdMapa') # Field name made lowercase.
    cdinst = models.ForeignKey(Instituicao, null=True, db_column='cdInst', blank=True) # Field name made lowercase.
    cdrede = models.ForeignKey(Redes, null=True, db_column='cdRede', blank=True) # Field name made lowercase.
    dsmapa = models.CharField(max_length=60, db_column='dsMapa', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'mapa'

class Redesumario(models.Model):
    id = models.IntegerField(primary_key=True)
    idrede = models.IntegerField(db_column='idRede') # Field name made lowercase.
    tmstamp = models.IntegerField(db_column='tmStamp') # Field name made lowercase.
    qthostsativos = models.IntegerField(db_column='qtHostsAtivos') # Field name made lowercase.
    qthostsinativos = models.IntegerField(db_column='qtHostsInativos') # Field name made lowercase.
    qthostsdesligados = models.IntegerField(db_column='qtHostsDesligados') # Field name made lowercase.
    qthostsligados = models.IntegerField(db_column='qtHostsLigados') # Field name made lowercase.
    qthostssemfqdn = models.IntegerField(db_column='qtHostsSemFqdn') # Field name made lowercase.
    class Meta:
        db_table = u'redeSumario'

class RedeInterna(models.Model):
    id = models.IntegerField(primary_key=True)
    armario = models.CharField(max_length=6)
    switch = models.CharField(max_length=45)
    porta = models.CharField(max_length=15, blank=True)
    vlan = models.CharField(max_length=45, blank=True)
    ponto = models.CharField(max_length=45, blank=True)
    sala = models.CharField(max_length=15, blank=True)
    velocidade = models.CharField(max_length=45, blank=True)
    mac = models.CharField(max_length=45, blank=True)
    ip = models.CharField(max_length=45, blank=True)
    nome = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'rede_interna'

class Redes(models.Model):
    cdrede = models.IntegerField(primary_key=True, db_column='cdRede') # Field name made lowercase.
    ip = models.CharField(max_length=48, blank=True)
    mascara = models.CharField(max_length=48, blank=True)
    cidr = models.CharField(max_length=6, blank=True)
    dsrede = models.CharField(max_length=180, db_column='dsRede', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, blank=True)
    cdinst = models.ForeignKey(Instituicao, null=True, db_column='cdInst', blank=True) # Field name made lowercase.
    tipo = models.CharField(max_length=60, blank=True)
    gateway = models.CharField(max_length=45, blank=True)
    dns = models.CharField(max_length=45, blank=True)
    wins = models.CharField(max_length=45, blank=True)
    cd = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'redes'

class Servicos(models.Model):
    cdservicos = models.IntegerField(primary_key=True, db_column='cdServicos') # Field name made lowercase.
    nmservico = models.CharField(max_length=45, db_column='nmServico', blank=True) # Field name made lowercase.
    dsservico = models.CharField(max_length=90, db_column='dsServico', blank=True) # Field name made lowercase.
    protocolotransporte = models.CharField(max_length=36, db_column='protocoloTransporte', blank=True) # Field name made lowercase.
    protocoloaplicacao = models.CharField(max_length=36, db_column='protocoloAplicacao', blank=True) # Field name made lowercase.
    portatransporte = models.IntegerField(null=True, db_column='portaTransporte', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'servicos'

class Snmp(models.Model):
    cdsnmp = models.IntegerField(primary_key=True, db_column='cdSnmp') # Field name made lowercase.
    dscomunidadero = models.IntegerField(null=True, db_column='dsComunidadeRo', blank=True) # Field name made lowercase.
    dscomunidaderw = models.IntegerField(null=True, db_column='dsComunidadeRw', blank=True) # Field name made lowercase.
    vlversao = models.CharField(max_length=6, db_column='vlVersao', blank=True) # Field name made lowercase.
    nmusr = models.IntegerField(null=True, db_column='nmUsr', blank=True) # Field name made lowercase.
    vlsenha = models.CharField(max_length=60, db_column='vlSenha', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmp'

class Snmpcpu(models.Model):
    cdsnmpcpu = models.IntegerField(primary_key=True, db_column='cdsnmpCpu') # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    cpuuser = models.IntegerField(null=True, db_column='cpuUser', blank=True) # Field name made lowercase.
    cpusystem = models.IntegerField(null=True, db_column='cpuSystem', blank=True) # Field name made lowercase.
    cpuidle = models.IntegerField(null=True, db_column='cpuIdle', blank=True) # Field name made lowercase.
    cpurawusr = models.IntegerField(null=True, db_column='cpuRawUsr', blank=True) # Field name made lowercase.
    cpurawnice = models.IntegerField(null=True, db_column='cpuRawNice', blank=True) # Field name made lowercase.
    cpurawsystem = models.IntegerField(null=True, db_column='cpuRawSystem', blank=True) # Field name made lowercase.
    cpurawidle = models.IntegerField(null=True, db_column='cpuRawIdle', blank=True) # Field name made lowercase.
    cpurawwait = models.IntegerField(null=True, db_column='cpuRawWait', blank=True) # Field name made lowercase.
    cpurawkernel = models.IntegerField(null=True, db_column='cpuRawKernel', blank=True) # Field name made lowercase.
    cpurawinterrupt = models.IntegerField(null=True, db_column='cpuRawInterrupt', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpCpu'

class Snmphd(models.Model):
    cdsnmphd = models.IntegerField(primary_key=True, db_column='cdSnmpHd') # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    hdindex = models.IntegerField(null=True, db_column='hdIndex', blank=True) # Field name made lowercase.
    hdpath = models.CharField(max_length=60, db_column='hdPath', blank=True) # Field name made lowercase.
    hddevice = models.CharField(max_length=60, db_column='hdDevice', blank=True) # Field name made lowercase.
    hdminimum = models.IntegerField(null=True, db_column='hdMinimum', blank=True) # Field name made lowercase.
    hdminpercent = models.CharField(max_length=9, db_column='hdMinPercent', blank=True) # Field name made lowercase.
    hdtotal = models.IntegerField(null=True, db_column='hdTotal', blank=True) # Field name made lowercase.
    hdavail = models.IntegerField(null=True, db_column='hdAvail', blank=True) # Field name made lowercase.
    hdused = models.IntegerField(null=True, db_column='hdUsed', blank=True) # Field name made lowercase.
    hdpercent = models.IntegerField(null=True, db_column='hdPercent', blank=True) # Field name made lowercase.
    hdpercentnode = models.IntegerField(null=True, db_column='hdPercentNode', blank=True) # Field name made lowercase.
    hderrorflag = models.CharField(max_length=60, db_column='hdErrorFlag', blank=True) # Field name made lowercase.
    hderrormsg = models.CharField(max_length=60, db_column='hdErrorMsg', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpHd'

class Snmpinterfaces(models.Model):
    cdsnmpinterfaces = models.IntegerField(primary_key=True, db_column='cdsnmpInterfaces') # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    snmpinterfacesindex = models.IntegerField(null=True, db_column='snmpInterfacesIndex', blank=True) # Field name made lowercase.
    snmpinterfacesdescricao = models.CharField(max_length=120, db_column='snmpInterfacesDescricao', blank=True) # Field name made lowercase.
    snmpinterfacesvelocidade = models.CharField(max_length=120, db_column='snmpInterfacesVelocidade', blank=True) # Field name made lowercase.
    snmpinterfacesmac = models.CharField(max_length=120, db_column='snmpInterfacesMac', blank=True) # Field name made lowercase.
    snmpinterfacesstatusadmin = models.CharField(max_length=120, db_column='snmpInterfacesStatusAdmin', blank=True) # Field name made lowercase.
    snmpinterfacesstatusoperacional = models.CharField(max_length=120, db_column='snmpInterfacesStatusOperacional', blank=True) # Field name made lowercase.
    tmcoleta = models.CharField(max_length=135, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpInterfaces'

class SnmpmrtgGlobal(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipohost = models.IntegerField(db_column='tipoHost') # Field name made lowercase.
    status = models.IntegerField()
    opcoes = models.TextField()
    variaveis = models.CharField(max_length=360, blank=True)
    class Meta:
        db_table = u'snmpMRTG-Global'

class SnmpmrtgOids(models.Model):
    codigo = models.IntegerField(primary_key=True)
    oid1 = models.CharField(max_length=90)
    oid2 = models.CharField(max_length=90, blank=True)
    titulo = models.CharField(max_length=180)
    opcoes = models.TextField()
    tipohost = models.IntegerField(db_column='tipoHost') # Field name made lowercase.
    variaveis = models.CharField(max_length=360, blank=True)
    status = models.IntegerField()
    class Meta:
        db_table = u'snmpMRTG-OIDS'

class Snmpmacip(models.Model):
    cdsnmpmacip = models.IntegerField(primary_key=True, db_column='cdSnmpMacIp') # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    ipmacindex = models.IntegerField(null=True, db_column='ipMacIndex', blank=True) # Field name made lowercase.
    ipmacenderecofisico = models.CharField(max_length=120, db_column='ipMacEnderecoFisico', blank=True) # Field name made lowercase.
    ipmacip = models.CharField(max_length=120, db_column='ipMacIp', blank=True) # Field name made lowercase.
    ipmactipo = models.CharField(max_length=90, db_column='ipMacTipo', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpMacIp'

class Snmpmemoria(models.Model):
    cdsnmpmemoria = models.IntegerField(primary_key=True, db_column='cdSnmpMemoria') # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    memindex = models.IntegerField(null=True, db_column='memIndex', blank=True) # Field name made lowercase.
    memerrorname = models.CharField(max_length=60, db_column='memErrorName', blank=True) # Field name made lowercase.
    memtotalswap = models.IntegerField(null=True, db_column='memTotalSwap', blank=True) # Field name made lowercase.
    memavailswap = models.IntegerField(null=True, db_column='memAvailSwap', blank=True) # Field name made lowercase.
    memtotalreal = models.IntegerField(null=True, db_column='memTotalReal', blank=True) # Field name made lowercase.
    memavailreal = models.IntegerField(null=True, db_column='memAvailReal', blank=True) # Field name made lowercase.
    memtotalfree = models.IntegerField(null=True, db_column='memTotalFree', blank=True) # Field name made lowercase.
    memminswap = models.IntegerField(null=True, db_column='memMinSwap', blank=True) # Field name made lowercase.
    memshared = models.IntegerField(null=True, db_column='memShared', blank=True) # Field name made lowercase.
    membuffer = models.IntegerField(null=True, db_column='memBuffer', blank=True) # Field name made lowercase.
    memcached = models.IntegerField(null=True, db_column='memCached', blank=True) # Field name made lowercase.
    memswaperror = models.CharField(max_length=45, db_column='memSwapError', blank=True) # Field name made lowercase.
    memswaperrormsg = models.CharField(max_length=60, db_column='memSwapErrorMsg', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpMemoria'

class Snmpprocesso(models.Model):
    cdsnmpprocesso = models.IntegerField(primary_key=True, db_column='cdSnmpProcesso') # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    cpuusage = models.IntegerField(null=True, db_column='cpuUsage', blank=True) # Field name made lowercase.
    processoindex = models.IntegerField(null=True, db_column='processoIndex', blank=True) # Field name made lowercase.
    processonome = models.CharField(max_length=105, db_column='processoNome', blank=True) # Field name made lowercase.
    processomin = models.IntegerField(null=True, db_column='processoMin', blank=True) # Field name made lowercase.
    processomax = models.IntegerField(null=True, db_column='processoMax', blank=True) # Field name made lowercase.
    processocount = models.IntegerField(null=True, db_column='processoCount', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpProcesso'

class Snmpsys(models.Model):
    cdsnmpsys = models.IntegerField(primary_key=True, db_column='cdSnmpSys') # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    sysdescr = models.CharField(max_length=300, db_column='sysDescr', blank=True) # Field name made lowercase.
    sysname = models.CharField(max_length=300, db_column='sysName', blank=True) # Field name made lowercase.
    syscontact = models.CharField(max_length=150, db_column='sysContact', blank=True) # Field name made lowercase.
    syslastchange = models.CharField(max_length=150, db_column='sysLastChange', blank=True) # Field name made lowercase.
    syslocation = models.CharField(max_length=150, db_column='sysLocation', blank=True) # Field name made lowercase.
    sysuptime = models.CharField(max_length=150, db_column='sysUpTime', blank=True) # Field name made lowercase.
    enderecofisico = models.CharField(max_length=150, db_column='enderecoFisico', blank=True) # Field name made lowercase.
    inoctets = models.CharField(max_length=150, db_column='inOctets', blank=True) # Field name made lowercase.
    outoctets = models.CharField(max_length=150, db_column='outOctets', blank=True) # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpSys'

class Snmptemperatura(models.Model):
    cdsnmptemperatura = models.IntegerField(primary_key=True, db_column='cdSnmpTemperatura') # Field name made lowercase.
    tempindex = models.CharField(max_length=15, db_column='tempIndex', blank=True) # Field name made lowercase.
    tempdevice = models.CharField(max_length=150, db_column='tempDevice', blank=True) # Field name made lowercase.
    tempvalor = models.CharField(max_length=30, db_column='tempValor', blank=True) # Field name made lowercase.
    cdhost = models.ForeignKey(Hosts, db_column='cdHost') # Field name made lowercase.
    tmcoleta = models.IntegerField(null=True, db_column='tmColeta', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'snmpTemperatura'

class Swvirtualizacao(models.Model):
    cdswvirtualizacao = models.IntegerField(primary_key=True, db_column='cdSwVirtualizacao') # Field name made lowercase.
    dsswvirtualizado = models.CharField(max_length=120, db_column='dsSwVirtualizado', blank=True) # Field name made lowercase.
    dstipo = models.IntegerField(null=True, db_column='dsTipo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'swVirtualizacao'

class Telefones(models.Model):
    id = models.IntegerField(primary_key=True)
    bloco = models.CharField(max_length=60, blank=True)
    fila = models.IntegerField(null=True, blank=True)
    ponto = models.IntegerField(null=True, blank=True)
    ramal = models.CharField(max_length=60, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    cdusr = models.ForeignKey(Usr, null=True, db_column='cdUsr', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'telefones'

class Tipohost(models.Model):
    cdtipohost = models.IntegerField(primary_key=True, db_column='cdTipoHost') # Field name made lowercase.
    dstipohost = models.CharField(max_length=60, db_column='dsTipoHost', blank=True) # Field name made lowercase.
    dsativo = models.IntegerField(null=True, db_column='dsAtivo', blank=True) # Field name made lowercase.
    dsnivelativo = models.IntegerField(null=True, db_column='dsNivelAtivo', blank=True) # Field name made lowercase.
    cdimagem = models.ForeignKey(Imagem, null=True, db_column='cdImagem', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tipoHost'

class Tipoinst(models.Model):
    cdtipoinst = models.IntegerField(primary_key=True, db_column='cdTipoInst') # Field name made lowercase.
    dstipoinst = models.CharField(max_length=150, db_column='dsTipoInst', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tipoInst'

class Tipousr(models.Model):
    cdtipousr = models.IntegerField(primary_key=True, db_column='cdTipoUsr') # Field name made lowercase.
    dstipo = models.CharField(max_length=60, db_column='dsTipo', blank=True) # Field name made lowercase.
    dscomentario = models.CharField(max_length=150, db_column='dsComentario', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tipoUsr'

class Usr(models.Model):

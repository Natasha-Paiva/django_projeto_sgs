# -*- coding: utf-8 -*-

from django.db import models

class Hosts(models.Model):
    class Meta:
	ordering = ['dsfqdn']
    db_table = u'hosts'

    cdhost = models.AutoField(primary_key = True,
                              db_column = 'cdHost')

    statusmon = models.IntegerField(null = True,
                                   db_column = 'statusMon',
                                   blank = True)

    dstipohost = models.IntegerField(null = True,
                                     db_column = 'dsTipoHost',
                                     blank = True)

    tminicial = models.IntegerField(null = True,
                                    db_column = 'tmInicial',
                                    blank = True)

    tmatual = models.IntegerField(null = True,
                                  db_column = 'tmAtual',
                                  blank = True)

    tmanterior = models.IntegerField(null = True,
                                     db_column = 'tmAnterior',
                                     blank = True)

    dsstatus = models.IntegerField(null = True,
                                   db_column = 'dsStatus',
                                   blank = True)

    dsstatusanterior = models.IntegerField(null = True,
                                           db_column = 'dsStatusAnterior',
                                           blank = True)

    vlip = models.CharField(max_length = 45,
                              db_column = 'vlIP',
                              blank = True)

    dsfqdn = models.CharField(max_length = 300,
                              db_column = 'dsFQDN',
                              blank = True)

    dslocalizacao = models.CharField(max_length = 180,
                                     db_column = 'dsLocalizacao',
                                     blank = True)

    snmpcomunidade = models.CharField(max_length = 180,
                                      db_column = 'snmpComunidade',
                                      blank = True)

    snmp = models.IntegerField(null = True,
                               db_column = 'snmp',
                               blank = True)
    tempo = models.CharField(max_length = 200, db_column = 'tempo', blank=True)
    minutos = models.CharField(max_length=200, db_column='minutos', blank=True)
    cdrede = models.IntegerField(db_column = 'cdRede')
    cdtipohost = models.IntegerField(db_column = 'cdTipoHost')
    dsmudancastatus = models.IntegerField(db_column = 'dsMudancaStatus')

    def __unicode__(self):
      return self.dsfqdn

class Redes(models.Model):
    class Meta:
        db_table = u'redes'

    dsrede = models.CharField(max_length = 180,
                               db_column ='dsRede', blank = True)
    cdrede = models.IntegerField(primary_key = True,
                                  db_column='cdRede')


class Usr(models.Model):
    class Meta:
        db_table = u'usr'

    cdusr = models.IntegerField(primary_key=True,
                                db_column='cdUsr')

    dslogin = models.CharField(max_length=180,
                               db_column='dsLogin',
                               blank=True)

    dssenha = models.CharField(max_length=180,
                               db_column='dsSenha',
                               blank=True)

    dsstatus = models.CharField(max_length=120,
                                db_column='dsStatus',
                                blank=True)

    nmusuario = models.CharField(max_length=150,
                                 db_column='nmUsuario',
                                 blank=True)

    dscomentario = models.CharField(max_length=120,
                                    db_column='dsComentario',
                                    blank=True)

    cdtipousr = models.IntegerField(null=True,
                                    db_column='cdTipoUsr',
                                    blank=True)

    cdinst = models.IntegerField(null=True,
                                 db_column='cdInst',
                                 blank=True)

    cdrede = models.ForeignKey(Redes, null=True,
                                      db_column='cdRede',
                                      blank=True)
    dtcriacao = models.CharField(max_length=60,
                                 db_column='dtCriacao',
                                 blank=True)

    dtexpirar = models.CharField(max_length=60,
                                 db_column='dtExpirar',
                                 blank=True)

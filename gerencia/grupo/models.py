# -*- coding: utf-8 -*-

from django.db import models

class Grupo(models.Model):
    class Meta:
        db_table = u'grupo'
    id = models.AutoField(primary_key=True)
    ds_grupo = models.CharField(max_length=600,
                                blank=True,
                                verbose_name="Nome")

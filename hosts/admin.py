# -*- coding: utf-8 -*-
from django.contrib import admin

from hosts.models import Hosts

class HostsAdmin(admin.ModelAdmin):
#    list_display = ('dsfqdn', 'vlip', 'dsstatus', 'dsrede')
#    list_filter  = ['dsfqdn', 'vlip', 'dsstatus', 'dsrede']

  list_display = ('dsfqdn', 'vlip', 'dsstatus')
  list_filter = ['dsfqdn', 'vlip', 'dsstatus']

admin.site.register(Hosts, HostsAdmin)


#!/usr/bin/python
import sys
import os

sys.path.insert(0, '/var/django/projects/projeto_sgs/')
sys.path.insert(0, '/var/django/pluggables/')


os.chdir('/var/django/projects/projeto_sgs/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method='threaded', daemonize='false')

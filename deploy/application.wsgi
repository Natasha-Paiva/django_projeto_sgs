#!/usr/bin/python

import os
import sys
import site

from os.path import abspath, join, dirname

project_name = "projeto_sgs"
root_dir = abspath(join(dirname(__file__), '..'))
python_version = sys.version_info[:2]

site_dir = 'lib/python%s.%s/site-packages' % python_version
site.addsitedir(join(root_dir, site_dir))
sys.path.append(root_dir)
sys.path.append(join(root_dir, project_name))

os.environ['DJANGO_SETTINGS_MODULE'] = projeto_sgs.settings
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


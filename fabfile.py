# -*- coding: utf-8 -*- #
from __future__ import absolute_import, print_function, unicode_literals

import sys
import os
import tempfile

from fabric.api import env, execute, cd, run, local, puts, warn, abort, task, settings, prefix, sudo, roles
from fabric.contrib import django, console

django.settings_module('woyd.settings.dev')
from woyd.settings.dev import *

env.forward_agent = True
env.code_dir = '/home/webuser/src/fuzzic'
env.shell = "/bin/bash -l -i -c"
env.roledefs = {
    'dev': ['webuser@92.222.83.137'],
}

OS = sys.platform
DB = DATABASES['default']
DB['CONN'] = 'postgresql://%s@%s:%s' % (DB['USER'],
                                        DB['HOST'],
                                        DB['PORT'])
TEMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
DB_DUMP_FILE = os.path.join(TEMP_DIR, '%s.%s.dump' % (DB['HOST'], DB['NAME']))
MEDIA_DUMP_FILE = os.path.join(TEMP_DIR, 'media.tar.gz')

def make_temp_dir():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

# Local tasks

@task
def clean():
    ''' Remove all cache files in the project
    '''
    if OS == 'darwin':
        local('gfind -iname "*.pyc" -delete')
    else:
        local('find -iname "*.pyc" -delete')
    local('rm -rf .sass-cache')


@task
def po():
    ''' Update translations files
    '''
    local('python manage.py makemessages -l en -l it --ignore="styles/*" --ignore="www/static/*" --ignore "node_modules/*" ')


@task
def mo():
    ''' Compile translations files
    '''
    local('python manage.py compilemessages')


@task
def test():
    ''' Run tests
    '''
    execute('clean')
    local('bash runtests.sh')


@task
def dev():
    ''' Run a local python web server and gulp
    '''
    execute('clean')
    local('python manage.py runserver 0.0.0.0:9091')


@task
def manage(cmd):
    ''' Run a manage.py command
    '''
    execute('clean')
    local('python manage.py %s' % cmd)


@task
def update():
    ''' Update requirements
    '''
    execute('clean')
    local('pip install --exists-action=w -r requirements.txt')
    local('npm install')


def overwrite(f):
    if os.path.isfile(f):
        if not console.confirm('There is already a media dump. Overwrite?', default=False):
            return False
    return True


@task
def mediadump():
    ''' Dump the media files
    '''
    if overwrite(MEDIA_DUMP_FILE):
        make_temp_dir()
        local('tar -zcvf %s media' % MEDIA_DUMP_FILE)
        print('\nThe media dump is %s' % MEDIA_DUMP_FILE)


# Database tasks

@task
def dbdump():
    ''' Dump the database
    '''
    if overwrite(DB_DUMP_FILE):
        make_temp_dir()
        local('pg_dump %s/%s -Ox -F c -f %s' % (DB['CONN'], DB['NAME'], DB_DUMP_FILE))
        print('\nThe database dump is %s' % DB_DUMP_FILE)


@task
def dbrestore(df=None):
    ''' Restore the dumped database
    '''
    execute(dbreset)
    if df == None:
        df = DB_DUMP_FILE
    local('pg_restore -d "%s/%s" -Ocxe --if-exists %s' % (DB['CONN'], DB['NAME'], df))


@task
def dbreset(migrate=False):
    ''' Delete and create a new empty database
    '''
    local('psql %s/postgres -c "DROP DATABASE IF EXISTS %s;"' % (DB['CONN'], DB['NAME']))
    local('psql %s/postgres -c "CREATE DATABASE %s;"' % (DB['CONN'], DB['NAME']))
    if migrate:
        execute('migrate')


@task
def migrate():
    ''' Run migrations
    '''
    local('python manage.py makemigrations')
    local('python manage.py migrate')

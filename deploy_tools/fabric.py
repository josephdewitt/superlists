from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'http://github.com/josephdewitt/superlists.git'

def deploy():
	site_folder = '/home/%s/sites/%s' % (env.user, env.host)
	source_folder = site_folder + '/source'
	_create_directory_structure_if_necessary(site_folder)
	_get_latest_source(source_folder)
	_update_settings(source_folder, env.host)
	_update_virtualenv(source_folder)

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'http://github.com/josephdewitt/superlists.git'

def deploy():
	site_folder = '/home/%s/sites/%s' % (env.user, env.host)
	source_folder = site_folder + 'sourse'
	_create_directory_structure_if_necessary(site_folder)
	
	

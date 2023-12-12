# Configuration file for jupyterhub.
import os

c = get_config()  #noqa

###c.JupyterHub.admin_users = {'root'} 


from oauthenticator.generic import GenericOAuthenticator

c.JupyterHub.authenticator_class = GenericOAuthenticator

c.GenericOAuthenticator.client_id = '1e8cef9933695c137acd'
c.GenericOAuthenticator.client_secret = 'e9c42a5f4be46bedf8eb0060828fe31cf9891ac4'
c.GenericOAuthenticator.oauth_callback_url = 'http://10.100.0.239:8888/hub/oauth_callback'
c.GenericOAuthenticator.token_url = 'http://10.100.0.239:8900/api/login/oauth/access_token'
c.GenericOAuthenticator.authorize_url = 'http://10.100.0.239:8900/login/oauth/authorize'
c.GenericOAuthenticator.userdata_url = 'http://10.100.0.239:8900/api/get-account'
c.GenericOAuthenticator.userdata_method = 'GET'
c.GenericOAuthenticator.userdata_params = {"state": "state"}
c.GenericOAuthenticator.username_claim = 'name'

#c.GenericOAuthenticator.auto_login = True
#c.GenericOAuthenticator.auth_refresh_age = 21600
#c.GenericOAuthenticator.refresh_pre_spawn = True
c.GenericOAuthenticator.tls_verify = False
c.GenericOAuthenticator.enable_auth_state = True

c.OAuthenticator.allow_all = True
#c.Authenticator.allowed_users = {'sunny5156'}


#c.ConfigurableHTTPProxy.should_start = True
#c.ConfigurableHTTPProxy.api_url = 'http://10.100.0.239:8000'

#c.JupyterHub.base_url = '/'
c.JupyterHub.hub_ip = '10.100.0.239'
##c.JupyterHub.port = 8000
##c.JupyterHub.hub_port = 8080
#c.JupyterHub.bind_url = 'http://:8888'
c.JupyterHub.bind_url = 'http://10.100.0.239:8888'
##c.JupyterHub.hub_connect_ip = '10.100.0.239'
#c.JupyterHub.default_url = '/hub/home'

#c.Spawner.default_url = '/'
#c.Spawner.notebook_dir = '/'
c.Spawner.default_url = '/lab'
c.JupyterHub.redirect_to_server = False
c.JupyterHub.debug_proxy = False

#c.JupyterHub.proxy_api_ip = '10.100.0.239'
#c.JupyterHub.proxy_api_port = 5432

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'cuda-rockylinux-nb:0.3.4'
c.DockerSpawner.network_name = 'bridge'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.extra_host_config = {'network_mode': 'bridge'}
#c.DockerSpawner.container_ip = '172.17.0.7'
c.JupyterHub.internal_ssl = False

c.DockerSpawner.cmd = "bash /run.sh && jupyter-labhub"

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
# c.Spawner.notebook_dir = '~' 
#username = spawner.user.name
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/{username}'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { '/L/jupyter/jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.extra_create_kwargs = {
    #"user": "root" # Can also be an integer UID
}

c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}
c.DockerSpawner.hub_connect_url = 'http://10.100.0.239:8081'
c.DockerSpawner.debug = False

c.JupyterHub.tornado_settings = {'slow_spawn_timeout': 50}

# Other stuff
c.Spawner.cpu_limit = 10
c.Spawner.mem_limit = '10G'

c.Spawner.http_timeout = 60
c.Spawner.start_timeout = 60
c.Spawner.args = ["--allow-root"]
## Services
# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]

###c.LocalAuthenticator.create_system_users = False  
###c.LocalAuthenticator.add_user_cmd = ['adduser'] 
###c.DummyAuthenticator.password = 123654
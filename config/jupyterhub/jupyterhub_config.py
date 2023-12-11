# Configuration file for jupyterhub.
import os

c = get_config()  #noqa

###c.JupyterHub.admin_users = {'root'} 

from oauthenticator.generic import GenericOAuthenticator

c.JupyterHub.authenticator_class = GenericOAuthenticator

c.GenericOAuthenticator.client_id = '1e8cef9933695c137acd'
c.GenericOAuthenticator.client_secret = 'e9c42a5f4be46bedf8eb0060828fe31cf9891ac4'
#c.GenericOAuthenticator.oauth_callback_url = 'http://10.100.0.239:8000/callback'
#c.GenericOAuthenticator.oauth_callback_url = 'http://172.17.0.12:8081/hub/oauth_callback'
c.GenericOAuthenticator.oauth_callback_url = 'http://10.100.0.239:8080/hub/oauth_callback'
c.GenericOAuthenticator.token_url = 'http://10.100.0.239:8000/api/login/oauth/access_token'
c.GenericOAuthenticator.authorize_url = 'http://10.100.0.239:8000/login/oauth/authorize'
#c.GenericOAuthenticator.userdata_url = 'http://10.100.0.239:8000/api/userinfo'
c.GenericOAuthenticator.userdata_url = 'http://10.100.0.239:8000/api/get-account'
c.GenericOAuthenticator.userdata_method = 'GET'
c.GenericOAuthenticator.userdata_params = {"state": "state"}
#c.GenericOAuthenticator.username_key = 'name'
c.GenericOAuthenticator.username_claim = 'name'

#c.GenericOAuthenticator.auto_login = True
#c.GenericOAuthenticator.auth_refresh_age = 21600
#c.GenericOAuthenticator.refresh_pre_spawn = True
c.GenericOAuthenticator.tls_verify = False
c.GenericOAuthenticator.enable_auth_state = True

c.OAuthenticator.allow_all = True
#c.Authenticator.allowed_users = {'sunny5156'}


#c.JupyterHub.base_url = '/'
c.JupyterHub.port = 8008
c.JupyterHub.hub_port = 8080
c.JupyterHub.bind_url = 'http://:8888'
c.JupyterHub.hub_connect_ip = '10.100.0.239'

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.JupyterHub.spawner_class = 'docker'
#c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.image = 'cuda-rocklinux-nb:0.3.2'
c.DockerSpawner.network_name = 'bridge'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.extra_host_config = {'network_mode': 'bridge'}

#c.DockerSpawner.cmd = "jupyter lab --notebook-dir=~ --no-browser --allow-root"
c.JupyterHub.hub_ip = '10.100.0.239'

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
# c.Spawner.notebook_dir = '~' 
#username = spawner.user.name
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/{username}'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { '/L/jupyter/jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.extra_create_kwargs = {
    #"user": "root" # Can also be an integer UID
    #"interactive": True,
    #"detach": True,
    #"tty": True,
    #"restart": "unless-stopped",
    #"network": "jupyter_bridge",
}

c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}

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

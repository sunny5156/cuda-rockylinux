# Configuration file for jupyterhub.

c = get_config()  #noqa

c.JupyterHub.admin_users = {'root'} 
c.JupyterHub.base_url = '/' 
c.JupyterHub.bind_url = 'http://:8888' 
c.JupyterHub.port = 80 
c.Spawner.notebook_dir = '~' 

c.LocalAuthenticator.create_system_users = True 
c.LocalAuthenticator.add_user_cmd = "adduser"
c.DummyAuthenticator.password = "123654"
#!/bin/bash

# source /etc/profile

# source /root/.bashrc

# IS_EXSIT=$(conda list |grep nb_conda | wc -l)

if [ ! -f /root/.jupyter/jupyter_lab_config.py ];then

    # 指定版本
    /opt/anaconda3/bin/pip install jupyterlab==3.6.5  -i https://pypi.mirrors.ustc.edu.cn/simple/

    /opt/anaconda3/bin/pip install -U "nbclassic>=0.2.8"  -i https://pypi.mirrors.ustc.edu.cn/simple/

    #安装 jupyter
    /opt/anaconda3/bin/conda install -y  nb_conda 

    /opt/anaconda3/bin/jupyter lab --generate-config 

    # 配置文件 /root/.jupyter/jupyter_lab_config.py

    sed -i "s|# c.ServerApp.allow_remote_access.*|c.ServerApp.allow_remote_access = True |g" /root/.jupyter/jupyter_lab_config.py

    # c.ServerApp.notebook_dir = '/data/aiworkspaces/'

    sed -i "s|# c.ServerApp.notebook_dir.*|c.ServerApp.notebook_dir = '~' |g" /root/.jupyter/jupyter_lab_config.py

    # c.ServerApp.local_hostnames = ['10.100.1.241']

    sed -i "s|# c.ServerApp.local_hostnames.*|c.ServerApp.local_hostnames = ['0.0.0.0'] |g" /root/.jupyter/jupyter_lab_config.py

    # c.ServerApp.ip = 'localhost'
    sed -i "s|# c.ServerApp.ip.*|c.ServerApp.ip = '0.0.0.0' |g" /root/.jupyter/jupyter_lab_config.py


    # jupyter lab password  (defaults password : 123456)
    sed -i "s|# c.ServerApp.password.*|c.ServerApp.password = 'argon2:\$argon2id\$v=19\$m=10240,t=10,p=8\$CGsPYX1oTYf/IrlvhewD2w\$FhbSymh1XS5d5UQCLf1hpXBCkAIKiYIwtsu9PM7oTfY'|g" /root/.jupyter/jupyter_lab_config.py

    # # c.ServerApp.allow_root = False
    sed -i "s|# c.ServerApp.allow_root.*|c.ServerApp.allow_root = True |g" /root/.jupyter/jupyter_lab_config.py


    # install plugins
    /opt/anaconda3/bin/pip install jupyterthemes -i https://pypi.mirrors.ustc.edu.cn/simple/
    # pip install jupyterlab-lsp -i https://pypi.mirrors.ustc.edu.cn/simple/


    # pip install jupyter_contrib_nbextensions  -i https://pypi.mirrors.ustc.edu.cn/simple/


    # finshed
    echo "Jupyter Lab  Setup Finished"

    # jupyterhub
    /opt/anaconda3/bin/pip install jupyterhub==4.0.1 -i https://pypi.mirrors.ustc.edu.cn/simple/

    mkdir -p /opt/jupyterhub/ 

    cd /opt/jupyterhub/ 

    /opt/anaconda3/bin/jupyterhub --generate-config 

    cd /

    #
    sed -i "s|# c.JupyterHub.port.*|c.JupyterHub.port = 80 |g" /opt/jupyterhub/jupyterhub_config.py

    sed -i "s|# c.JupyterHub.base_url.*|c.JupyterHub.base_url = '/' |g" /opt/jupyterhub/jupyterhub_config.py

    sed -i "s|# c.JupyterHub.bind_url.*|c.JupyterHub.bind_url = 'http://:8888' |g" /opt/jupyterhub/jupyterhub_config.py

    # c.Spawner.notebook_dir = '/data/'

    # LocalAuthenticator.create_system_users=True

    sed -i "s|# c.Spawner.notebook_dir.*|c.Spawner.notebook_dir = '~' |g" /opt/jupyterhub/jupyterhub_config.py

    sed -i "s|# c.JupyterHub.admin_users.*|c.JupyterHub.admin_users = {'root'} |g" /opt/jupyterhub/jupyterhub_config.py

    echo -e "\n\
c.LocalAuthenticator.create_system_users = True  \n\
c.LocalAuthenticator.add_user_cmd = "adduser" \n\
c.DummyAuthenticator.password = "123654" \n\
    " >>　/opt/jupyterhub/jupyterhub_config.py

    # c.Authenticator.whitelist = {'root','super','jupyter'}

    # c.JupyterHub.admin_users = {'root','super'}

    # c.Spawner.cmd = ['jupyterhub-singleuser']

    # finshed
    echo "Jupyter Hub  Setup Finished"
fi




 

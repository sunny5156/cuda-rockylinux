# FROM nvidia/cuda:12.0.0-cudnn8-runtime-rockylinux8  AS builder 
FROM nvidia/cuda:12.0.0-cudnn8-devel-rockylinux8  AS builder 
# FROM nvidia/cuda:11.2.0-cudnn8-devel-rockylinux8  AS builder

# FROM centos:centos7
MAINTAINER sunny5156 <sunny5156@qq.com>

# COPY ./Anaconda3-2023.09-0-Linux-x86_64.sh /root/Anaconda3-2023.09-0-Linux-x86_64.sh
COPY ./Miniconda3-latest-Linux-x86_64.sh /root/Miniconda3-latest-Linux-x86_64.sh
#COPY ./anaconda3-bak.zip /opt/anaconda3-bak.zip


COPY ./run.sh /run.sh
# COPY ./auto-install-anaconda.sh /auto-install-anaconda.sh

#RUN echo | /root/Anaconda3-2021.05-Linux-x86.sh 

# RUN yum install -y anaconda 

RUN yum install -y sudo vim git zip unzip lrzsz iproute openssh-server openssh-clients procps epel-release 


# RUN cd /opt \
#     && unzip anaconda3-bak.zip

RUN sh /root/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3/  \
    && rm -rf /root/Miniconda3-latest-Linux-x86_64.sh

# -----------------------------------------------------------------------------
# Configure, timezone/sshd/passwd/networking , Config root , add super
# -----------------------------------------------------------------------------
# WARNING: 'UsePAM no' is not supported in Red Hat Enterprise Linux and may cause several problems.
RUN ln -sf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime \
    && echo "root:123456" | chpasswd \
    && ssh-keygen -q -t rsa -b 4096 -f /etc/ssh/ssh_host_rsa_key -N '' \ 
    && ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \
    && ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N '' \
    && sed -i "s/GSSAPIAuthentication yes/GSSAPIAuthentication no/g" /etc/ssh/ssh_config \
    && useradd super \
    && echo "super:123456" | chpasswd \
    && echo "super  ALL=(ALL)  NOPASSWD: ALL" >> /etc/sudoers 


COPY ./config/profile /etc/profile

COPY ./config/.bashrc /root/.bashrc
COPY ./config/.bashrc /home/super/.bashrc

COPY ./jupyterlab-install.sh /opt/jupyterlab-install.sh

COPY ./config/supervisor /etc/supervisor


RUN echo "/usr/sbin/sshd" >> /etc/rc.local \
    && chmod +x /etc/rc.local /run.sh \
    && rm -rf /run/nologin

RUN curl -s --location https://rpm.nodesource.com/setup_16.x | bash - \
    && yum install -y nodejs htop \
    && npm --registry https://registry.npm.taobao.org install -g configurable-http-proxy \
    && sh /opt/jupyterlab-install.sh

COPY ./config/jupyterhub/jupyterhub_config.py /opt/jupyterhub/jupyterhub_config.py
COPY ./config/jupyterhub/jupyterhub_cookie_secret /root/jupyterhub_cookie_secret
# -----------------------------------------------------------------------------
# Install Python PIP & Supervisor distribute
# -----------------------------------------------------------------------------
RUN cd ${SRC_DIR} \
    # && pip install --upgrade pip \
    && /opt/miniconda3/bin/pip install supervisor==4.2.2 


# 压缩合并
FROM nvidia/cuda:12.0.0-cudnn8-devel-rockylinux8

COPY --from=builder / / 

CMD ["/run.sh"]
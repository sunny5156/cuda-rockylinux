# cuda-rockylinux

cuda-rockylinux

base nvidia/cuda:11.2.0-cudnn8-devel-rockylinux8  

jupyterlab: 3.6.5

jupyterhub: 4.0.1

supervisor: 4.2.2



准备工作

基础镜像拉取(可以根据自己情况选择)

```bash
# 镜像大,有点慢
docker pull nvidia/cuda:12.0.0-cudnn8-devel-rockylinux8

```



编译自己的镜像

```bash
# 先编译 cuda-rockylinux:0.3.2
docker build -t cuda-rockylinux:0.3.2 -f Dockerfile ./

# 在编译 cuda-rockylinux-nb:0.3.4
docker build -t cuda-rockylinux-nb:0.3.4 -f Dockerfile.jupyterlab ./

```



Jupyterhub(宿主机) + Jupyterlab(Docker)



```bash

yum install python3.11 python3.11-pip -y

ln -s python3.11 python

ln -s pip3.11 pip

pip install jupyterhub==4.0.1  dockerspawner oauthenticator  -i https://pypi.mirrors.ustc.edu.cn/simple/
```






```bash



docker build -t cuda-rockylinux8:0.0.1 ./

docker run -itd --gpus all --name cuda-test-8 --hostname cuda-test-8 -v /data/:/data/ cuda-rockylinux8:0.0.1

```


```bash

conda create -n mypy python=3.10 nb_conda_kernels -y

```

```bash

docker build -t cuda-rockylinux8:0.3.2 ./

docker run -itd --privileged --restart=unless-stopped --name cuda-env-2 --hostname cuda-env-2  --mount "type=bind,source=/var/run/docker.sock,destination=/var/run/docker.sock" cuda-rocklinux:0.3.2

```





Jupyterhub(Docker) + Jupyterlab(Docker)
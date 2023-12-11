# cuda-rockylinux

cuda-rockylinux

base nvidia/cuda:11.2.0-cudnn8-devel-rockylinux8  

jupyterlab: 3.6.5
jupyterhub: 4.0.1
supervisor: 4.2.2


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
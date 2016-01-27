django-docker-ubunutu
=======================
This project records details about how to run a django server with ubuntu in docker.
You can download the docker image from [here](https://hub.docker.com/u/xpxu/) with `docker pull xpxu/ubuntu_django`

1. start up docker image with network setup
-----------
X.X.X.X is the host ip. convert 80 of host ip to docker 8080

    docker run -i -t  -p X.X.X.X:80:8080 ubuntu_django


2. proxy setup
--------------
    export HTTP_PROXY=http://www-proxy.XX.com:80
    export HTTPS_PROXY=http://www-proxy.XX.com:80
    export http_proxy=http://www-proxy.XX.com:80
    export https_proxy=http://www-proxy.XX.com:80

3. virtualenv active
--------------------
    source env/bin/activate

4. exit
-------
remember to save the docker image every time, otherwise all the previous operations will beat the air.

    exit
    docker commit  container进程id image_name

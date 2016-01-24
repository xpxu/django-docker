django-docker-ubunutu
=======================
This project records details about how to run a django server with ubuntu in docker.


1. start up with network setup
-----------
10.245.251.161 is the host ip. convert 80 of host ip to docker 8080

    docker run -i -t  -p 10.245.251.161:80:8080 ubuntu_django


2. proxy setup
--------------
    export HTTP_PROXY=http://www-proxy.us.oracle.com:80
    export HTTPS_PROXY=http://www-proxy.us.oracle.com:80
    export http_proxy=http://www-proxy.us.oracle.com:80
    export https_proxy=http://www-proxy.us.oracle.com:80


3. exit
-------
remember to save the docker image every time, otherwise all the previous operations will beat the air.

    exit
    docker commit  container_id image_name

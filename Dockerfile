FROM ubuntu:16.04
LABEL "Maintainer"="Scott Hansen <firecat4153@gmail.com>"

# Install packages
RUN apt-get update -q && \
    apt-get -qy install git python-setuptools && \
    easy_install --upgrade pip && \
    git clone https://github.com/firecat53/carpool /srv/http/carpool && \
    pip install --upgrade -r /srv/http/carpool/requirements.txt && \
    apt-get autoremove -qy git && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8080

CMD ["/srv/http/carpool/carpool.sh"]

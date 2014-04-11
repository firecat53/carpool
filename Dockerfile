FROM ubuntu:12.04
MAINTAINER Scott Hansen firecat4153@gmail.com

# Install packages
RUN apt-get update && apt-get -y install python-setuptools git
RUN easy_install --upgrade pip

# Download and configure carpool script
RUN git clone https://github.com/firecat53/carpool /srv/http/carpool
RUN pip install --upgrade -r /srv/http/carpool/requirements.txt

EXPOSE 8080

CMD ["/srv/http/carpool/carpool.sh"]

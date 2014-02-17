FROM ubuntu
MAINTAINER Scott Hansen firecat4153@gmail.com

ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python python-pip git

# Download and configure carpool script
RUN git clone https://github.com/firecat53/carpool /srv/http/carpool
RUN chown -R www-data:www-data /srv/http/carpool
RUN pip install --upgrade -r /srv/http/carpool/requirements.txt

EXPOSE 8080

CMD ["/bin/su", "-c", "/srv/http/carpool/carpool.sh", "www-data"]

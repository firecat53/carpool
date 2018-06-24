FROM python:alpine
LABEL "Maintainer"="Scott Hansen <firecat4153@gmail.com>"

# Install packages
RUN apk --no-cache add git && \
    git clone https://github.com/firecat53/carpool.git /srv/http/carpool && \
    pip install --upgrade -r /srv/http/carpool/requirements.txt && \
    adduser -DH carpool && \
    chown -R carpool:users /srv/http/carpool && \
    apk del git

USER carpool
VOLUME /srv/http/carpool/data
WORKDIR /srv/http/carpool/
EXPOSE 8080

CMD ["/srv/http/carpool/carpool.sh"]

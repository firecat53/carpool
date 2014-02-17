Carpool Tracker
===============

Small script to keep track of whose turn it is to drive and total days driven in a calendar year.

Features
--------

- Clicking on a driver moves them to the bottom of the list and adds a date when they drove. 
- Shows most recent date driven
- Tracks number of days driven by each driver
- Add/delete drivers
- Authenticated login (TODO)


License
-------

- MIT

Requirements
------------

1. Python 2.7+ or 3.2+
2. bottle
3. bottle-cork (for authentication) (TODO)

Installation (normal)
---------------------

- Clone app ``git clone https://github.com/firecat53/carpool.git``
- Create virtualenv ``cd carpool && virtualenv --no-site-packages venv && source venv/bin/activate``
- Install requirements ``pip install -r requirements.txt``
- Run server ``python app.py`` and visit http://localhost:8080
- Configure reverse proxy webserver if desired.

Installation (docker)
---------------------
- Copy the Dockerfile into the current directory and run ``sudo docker build -t carpool .``
- Run the data container ``sudo docker run -v /srv/http/carpool/data -name DATA busybox true``
- Run the docker container ``sudo docker run -d -p 8080:8080 --volumes-from DATA carpool:latest``

#!/bin/sh
# Add script to /etc/rc.local or equivalent to run carpool on startup

app_dir="/srv/http/carpool"

cd "$app_dir"
if [ -d "venv" ]; then
	. venv/bin/activate
fi
python app.py > /dev/null

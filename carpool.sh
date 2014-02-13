#!/bin/sh
# Add script to /etc/rc.local or equivalent to run carpool on startup

app_dir="/srv/http/carpool"

cd "$app_dir"
source "venv/bin/activate"
python app.py > /dev/null

#!/bin/bash
DOMAIN="${DOMAIN:localhost}"
DEBUG="$DEBUG"

mkdir -p /var/www/

CONFFILE=/var/www/reviewboard/conf/settings_local.py

if [[ ! -d /var/www/reviewboard ]]; then
    rb-site install --noinput \
        --domain-name="$DOMAIN" \
        --site-root=/ --static-url=static/ --media-url=media/ \
        --db-type=sqlite3 --db-name=/var/www/reviewboard/data/reviewboard.db \
        --web-server-type=lighttpd --web-server-port=8000 \
        --admin-user=ericsson --admin-password=ericsson --admin-email=anderson.parra.de.paula@ericsson.com \
        /var/www/reviewboard/
fi
if [[ "$DEBUG" ]]; then
    sed -i 's/DEBUG *= *False/DEBUG=True/' "$CONFFILE"
fi

exec uwsgi --ini /uwsgi.ini

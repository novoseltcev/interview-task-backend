#!/bin/sh

set -e

. /venv/bin/activate

echo "DB migrating"
while ! flask db upgrade
do
     echo "Retry migrate..."
     sleep 1
done
echo "DB migrated"

while ! update_exchange_rate
do
     echo "Retry update USD exchange rate..."
     sleep 1
done

while ! update_orders
do
     echo "Retry update orders..."
     sleep 1
done

exec gunicorn --bind 0.0.0.0:5000 --forwarded-allow-ips='*' --workers=$WORKERS wsgi:application
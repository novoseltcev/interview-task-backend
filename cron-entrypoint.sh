#!/bin/sh

set -e

. /venv/bin/activate

exec crond -f -l5 -L /app/crontab.log
#!/bin/bash
set -e

# Setup database automatically if needed
#if [ -z "$TAIGA_SKIP_DB_CHECK" ]; then
DB_CHECK_STATUS=$(python /scripts/checkdb.py)
if [[ $DB_CHECK_STATUS == "missing_django_migrations" ]]; then
  echo "Configuring initial database"
  python /home/taiga/taiga-back/manage.py migrate --noinput
  python /home/taiga/taiga-back/manage.py loaddata initial_user
  python /home/taiga/taiga-back/manage.py loaddata initial_project_templates
  #python /home/taiga/taiga-back/manage.py loaddata initial_role
fi
#fi

# Look for static folder, if it does not exist, then generate it
if [ "$(ls -A /home/taiga/taiga-back/static 2> /dev/null)" == "" ]; then
  python /home/taiga/taiga-back/manage.py collectstatic --noinput
fi

exec "$@"
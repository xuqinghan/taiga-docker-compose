#!/bin/bash
set -e


#if [ -z "$TAIGA_SKIP_DB_CHECK" ]; then
DB_CHECK_STATUS=$(python /scripts/checkdb.py)
if [[ $DB_CHECK_STATUS == "missing_django_migrations" ]]; then
  # Setup database automatically if needed
  echo "Configuring initial database"
  python {{BACKEND_SRC_CONTAINER}}/manage.py migrate --noinput
  python {{BACKEND_SRC_CONTAINER}}/manage.py loaddata initial_user
  python {{BACKEND_SRC_CONTAINER}}/manage.py loaddata initial_project_templates
  python {{BACKEND_SRC_CONTAINER}}/manage.py compilemessages
  python {{BACKEND_SRC_CONTAINER}}/manage.py sample_data
fi
#fi

# Look for static folder, if it does not exist, then generate it
if [ "$(ls -A {{BACKEND_STATIC_CONTAINER}} 2> /dev/null)" == "" ]; then
  python {{BACKEND_SRC_CONTAINER}}/manage.py collectstatic --noinput
fi



exec "$@"

#!/bin/sh
set -e

host="$1"
shift
until pg_isready -h "$host" -p 5432 -U order_user; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

>&2 echo "Postgres is up - executing command"
exec "$@"

#!/bin/bash

set -e

HEAVY_META_DB_NAME=${HEAVY_META_DB_NAME:-"heavy_meta-dev"}

# don't fail if the db exists
echo "Creating the database if necessary"
psql -c "create database \"${HEAVY_META_DB_NAME}\";" -U postgres 2> /dev/null || true

echo "Done"

#!/bin/bash
set -e

echo "=== Iniciando Apache Superset ==="

sleep 10

echo "Atualizando banco..."
superset db upgrade

echo "Criando admin..."
superset fab create-admin \
    --username "${ADMIN_USERNAME:-admin}" \
    --firstname "${ADMIN_FIRSTNAME:-Admin}" \
    --lastname "${ADMIN_LASTNAME:-User}" \
    --email "${ADMIN_EMAIL:-admin@superset.local}" \
    --password "${ADMIN_PASSWORD:-admin}" || true

echo "Inicializando..."
superset init

echo "Servidor rodando na porta 8088..."
gunicorn \
    --bind 0.0.0.0:8088 \
    --workers 4 \
    --timeout 120 \
    --limit-request-line 0 \
    --limit-request-field_size 0 \
    "superset.app:create_app()"

FROM apache/superset:latest

USER root

# Drivers de banco de dados (instalando no venv correto)
RUN /app/.venv/bin/pip install --no-cache-dir \
    psycopg2-binary \
    clickhouse-connect \
    trino

# Configuração
COPY superset_config.py /app/pythonpath/superset_config.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER superset

EXPOSE 8088

ENTRYPOINT ["/entrypoint.sh"]

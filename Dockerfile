FROM apache/superset:latest

USER root

# Drivers de banco de dados
RUN pip install --no-cache-dir \
    psycopg2-binary \
    mysqlclient \
    clickhouse-connect \
    pymssql \
    cx_Oracle \
    snowflake-sqlalchemy \
    sqlalchemy-redshift \
    elasticsearch-dbapi \
    sqlalchemy-bigquery \
    trino

# Configuração
COPY superset_config.py /app/pythonpath/superset_config.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER superset

EXPOSE 8088

ENTRYPOINT ["/entrypoint.sh"]

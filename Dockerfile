FROM apache/superset:latest

USER root

# Instalar driver PostgreSQL usando uv (gerenciador de pacotes do Superset)
RUN uv pip install psycopg2-binary

# Configuração
COPY superset_config.py /app/pythonpath/superset_config.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER superset

EXPOSE 8088

ENTRYPOINT ["/entrypoint.sh"]
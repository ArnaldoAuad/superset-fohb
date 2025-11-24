FROM apache/superset:latest

USER root

# Verificar estrutura e instalar
RUN ls -la /app/ && \
    find /app -name "pip" 2>/dev/null && \
    pip install --no-cache-dir psycopg2-binary || \
    python -m pip install --no-cache-dir psycopg2-binary

COPY superset_config.py /app/pythonpath/superset_config.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER superset
EXPOSE 8088
ENTRYPOINT ["/entrypoint.sh"]
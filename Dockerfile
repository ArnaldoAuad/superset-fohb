FROM apache/superset:latest

COPY superset_config.py /app/pythonpath/superset_config.py
COPY entrypoint.sh /entrypoint.sh

USER root
RUN chmod +x /entrypoint.sh
USER superset

EXPOSE 8088
ENTRYPOINT ["/entrypoint.sh"]
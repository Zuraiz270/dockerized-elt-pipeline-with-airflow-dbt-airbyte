FROM python:3.8-slim

RUN apt update && apt install -y wget gnupg2 && \
    echo "deb http://apt.postgresql.org/pub/repos/apt $(grep -oP '(?<=VERSION_CODENAME=)\w+' /etc/os-release)-pgdg main" \
    | tee /etc/apt/sources.list.d/pgdg.list && \
    wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt update && apt install -y postgresql-client-17 cron

COPY start.sh /app/start.sh
COPY elt_script.py .

WORKDIR /app

RUN echo "0 1 * * * python /app/elt_script.py" | crontab -

CMD ["python", "elt_script.py"]
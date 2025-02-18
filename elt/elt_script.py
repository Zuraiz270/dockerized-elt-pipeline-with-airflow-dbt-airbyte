import subprocess
import time

# Function to wait for Postgres to be ready
def wait_for_postgres(host, max_retries=5, delay_seconds=5):
    retries = 0
    while retries < max_retries:
        try:
            subprocess.run(
                [
                    "pg_isready",
                    "-h",
                    host
                ],
                check=True,
                capture_output=True,
                text=True
            )
            print("Postgres is connected")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to Postgres: {e}")
            retries += 1
            print(f"Retrying in {delay_seconds} seconds Attempt {retries}/{max_retries}")
            time.sleep(delay_seconds)
    print("Max retries reached")
    return False
    
if not wait_for_postgres(host="source_postgres"):
    print("Exiting")
    exit(1)

print("Starting ETL script")

source_config = {
    "dbname": "source_db",
    "user": "postgres",
    "password": "secret",
    "host": "source_postgres",
}

destination_config = {
    "dbname": "destination_db",
    "user": "postgres",
    "password": "secret",
    "host": "destination_postgres",
}

dump_command = [
    "pg_dump",
    "-h",
    source_config["host"],
    "-U",
    source_config["user"],
    "-d",
    source_config["dbname"],
    "-f",
    "data_dump.sql",
    "-w"
]

subprocess_env = {
    "PGPASSWORD": source_config["password"]
}
subprocess.run(dump_command, env=subprocess_env, check=True)

load_command = [
    "psql",
    "-h",
    destination_config["host"],
    "-U",
    destination_config["user"],
    "-d",
    destination_config["dbname"],
    "-a",
    "-f",
    "data_dump.sql",
]

subprocess_env = {
    "PGPASSWORD": destination_config["password"]
}

subprocess.run(load_command, env=subprocess_env, check=True)

print("ETL script completed")
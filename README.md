# ELT Pipeline with Airflow, dbt, and Docker

## Overview
This project is an **ELT pipeline** that extracts data from a PostgreSQL database, transforms it using **dbt**, and schedules tasks using **Apache Airflow**. The entire pipeline runs in **Docker** containers.

## Features
- **Airflow** for DAG scheduling
- **dbt** for data transformation & modeling
- **PostgreSQL** as the source database
- **Docker** for containerized deployment
- **Automated Cron Jobs** for scheduled ELT execution

## Project Structure
```
ELT/
│── airflow/
│   ├── dags/
│   │   ├── elt_dag.py  # Airflow DAG for pipeline execution
│   │   ├── airflow.cfg # Airflow configuration
│
│── custom_postgres/
│   ├── dbt_project.yml  # dbt project config
│   ├── models/          # dbt models for transformation
│   ├── macros/          # dbt macros for reusable SQL logic
│   ├── target/          # Compiled dbt models
│
│── elt/
│   ├── elt_script.py    # Python script for ELT execution
│   ├── Dockerfile       # Docker setup for ELT
│
│── source_db_init/
│   ├── init.sql         # SQL script to initialize source database
│
│── docker-compose.yaml  # Docker Compose configuration
│── start.sh             # Startup script for container execution
```

## Setup Instructions
### **1. Clone the Repository**
```sh
git clone <repository-url>
```

### **2. Build and Start the Docker Containers**
```sh
docker-compose up --build -d
```
This will start:
- Airflow Scheduler & Webserver
- PostgreSQL Database
- ELT processing container

### **3. Initialize the Airflow Database**
```sh
docker exec -it airflow-webserver airflow db init
```

### **4. Access the Services**
- **Airflow UI:** `http://localhost:8080` (Default login: `airflow / airflow`)
- **PostgreSQL:** Connect via `localhost:5432`

### **5. Run dbt Transformations**
```sh
docker exec -it elt-container dbt run
```

## Airflow DAGs
The **elt_dag.py** file schedules and executes the pipeline:
- **Extract Data** from PostgreSQL
- **Transform with dbt**
- **Load Processed Data** into final tables

## Cron Job Scheduling
The ELT script runs automatically via **cron**:
```sh
0 1 * * * python /app/elt_script.py
```
This executes the script **every day at 1:00 AM UTC**.

## Git Workflow
### **Committing Changes**
```sh
git status
git add .
git commit -m "Added Airflow DAG and dbt models"
git push origin main
```

## Troubleshooting
### **Check Container Logs**
```sh
docker logs elt-container
```
### **Restart Services**
```sh
docker-compose restart
```

## Contributors
- **Your Name** (Your Email / GitHub Profile)

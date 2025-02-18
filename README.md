For Running PostgreSQL queries on Docker cli:
docker exec -it elt-destination_postgres-1 psql -U postgres -d
 destination_db -c "SELECT * FROM public.actors LIMIT 10;
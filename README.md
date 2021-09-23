# Instalation
# Docker

(Cite Medium article here)

Create the multi-container application:
```commandline
docker compose --env-file ./config/.env up
```

Play with the db:
```commandline
docker exec -it pg_container bash
```

Login:
- Note the parameters below are examples: 
    - test_db is whatever the POSTGRES_DB env var is set to in .env.
    - root is whatever the user is set to in .env.

```commandline
psql -h pg_container -d test_db -U root
```

Remove container
```commandline
docker rm pg_container
```

Remove data from backup volumes:
```commandline
docker-compose down --volumes
```





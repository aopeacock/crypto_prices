FROM postgres:latest
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_USER=test1234
ENV POSTGRES_DB=database
COPY create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql
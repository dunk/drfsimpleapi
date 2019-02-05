FROM python:3.7.2

RUN pip install Django djangorestframework psycopg2-binary
COPY src /src
WORKDIR /src
ENV PATH="/src/simpleproject:${PATH}"

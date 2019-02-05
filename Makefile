.PHONY: run
run:
	docker-compose -p happy up

.PHONY: shell
shell:
	docker-compose -p happy run --rm happyweb manage.py shell

.PHONY: makemigrations
makemigrations:
	docker-compose -p happy run --rm happyweb manage.py makemigrations

.PHONY: migrate
migrate:
	docker-compose -p happy run --rm happyweb manage.py migrate

.PHONY: createsuperuser
createsuperuser:
	docker-compose -p happy run --rm happyweb manage.py createsuperuser --email admin@example.com --username admin

.PHONY: db
db:
	docker exec -it happydb psql -Upostgres -dsimpleapi

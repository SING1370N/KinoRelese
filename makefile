MANAGE = python3 manage.py
run:
	$(MANAGE) runserver 192.168.1.3:8000
rd:
	$(MANAGE) runserver
migrate:
	$(MANAGE) migrate
migrations:
	$(MANAGE) makemigrations
user:
	$(MANAGE) createsuperuser
db:
	rm db.data -f
	$(MANAGE) makemigrations
	$(MANAGE) migrate
	$(MANAGE) createsuperuser --username test --email djh20002@gmail.com
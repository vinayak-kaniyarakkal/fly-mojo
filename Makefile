init:
	pip install -r requirements.txt

clean:
	find . -name '*~' -delete
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

server:
	python flymojo/manage.py runserver

shell:
	python flymojo/manage.py shell

migrate:
	python flymojo/manage.py makemigrations && python flymojo/manage.py migrate

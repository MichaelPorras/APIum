clean:
	find . -name '*.pyc' -delete

celery:
	python runcelery.py -A apium.tasks.jobs worker

server:
	python manage.py runserver --host 0.0.0.0

wipe_db:
	rm -rf db.sqlite3

install:
	pip install -r requirements.txt

serve:
	python manage.py runserver 104.236.60.200:80

clean:
	find . -type f -name '*.pyc' -delete

migrate:
	python manage.py migrate

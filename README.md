# tdt4140G70-backend

## Project setup:

1. Install python3 in your path
2. Elasticsearch (use either i or ii)
    1. Install docker and docker-compose and run `docker-compose up -d`  
    2. Install elasticsearch 5 with the ingest plugin

3. Run the two first queries of [this file](docs/elasticsearch/test.query) against elasticsearch to configure the index

`curl -X PUT 'http://127.0.0.1:9200/_ingest/pipeline/attachment' -d @test.query`

4. Clone and start the django app:

* Linux:
```
git clone git@github.com:orhanhenrik/tdt4140G70-backend.git
cd tdt4140G70-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
* Windows:
```
git clone https://github.com/orhanhenrik/tdt4140G70-backend.git
cd tdt4140G70-backend
py -3 -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

deactivate
```

## Running tests and checking coverage:
```
coverage run --source='.' --omit='venv/*,*/wsgi.py,*/apps.py,*/migrations/*,manage.py'  manage.py test
coverage report
```

## Instructions for use of the system
There are two types of users in the system, professors and students. You should first log in with the professor account, which is the account you created in the `createsuperuser` step of the setup above. This professor can then create a course and some files belonging to this course.  
After you have done this, you can log in as a student. To create a student account you can use the signup form on the website. A student can perform activities like subscribing to courses, downloading and commenting on files, and searching for files.



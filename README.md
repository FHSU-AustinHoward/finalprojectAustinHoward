# finalprojectAustinHoward
The final project for INF601 - Advanced Programming with Python

### Rough Draft - Sites Used
* [NVDLib](https://nvdlib.com/en/latest/v2/startedv2.html)
* [Django](https://docs.djangoproject.com/en/5.0/)
* [NIST NVD](https://nvd.nist.gov/developers/vulnerabilities)


### Rough Draft - Installation Instructions
1. Obtain API Key
2. Install requirements.txt
3. Run env_creator.py

### Rough Draft - Helpful Commands
* Check Django version: ```python -m django --version```
* Create Django project: ```django-admin startproject VULNRbull```
* Create Django application: ```python manage.py startapp devices```
* Setup environment variables: ```python env_creator.py```
* Run the project server: ```python manage.py runserver```
* Create migrations for a particular app: ```python manage.py makemigrations devices```
* Perform the created migrations: ```python manage.py migrate```
* Create Super User ```python manage.py createsuperuser```
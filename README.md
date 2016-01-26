[VERITZA](http://veritza.herokuapp.com/)
=======

Veritza project code repository.

The Veritza platform provides an informational tool to track and analyse
goverment datasets.

### Overview

---
This is a [Django](https://www.djangoproject.com/) power web application.

The main building blocks are:

* [Django](http://www.djangoproject.com/)
* [Postgres](http://www.postgresql.org/) database.

The Django application is hosted on [Heroku](http://heroku.com/)


### Structure

---
![Tree]()

Veritza has been built more or less as a traditional / conventional Django project
with only a few changes:

* local applications have been grouped under the `apps` folder

The local applications all have a similar structure:

![Tree]()

* A **migrations** folder containing database migrations.
* **admin.py** for Admin interface models.
* **forms.py** for web forms.
* **models.py** for database / entity models.
* **urls.py** for url routing patterns.
* **views.py** for django views. These are  [class based views]()


### Set up

---

The application is built on [Django 1.8]() as of writing this documentation.

A typical workflow to get the development environment up running on a Unix like
operating system would be:

1. `cd` to project folder.
2. run `mkvirtualenv strandr --python=/usr/bin/python2` to create a `Python 2`
virtual environment. This step would be default as activate the virtual
environment.
3. run `pip install -r requirements.txt` to install dependencies. The
`requirements.txt` should contain the exact requirements list provide above.
4. resolve packages issues.
5. make a `.env` configuration file. (explained below)
6. run `python manage.py syncdb` to perform database sync.
7. run `python manage.py migrate` to perform database migrations.
8. run `python manage.py runserver` to start the local development server.

This workflow requires that `python2`, `python-virtualenvwrapper`,
`python-virtualenv`, `postgresql`,  or equivalent are already
installed in the system.

##### Configuration files locations

The django development and production environments configurations are defined in the `settings.py`
file in the **config** folder.

By default running `python manage.py runserver` with run the development server using the
development settings.


On a production environment the `wsgi.py` will set up the production configuration as the
default settings.


### Contributors

---
The project is written by [](<mailto:>)

The project documentation done by [Matt Gathu](http://mattgathu.me)  

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
![Tree](https://github.com/padejski/veritzaproto/raw/master/docs/tree.png)

Veritza has been built more or less as a traditional / conventional Django project
with only a few changes:

* local applications have been grouped under the `apps` folder
* configurations are under the `settings` folder


The local applications all have a similar structure:

![Tree](https://github.com/padejski/veritzaproto/raw/master/docs/apptree.png)

* A **migrations** folder containing database migrations.
* A **scrapers** folder containing scraping scripts.
* A **templates** folder containing django view templates.
* An optional **management** folder containig management commands.
* **admin.py** for Admin interface models.
* **models.py** for database / entity models.
* **urls.py** for url routing patterns.
* **views.py** for django views. These are [class based views](https://docs.djangoproject.com/es/1.9/topics/class-based-views/)


### Set up

---

The application is built on [Django 1.8](https://docs.djangoproject.com/en/1.9/releases/1.8/) as of writing this documentation.

A typical workflow to get the development environment up running on a Unix like
operating system would be:

1. `cd` to project folder.
2. run `mkvirtualenv veritza --python=/usr/bin/python2` to create a `Python 2`
virtual environment. This step would be default as activate the virtual
environment.
3. run `pip install -r requirements.txt` to install dependencies. The
`requirements.txt` should contain the exact requirements list provide above.
4. run `python manage.py syncdb` to perform database sync.
5. run `python manage.py migrate` to perform database migrations.
6. run `python manage.py runserver` to start the local development server.


##### Configuration files locations

The django development and production environments configurations are defined
in the `common.py`, `dev.py` and `prod.py` files in the **settings** folder.

By default running `python manage.py runserver` with run the development server using the
development settings.

On a production environment the `wsgi.py` will set up the production configuration as the
default settings.


### Contributors

---
The project is written by [Alexander Stefanov](<mailto:alexander.stefanov@lulin.bg>)
and [Matt Gathu](http://mattgathu.me)

The project documentation done by [Matt Gathu](http://mattgathu.me)  

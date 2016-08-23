# WOYD - Just another Wagtail demo project

This is a demonstration project for Wagtail CMS.

I created a website for a Wedding Planner agency in Wagtail.
I wrote from the first byte of backend to the last byte of frontend and oprations.

This project was not meant to be used as a starting project for yout site.
Please consider this project as an example I wrote to study Wagtail.

I am mainly a frontend developer, and all the scss you will find here
is my from my own, I did not use any framework.

To see how this site looks, go to http://woyd.carlorat.me

I deploy the project using [Fabric](http://www.fabfile.org/), on a [Debian](http://www.debian.org/) vps.

## Requisites

* Python
* Ruby
* NodeJs and npm
* Compass (http://compass-style.org/install/)
* Scss Lint (https://github.com/brigade/scss-lint#installation)

## Installation


1. Clone and enter the project

```
$ git clone git@git.carlorat.me:private/woyd.git
$ cd woyd
```

2. Create a virtualenv (here I am using virtualenvwrapper)

```
mkvirtualenv env_woyd
```

3. Install project requirements

```
$ pip install -r requirements.txt
$ npm install
```

4. Copy and edit example settings file

```
$ cp woyd/settings/dev-example.py woyd/settings/dev.py
$ $EDITOR woyd/settings/dev.py
```

Set the database here to suit your needs. Are you using [PostgreSQL](http://www.postgresql.org), right :) ?

5. Run the migrations

```
python manage.py migrate
```

6. Create a superuser

```
python manage.py createsuperuser
```

7. Run the project

```
python manage.py runserver
```

8. Login to admin, visit ``http://127.0.0.1/admin`` and start adding contents


## TODO

* Tests!
* Give sample assets


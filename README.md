# AMS - XploreTechnologies Project


![AMS preview](screenshot.png "XploreTechnologies site preview")



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
  $ cp xplre/settings/dev-example.py xplore/settings/dev.py
  $ $EDITOR xplore/settings/dev.py
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

8. Login to admin, visit http://127.0.0.1/admin and start adding contents


## TODO

* Tests!
* Give sample assets


To Run Zenfeat Test Project.

First Please try to install virutalenv by using `pip install virtualenv` command.

After than setup virutal enviroment using `virutalenv .venv` command.

Activate `.vevn` using bin/activate.

Run `pip install django django-redis`

Please note that redis should be running on local system.

After than

Run following commands.

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

Then test project will running on port 8000.

Able to visit Admin page `localhost:8000/admin` able to login with superuser credentials that you created just before.

Regards.

Thanks.

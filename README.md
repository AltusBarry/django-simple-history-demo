# django-simple-history-demo

Usage
-----

Create a postgres db::

    createuser --interactive demoversion
    createdb demoversion --owner=demoversion

Ready env::

    virtualenv ve -p python3.8
    ./ve/bin/pip install -r requirements.txt
    ./ve/bin/python manage.py migrate
    ./ve/bin/python manage.py createsuperuser

Create some polls, will take a while::

    ./ve/bin/python manage.py createmanypolls
Creates Questions and Choices via nested loops. Then uses the bulk create util from simple history to create more questions.

Start the django server::

    ./ve/bin/python manage.py runserver

Browse to http://localhost:8000/admin

Login and check the history of various objects. History button is located on object detail page, the same button we always used to see the basic Django change history.

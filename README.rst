=====
Django Tabulate
=====

Django Tabulate is a simple app on top of Python tabulate, but for Django querysets.
It allows us to to Pretty-print Django QuerySets

Requirements
------------
* **Python**: 2.7, 3.5
* **Django**: 1.8, 1.11
* **tabulate**: 0.8.1

Tested on these, but should still work on all actively supported Python and Django versions.

Installation
------------

Install using pip:

.. code-block:: sh

    pip install django-tabulate


Usage
-----

You can use it as a function:


.. code-block:: python

    from myapp.models import MyModel
    from django_tabulate import tabulate_qs
    print tabulate_qs(MyModel.objects.all())
    +------+----------+
    |   id | name     |
    |------+----------|
    |    1 | Python   |
    |    2 | Django   |
    |    3 | Tabulate |
    +------+----------+

Or as a QuerySet mixin:

.. code-block:: python
    
    #models.py
    from django.db import models
    from django_tabulate import TabulateMixin

    class MyModelQuerySet(models.QuerySet, TabulateMixin):
        pass

    class MyModel(models.Model):
        name = models.CharField(max_length=255)
        
        objects = MyModelQuerySet.as_manager()

    #then in the shell
    from myapp.models import MyModel
    print MyModel.objects.all().tabulate()

Settings
-----------

You can override all default tabulate settings via `TABULATE_DEFAULTS`

.. code-block:: python
    TABULATE_DEFAULTS = {
        'tablefmt': 'psql'
    }

For a complete list of all tabulate options take a look at 
https://bitbucket.org/astanin/python-tabulate/overview
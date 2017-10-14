=====
Django Tabulate
=====

Django Tabulate is a simple Django app on top of Python tabulate, but for querysets.

Quick start
-----------

1. Install django-tabulate from pip::

    pip install django-tabulate

2. Lets your QuerySet Inherit from `TabulateMixin` or `TabulateQuerySet`:

    from django_tabulate import TabulateMixin

    class MyQuerySet(TabulateMixin, models.QuerySet):
        #...

    class MyModel(models.Model):
        #...

        objects = MyQuerySet.as_manager()
        #if we have a manager, then
        objects = MyManager.from_queryset(MyQuerySet)()

4. Start the python shell
    
    python manage.py shell

5. Tabulate a QuerySet
    
    from myapp.models import MyModel
    print MyModel.objects.all().tabulate()
from django.db import models
from django_tabulate.base import tabulate_qs

class TabulateMixin(object):
    def tabulate(self, **kwargs):
        return tabulate_qs(self, **kwargs)

class TabulateQuerySet(TabulateMixin, models.QuerySet):
    pass
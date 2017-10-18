from django.db import connections
from django.conf import settings
from tabulate import tabulate as tblt

def tabulate_qs(qs, **kwargs):
    """Tabulates a Django Queryset"""
    cursor = connections[qs.db].cursor()
    cursor.execute(*qs.query.sql_with_params())
    columns = [col[0] for col in cursor.description]
    options = getattr(settings, 'TABULATE_DEFAULTS', {}).copy()
    options.update(kwargs)
    return tblt(cursor.fetchall(), headers=columns, **options)
from django.db import models
from django.db import connections
from tabulate import tabulate as tblt

class TabulateMixin(object):
    def tabulate(self, *args, **kwargs):
        # tablefmt="simple",
        # floatfmt=_DEFAULT_FLOATFMT,
        # numalign="decimal", stralign="left",
        # missingval=_DEFAULT_MISSINGVAL, 
        # showindex="default", 
        # disable_numparse=False
        # return tblt(self.values(), headers='keys', *args, **kwargs)
        cursor = connections[self.db].cursor()
        cursor.execute(*self.query.sql_with_params())
        columns = [col[0] for col in cursor.description]
        return tblt(cursor.fetchall(), headers=columns, *args, **kwargs)

class TabulateQuerySet(TabulateMixin, models.QuerySet):
    pass
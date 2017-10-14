from django.db import models
from django_tabulate.mixins import TabulateQuerySet

class BookTabulateQuerySet(TabulateQuerySet):
	pass

class Book(models.Model):
	name = models.CharField(max_length=255)
	
	objects = BookTabulateQuerySet.as_manager()
from django.test import TestCase
from django.db.models import Count
from tests.models import Book
from django_tabulate import tabulate_qs

class TabulateTests(TestCase):

    def setUp(self):
        Book.objects.create(name='Python')
        Book.objects.create(name='Django')
        Book.objects.create(name='Tabulate')
 
    def test_method_execution(self):
        qs = Book.objects.all()
        self.assertEqual(qs.tabulate(), '\n'.join([
            '  id  name',
            '----  --------',
            '   1  Python',
            '   2  Django',
            '   3  Tabulate',
        ]))

        self.assertEqual(qs.tabulate(), tabulate_qs(qs))

    def test_kwargs_execution(self):
        qs = Book.objects.all()
        self.assertEqual(qs.tabulate(tablefmt='grid'), '\n'.join([
            '+------+----------+',
            '|   id | name     |',
            '+======+==========+',
            '|    1 | Python   |',
            '+------+----------+',
            '|    2 | Django   |',
            '+------+----------+',
            '|    3 | Tabulate |',
            '+------+----------+',
        ]))

    def test_values_with_annotation(self):
        qs = Book.objects.values('name').annotate(Count('pk'))
        self.assertEqual(qs.tabulate(tablefmt='psql'), '\n'.join([
            '+----------+-------------+',
            '| name     |   pk__count |',
            '|----------+-------------|',
            '| Django   |           1 |',
            '| Python   |           1 |',
            '| Tabulate |           1 |',
            '+----------+-------------+',
        ]))
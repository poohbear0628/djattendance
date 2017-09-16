from django.core.management.base import BaseCommand

from books.models import Publisher, Author, Book

class Command(BaseCommand):
  def handle(self, *args, **options):
    print('* Populating books...')
    p = Publisher(name='Living Stream Ministry', code='LSM')
    p.save()
    a = Author(first_name='Witness', last_name='Lee')
    a.save()
    b = Book(publisher=p, name='Experience of Life', chapters=20)
    b.save()
    b.author = (a,)
    b.save()

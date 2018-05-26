from django.core.management.base import BaseCommand

from books.models import Publisher, Author, Book

from collections import OrderedDict

lifestudies = [
    ('Genesis', 120), ('Exodus', 185), ('Leviticus', 64), ('Numbers', 53), ('Deutoronomy', 30), ('Joshua', 15), ('Judges', 10),
    ('Ruth', 8), ('1 & 2 Samuel', 38), ('1 & 2 Kings', 23), ('1 & 2 Chronicles', 13), ('Ezra', 5), ('Nehemiah', 5), ('Esther', 2),
    ('Job', 38), ('Psalms', 45), ('Proverbs', 8), ('Ecclesiastes', 2), ('Song of Songs', 10),
    ('Isaiah', 54), ('Jeremiah', 40), ('Lamentations', 4), ('Ezekiel', 27), ('Daniel', 17),
    ('Hosea', 8), ('Joel', 7), ('Amos', 3), ('Obadiah', 1), ('Jonah', 1), ('Micah', 4),
    ('Nahum', 1), ('Habakkuk', 3), ('Zephaniah', 1), ('Haggai', 1), ('Zechariah', 15), ('Malachi', 4),
    ('Matthew', 72), ('Mark', 70), ('Luke', 79), ('John', 51), ('Acts', 72),
    ('Romans', 69), ('1 Corinthians', 69), ('2 Corinthians', 59),
    ('Galatians', 46), ('Ephesians', 97), ('Philippians', 62), ('Colossians', 65),
    ('1 Thessalonians', 24), ('2 Thessalonians', 7), ('1 Timothy', 12), ('2 Timothy', 8), ('Titus', 6),
    ('Philemon', 2), ('Hebrews', 69), ('James', 14), ('1 Peter', 34), ('2 Peter', 13), ('1 John', 40),
    ('2 John', 2), ('3 John', 2), ('Jude', 5), ('Revelation', 68)
]


class Command(BaseCommand):
  def handle(self, *args, **options):
    Book.objects.all().delete()
    Publisher.objects.all().delete()
    Author.objects.all().delete()
    print('* Populating books...')
    orderedLS = OrderedDict(lifestudies)
    p = Publisher(name='Living Stream Ministry', code='LSM')
    p.save()
    a = Author(first_name='Witness', last_name='Lee')
    a.save()
    for b, c in orderedLS.items():
      print b
      b = Book(publisher=p, name=b, chapters=c)
      b.save()
      b.author = (a,)
      b.save()

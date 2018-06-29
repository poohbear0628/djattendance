from django.contrib import admin
from bible_tracker.models import BibleReading

class BibleReadingAdmin(admin.ModelAdmin):
  ordering = ('trainee',)

  def weekly_reading_count(obj):
    return len(obj.weekly_reading_status)

  def books_read_count(obj):
    return len(obj.books_read)


  list_display = ('trainee', weekly_reading_count, books_read_count)
  search_fields = ['trainee__firstname', 'trainee__lastname']  # to search up trainees


admin.site.register(BibleReading, BibleReadingAdmin)
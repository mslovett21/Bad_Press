from django.contrib import admin

# Register your models here.

from .models import Source, State, Issue, Article, Candidate, Cloud, Popularity

#admin.site.register(Source)
#admin.site.register(State)
#admin.site.register(Issue)
#admin.site.register(Article)
#admin.site.register(Candidate)
# Define the admin class
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'party', 'state', 'date_of_birth')
    list_filter = ('party', 'state')

# Register the admin class with the associated model
admin.site.register(Candidate, CandidateAdmin)

# Register the Admin classes for Article using the decorator

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'candidate', 'state', 'issue', 'source', 'link')

# Register the Admin classes for BookInstance using the decorator

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'URL_logo')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'primaries_date', 'URL_logo')

# Register the Admin classes for BookInstance using the decorator

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'URL_logo')

@admin.register(Cloud)
class CloudAdmin(admin.ModelAdmin):
    list_display = ('id',
      'word_1',
      'word_2',
      'word_3',
      'word_4',
      'word_5',
      'word_6',
      'word_7',
      'word_8',
      'word_9',
      'word_10',
      'word_11',
      'word_12',
      'word_13',
      'word_14',
      'word_15',
      'word_16',
      'word_17',
      'word_18',
      'word_19',
      'word_20')

@admin.register(Popularity)
class PopularityAdmin(admin.ModelAdmin):
    list_display = ('id',
      'april',
      'may',
      'june',
      'july',
      'august',
      'september',
      'october',
      'november',
      'december',
      'january',
      'february',
      'march')

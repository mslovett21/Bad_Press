from django.contrib import admin

# Register your models here.

from .models import Source, State, Issue, Article, Candidate

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


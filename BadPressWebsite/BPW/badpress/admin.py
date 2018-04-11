from django.contrib import admin

# Register your models here.
'''
from .models import Candidate, Article, Issue, Stateresults

admin.site.register(Genre)

# Define the admin class
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name']

# Register the admin class with the associated model
admin.site.register(Candidate, CandidateAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('newspaper', 'title', 'date')

@admin.register(BookInstance)
class IssueAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('name', 'info')
        }),
    )
    '''

from django.db import models

# Create your models here.

class Source(models.Model):
    """
    Model representing article source.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    URL_logo = models.CharField(max_length=250)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class State(models.Model):
    """
    Model representing article source.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length=250)
    primaries_date = models.DateField(null=True, blank=True)
    URL_logo = models.CharField(null=True, max_length=1000)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Issue(models.Model):
    """
    Model representing article source.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    info = models.TextField(max_length=1000)
    URL_logo = models.CharField(max_length=250)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Article(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey('Candidate', on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    issue = models.ForeignKey('Issue', on_delete=models.SET_NULL, null=True)
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Candidate as a string rather than object because it hasn't been declared yet in the file.
    link = models.CharField(max_length=250)
    sentiment_score = models.IntegerField()
    summary = models.TextField(max_length=5000, help_text='Enter a brief description of the article')
    date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=250)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('article-detail', args=[str(self.id)])


class Candidate(models.Model):
    """
    Model representing a candidate.
    """
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    place_birth = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    CANDIDATE_POSITION  = (
        ('r', 'Republican'),
        ('d', 'Democrat'),
        ('i', 'Independent'),
    )
    party = models.CharField(max_length=1, choices=CANDIDATE_POSITION, blank=True)
    URL_photo = models.CharField(max_length=250)
    #party = models.CharField(max_length=100)
    score_issue_1 = models.IntegerField()
    score_issue_2 = models.IntegerField()
    score_issue_3 = models.IntegerField()
    score_issue_4 = models.IntegerField()
    score_issue_5 = models.IntegerField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular candidate instance.
        """
        return reverse('candidate-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} {1}'.format(self.first_name, self.last_name)
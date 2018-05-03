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
    name = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    place_birth = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    CANDIDATE_POSITION  = (
        ('r', 'Republican'),
        ('d', 'Democrat'),
        ('i', 'Independent'),
        ('o','Other'),
    )
    party = models.CharField(max_length=1, choices=CANDIDATE_POSITION, blank=True)
    URL_photo = models.CharField(max_length=250)
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

class Cloud(models.Model):
    """
    Model representing word cloud.
    """
    id = models.OneToOneField('Candidate', on_delete=models.CASCADE, primary_key=True, null=False)
    word_1 = models.CharField(max_length=250)
    word_2 = models.CharField(max_length=250)
    word_3 = models.CharField(max_length=250)
    word_4 = models.CharField(max_length=250)
    word_5 = models.CharField(max_length=250)
    word_6 = models.CharField(max_length=250)
    word_7 = models.CharField(max_length=250)
    word_8 = models.CharField(max_length=250)
    word_9 = models.CharField(max_length=250)
    word_10 = models.CharField(max_length=250)
    word_11 = models.CharField(max_length=250)
    word_12 = models.CharField(max_length=250)
    word_13 = models.CharField(max_length=250)
    word_14 = models.CharField(max_length=250)
    word_15 = models.CharField(max_length=250)
    word_16 = models.CharField(max_length=250)
    word_17 = models.CharField(max_length=250)
    word_18 = models.CharField(max_length=250)
    word_19 = models.CharField(max_length=250)
    word_20 = models.CharField(max_length=250)

class Popularity(models.Model):
    """
    Model representing word cloud.
    """
    id = models.OneToOneField('Candidate', on_delete=models.CASCADE, primary_key=True, null=False)
    april = models.IntegerField()
    may = models.IntegerField()
    june = models.IntegerField()
    july = models.IntegerField()
    august = models.IntegerField()
    september = models.IntegerField()
    october = models.IntegerField()
    november = models.IntegerField()
    december = models.IntegerField()
    january = models.IntegerField()
    february = models.IntegerField()
    march = models.IntegerField()

database_up_to_date=True
statelist = []
candidatelist = []
if database_up_to_date:
    pass
else:
    with open("states.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            namef = line[0]
            URL_logof = line[1]
            primaries_datef = line[2]
            object = State.objects.create( name=namef, primaries_date=primaries_datef, URL_logo=URL_logof )
            object.save()
            statelist.append(object)

    with open("sources.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            namef = line[0]
            URL_logof = line[1]
            object = Source.objects.create( name=namef, URL_logo=URL_logof )
            object.save()

    with open("issues.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            namef = line[0]
            infof = line[1]
            URL_logof = line[2]
            object = Issue.objects.create( name=namef, info=infof, URL_logo=URL_logof )
            object.save()

    with open("candidates.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            statef = line[1]
            if statef=="West_Virgina":
                stateobject=statelist[0]
            elif statef=="Virginia":
                stateobject=statelist[1]
            else:
                stateobject=statelist[2]
            namef = line[0]
            first_namef = line[7]
            last_namef = line[8]
            date_of_birthf = line[2]
            place_birthf = line[3]
            positionf = line[4]
            partyf  = line[6]
            URL_photof = line[5]
            score_issue_1f = line[9]
            score_issue_2f = line[10]
            score_issue_3f = line[11]
            score_issue_4f = line[12]
            score_issue_5f = line[13]
            object = Candidate.objects.create(
                state=stateobject,
                name=namef,
                first_name=first_namef,
                last_name=last_namef,
                date_of_birth=date_of_birthf,
                place_birth=place_birthf,
                position=positionf,
                party=partyf,
                URL_photo=URL_photof,
                score_issue_1=score_issue_1f,
                score_issue_2=score_issue_2f,
                score_issue_3=score_issue_3f,
                score_issue_4=score_issue_4f,
                score_issue_5=score_issue_5f )
            object.save()
            candidatelist.append(object)

    with open("popularity.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            a_candidate = line[4]
            if a_candidate==1:
                popularityobject=candidatelist[0]
            elif a_candidate==2:
                popularityobject=candidatelist[1]
            elif a_candidate==3:
                popularityobject=candidatelist[2]
            elif a_candidate==4:
                popularityobject=candidatelist[3]
            elif a_candidate==5:
                popularityobject=candidatelist[4]
            elif a_candidate==6:
                popularityobject=candidatelist[5]
            elif a_candidate==7:
                popularityobject=candidatelist[6]
            elif a_candidate==8:
                popularityobject=candidatelist[7]
            elif a_candidate==9:
                popularityobject=candidatelist[8]
            elif a_candidate==10:
                popularityobject=candidatelist[9]
            elif a_candidate==11:
                popularityobject=candidatelist[10]
            elif a_candidate==12:
                popularityobject=candidatelist[11]
            elif a_candidate==13:
                popularityobject=candidatelist[12]
            elif a_candidate==14:
                popularityobject=candidatelist[13]
            elif a_candidate==15:
                popularityobject=candidatelist[14]
            elif a_candidate==16:
                popularityobject=candidatelist[15]
            else:
                popularityobject=candidatelist[16]
            idf = popularityobject
            aprilf = line[0]
            mayf = line[9]
            junef = line[7]
            julyf = line[6]
            augustf = line[1]
            septemberf = line[12]
            octoberf = line[11]
            novemberf = line[10]
            decemberf = line[2]
            januaryf = line[5]
            februaryf = line[3]
            marchf = line[8]
            object = Popularity.objects.create(
                id = idf,
                april = aprilf,
                may = mayf,
                june = junef,
                july = julyf,
                august = augustf,
                september = septemberf,
                october = octoberf,
                november = novemberf,
                december = decemberf,
                january = januaryf,
                february = februaryf,
                march = marchf )
            object.save()

    with open("cloud.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            a_candidate = line[0]
            if a_candidate==1:
                a_object=candidatelist[0]
            elif a_candidate==2:
                a_object=candidatelist[1]
            elif a_candidate==3:
                a_object=candidatelist[2]
            elif a_candidate==4:
                a_object=candidatelist[3]
            elif a_candidate==5:
                a_object=candidatelist[4]
            elif a_candidate==6:
                a_object=candidatelist[5]
            elif a_candidate==7:
                a_object=candidatelist[6]
            elif a_candidate==8:
                a_object=candidatelist[7]
            elif a_candidate==9:
                a_object=candidatelist[8]
            elif a_candidate==10:
                a_object=candidatelist[9]
            elif a_candidate==11:
                a_object=candidatelist[10]
            elif a_candidate==12:
                a_object=candidatelist[11]
            elif a_candidate==13:
                a_object=candidatelist[12]
            elif a_candidate==14:
                a_object=candidatelist[13]
            elif a_candidate==15:
                a_object=candidatelist[14]
            elif a_candidate==16:
                a_object=candidatelist[15]
            else:
                a_object=candidatelist[16]
            idf = a_object
            word_1f = line[1]
            word_2f = line[2]
            word_3f = line[3]
            word_4f = line[4]
            word_5f = line[5]
            word_6f = line[6]
            word_7f = line[7]
            word_8f = line[8]
            word_9f = line[9]
            word_10f = line[10]
            word_11f = line[11]
            word_12f = line[12]
            word_13f = line[13]
            word_14f = line[14]
            word_15f = line[15]
            word_16f = line[16]
            word_17f = line[17]
            word_18f = line[18]
            word_19f = line[19]
            word_20f = line[20]
            object = Cloud.objects.create(
                id = idf,
                word_1 = word_1f,
                word_2 = word_2f,
                word_3 = word_3f,
                word_4 = word_4f,
                word_5 = word_5f,
                word_6 = word_6f,
                word_7 = word_7f,
                word_8 = word_8f,
                word_9 = word_9f,
                word_10 = word_10f,
                word_11 = word_11f,
                word_12 = word_12f,
                word_13 = word_13f,
                word_14 = word_14f,
                word_15 = word_15f,
                word_16 = word_16f,
                word_17 = word_17f,
                word_18 = word_18f,
                word_19 = word_19f,
                word_20 = word_20f )
            object.save()

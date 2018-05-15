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
    issue_id=models.IntegerField(default=6)
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
    article_id=models.IntegerField(default=1)
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
    candidate_id=models.IntegerField(default=1)
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
    id =models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=250,default="LASt")
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
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=250,default="LAST")
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


STATES_UP_TO_DATE     = False
SOURCES_UP_TO_DATE    = False
ISSUES_UP_TO_DATE     = False
CANDIDATE_UP_TO_DATE  = False
POPULARITY_UP_TO_DATE = False
CLOUD_UP_TO_DATE      = False
ARTICLES_UP_TO_DATE   = False
'''

STATES_UP_TO_DATE     = True
SOURCES_UP_TO_DATE    = True
ISSUES_UP_TO_DATE     = True
CANDIDATE_UP_TO_DATE  = True
POPULARITY_UP_TO_DATE = True
CLOUD_UP_TO_DATE      = True
ARTICLES_UP_TO_DATE   = True

'''


statelist = []
candidatelist = []
issue_list =[]
source_list=[]

if STATES_UP_TO_DATE:
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


if SOURCES_UP_TO_DATE:
    pass
else:
    with open("sources.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            namef = line[0]
            URL_logof = line[1]
            object = Source.objects.create( name=namef, URL_logo=URL_logof )
            object.save()
            source_list.append(object)

if ISSUES_UP_TO_DATE:
    pass
else:
    j_issue=1
    with open("issues.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split('"')
            namef = line[0]
            infof = line[1]
            URL_logof = line[2]
            object = Issue.objects.create( name=namef,issue_id=j_issue, info=infof, URL_logo=URL_logof )
            object.save()
            issue_list.append(object)
            j_issue=j_issue+1

if CANDIDATE_UP_TO_DATE:
    pass
else:
    j_candidate=1
    with open("candidates.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            statef = line[1]
            if statef=="West_Virginia":
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
                candidate_id=j_candidate,
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
            print(object.__str__())
            candidatelist.append(object)
            j_candidate=j_candidate+1


if POPULARITY_UP_TO_DATE:
    pass
else:
    with open("popularity.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            last_namef = line[12]
            aprilf = line[0]
            mayf = line[1]
            junef = line[2]
            julyf = line[3]
            augustf = line[4]
            septemberf = line[5]
            octoberf = line[6]
            novemberf = line[7]
            decemberf = line[8]
            januaryf = line[9]
            februaryf = line[10]
            marchf = line[11]
            object = Popularity.objects.create(
                last_name = last_namef,
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


if CLOUD_UP_TO_DATE:
    pass
else:
    with open("cloud.csv", "r" ) as source:
        for line in source:
            line = line.strip()
            line = line.split(',')
            last_namef = line[21]
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
                last_name=last_namef,
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

if ARTICLES_UP_TO_DATE:
    pass
else:
    i=0
    j_article=1
    with open("articles.csv", "r" ) as articles:
            for line in articles:
                line = line.strip()
                line = line.split('\t')
                if len(line)==9:
                    datet=line[0]
                    linkt=line[1]
                    titlet=line[2]
                    summaryt=line[6]
                    sentiment_scoret=line[7]
                    issue_fk= int(line[8])
                    state_fk=int(line[5])
                    candi_fk=int(line[3])
                    source_fk=int(line[4])
                    issue_object=issue_list[0]
                    state_object=statelist[0]
                    candi_object=candidatelist[0]
                    source_object=source_list[0]
                    if issue_fk == 1:
                        issue_object =issue_list[0]
                    elif issue_fk == 2:
                        issue_object=issue_list[1]
                    elif issue_fk == 3:
                        issue_object =issue_list[2]
                    elif issue_fk == 4:
                        issue_object=issue_list[3]
                    elif issue_fk == 5:
                        issue_object=issue_list[4]
                    else:
                        issue_object =issue_list[5]
                    if state_fk== 1:
                        state_object=statelist[0]
                    elif state_fk== 2:
                        state_object=statelist[1]
                    else:
                        state_object=statelist[2]
                    if source_fk == 1:
                        source_object=source_list[0]
                    elif source_fk == 2:
                        source_object=source_list[1]
                    else:
                        source_object=source_list[2]
                    if candi_fk==1:
                        candi_object=candidatelist[0]
                    elif candi_fk==2:
                        candi_object=candidatelist[1]
                    elif candi_fk==3:
                        candi_object=candidatelist[2]
                    elif candi_fk==4:
                        candi_object=candidatelist[3]
                    elif candi_fk==5:
                        candi_object =candidatelist[4]
                    elif candi_fk==6:
                        candi_object =candidatelist[5]
                    elif candi_fk==7:
                        candi_object =candidatelist[6]
                    elif candi_fk ==8:
                        candi_fk =candidatelist[7]
                    elif candi_fk ==9:
                        candi_object =candidatelist[8]
                    elif candi_fk ==10:
                        candi_object=candidatelist[9]
                    elif candi_fk==11:
                        candi_object =candidatelist[10]
                    elif candi_fk==12:
                        candi_object =candidatelist[11]
                    elif candi_fk==13:
                        candi_object =candidatelist[12]
                    elif candi_fk==14:
                        candi_object=candidatelist[13]
                    elif candi_fk==15:
                        candi_object=candidatelist[14]
                    elif candi_fk==16:
                        candi_object=candidatelist[15]
                    else:
                        candi_object= candidatelist[16]
                    print("candi object")
                    print(candi_object.__str__())
                    print(candi_fk)
                    object = Article.objects.create(
                            candidate = candi_object,
                            state = state_object,
                            article_id=j_article,
                            issue = issue_object,
                            source =  source_object,
                            link = linkt,
                            sentiment_score =sentiment_scoret,
                            summary = summaryt,
                            date = datet,
                            title = titlet
                        )
                    object.save()
                    i=i+1
                    j_article=j_article+1
                else:
                    pass

'''
'''
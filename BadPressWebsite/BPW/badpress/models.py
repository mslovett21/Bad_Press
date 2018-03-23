from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class state(models.Model):
	name=models.CharField(max_length=50)
	info=models.TextField()
	URL_logo=models.CharField(max_length=250)

def __str__(self):
	return self.name
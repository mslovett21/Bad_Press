from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class State(models.Model):
    """
    Model representing a state.
    """
    state_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """
        Returns the url to access a particular state instance.
        """
        return reverse('state-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.state_name


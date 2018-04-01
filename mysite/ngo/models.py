from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User

# Create your models here.
class Ngo(models.Model):
    ngo_name = models.CharField(max_length=250)
    ngo_logo = models.CharField(max_length=500)
    ngo_loc = models.CharField(max_length=500)
    relief_type = models.CharField(max_length=500)
    # created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ngo_name+'-'+self.relief_type+'--'+self.ngo_loc
    
    def get_absolute_url(self):
        return reverse('ngo-details',kwargs={'pk':self.pk})

class NgoDetails(models.Model):
    name = models.ForeignKey(Ngo,on_delete=models.CASCADE)
    details = models.TextField(max_length = 5000)
    address = models.TextField(max_length = 5000)

    def __str__(self):
        return self.name
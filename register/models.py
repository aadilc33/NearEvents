from django.db import models

# Create your models here.
class MyclubUsers(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.first_name +" "+self.last_name


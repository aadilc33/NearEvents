from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue name',max_length=200)
    address = models.CharField(max_length=500)
    zip_code=models.CharField('Zip Code',max_length=15)
    phone=models.CharField('Contact Number',max_length=15,blank=True)
    Web =models.URLField('Website Address',blank=True)
    email_address=models.EmailField('Email Address',blank=True)
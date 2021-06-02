from django.db import models

# Create your models here.
class Foods(models.Model):
    donatorName = models.CharField(max_length=100)
    donatorMobile = models.CharField(max_length=100)
    donationAddress = models.TextField()
    landMark = models.CharField(max_length=100)
    foodType = models.CharField(max_length=100)
    foodName = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    pickupDate = models.CharField(max_length=100)
    preferedTime = models.CharField(max_length=100)
    foodDescription = models.TextField()
    latitude = models.FloatField()
    longititude = models.FloatField()
    def __str__(self):
        return self.donatorMobile


class Cloths(models.Model):
    donatorName = models.CharField(max_length=100)
    donatorMobile = models.CharField(max_length=100)
    donationAddress = models.TextField()
    landMark = models.CharField(max_length=100)
    clothsType = models.CharField(max_length=100)
    clothsName = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    pickupDate = models.CharField(max_length=100)
    preferedTime = models.CharField(max_length=100)
    clothsDescription = models.TextField()
    latitude = models.FloatField()
    longititude = models.FloatField()
    def __str__(self):
        return self.donatorMobile

class Books(models.Model):
    donatorName = models.CharField(max_length=100)
    donatorMobile = models.CharField(max_length=100)
    donationAddress = models.TextField()
    landMark = models.CharField(max_length=100)
    booksType = models.CharField(max_length=100)
    booksName = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    pickupDate = models.CharField(max_length=100)
    preferedTime = models.CharField(max_length=100)
    booksDescription = models.TextField()
    latitude = models.FloatField()
    longititude = models.FloatField()
    def __str__(self):
        return self.donatorMobile
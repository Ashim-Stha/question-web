from django.db import models

# Create your models here.
class Questionpaper(models.Model):
    croppedno=models.IntegerField()
    faculty=models.CharField(max_length=4)
    semester=models.IntegerField()
    year=models.IntegerField()


class ioequestionpaper(models.Model):
    croppedno=models.IntegerField()
    faculty=models.CharField(max_length=4)
    semester=models.IntegerField()
    year=models.IntegerField()
    imagecropped=models.BinaryField()
    desc=models.TextField()
    keyword=models.TextField()


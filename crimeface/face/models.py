from django.db import models

from django import forms
# Create your models here.
class criminaldata(models.Model):

	Name = models.CharField(max_length = 255)
	FathersName = models.CharField(max_length = 255)
	MothersName = models.CharField(max_length = 255)
	Gender = models.CharField(max_length = 255)
	DOB = models.CharField(max_length = 255)
	BloodGroup = models.CharField(max_length = 255)
	IdentificationMark = models.CharField(max_length = 255)
	Nationality = models.CharField(max_length = 255)
	Religion = models.CharField(max_length = 255)
	CrimesDone = models.CharField(max_length = 255)

class Image(models.Model):
	Image = models.ImageField(upload_to = 'profile_pics',null = True,blank = True)

	def __str__(self):
		return f'{self.Image.url}'
# Create your models here.

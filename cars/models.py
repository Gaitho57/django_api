from django.db import models

class Car(models.Model):
	name = models.CharField(max_length=200)
	model = models.CharField(max_length=200)
	year = models.IntegerField()

	def __str__(self):
	    return self.name 
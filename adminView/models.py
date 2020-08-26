from django.db import models
from .validators import validate_name,validate_description
# Create your models here.

class Hajime(models.Model):
	name 		= models.CharField(max_length=25, null= True, validators=[validate_name])
	description = models.CharField(max_length=100, null= True, validators=[validate_description])

	JURUSAN = (
		('RPL','RPL'),
		('TKJ','TKJ'),
		('MM','MM'),
	)
	majors = models.CharField(max_length=20, choices=JURUSAN, default='RPL')

	def get_absolute_url(self):
		return '/'

	def __str__(self):
		return self.name





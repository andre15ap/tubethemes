from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Theme(models.Model):
	name = models.CharField('Theme Name', max_length=100)
	media_thumbs = models.FloatField(default=0)

	def __str__(self):
		return self.name[:20]
	
	def update_thumbs(self):
		tubes = Tube.objects.filter(theme=self)
		up = 0
		down = 0
		for tube in tubes:
			up += tube.thumbs_up
			down += tube.thumbs_down
		result = up - (down / 2)
		self.media_thumbs = result
		print('---------- salved ',self.media_thumbs)
		self.save()

class Tube(models.Model):
	name = models.CharField('Tube Name', max_length=200)
	description = models.TextField('Description', null=True, blank=True)
	link = models.CharField('link', max_length=255)
	theme = models.ForeignKey(Theme, null=True, on_delete=models.SET_NULL)
	thumbs_up = models.PositiveIntegerField(default=0)
	thumbs_down = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL )


	def __str__(self):
		return self.name
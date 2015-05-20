from django.db import models


class Picture(models.Model):
	author = models.CharField(max_length=100)
	gallery_name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField()
	created = models.DateTimeField()
	pic = models.ImageField(upload_to='pic')
	def __unicode__(self):
		return self.gallery_name

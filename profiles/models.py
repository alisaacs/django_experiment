from django.db import models
from django.utils import timezone

class advert(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	featured = models.BooleanField(default=False)

	def publish(self):
		self.save()

#	For future use

#	def feature(self):
#		pass

	def __str__(self):
		return self.title
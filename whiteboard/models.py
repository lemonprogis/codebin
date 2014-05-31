from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	user = models.ForeignKey(User)
	datetime = models.DateTimeField(auto_now_add=True)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return "%s" % (self.title)


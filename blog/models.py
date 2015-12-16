#import bits from other files
from django.db import models
from django.utils import timezone

#define new model called Post
#models.Model - specifies it's a Django Model, save in the db
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

#method/function to publish
def publish(self):
	self.published_date = timezone.now()
	self.save()

#return text(string) with Post title
def __str__(self):
	return self.title

	
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User, default=1)
  likes = models.ManyToManyField(User, related_name='likes_set')
  
  def get_url(self):
    return reverse('question-details', args=[self.id])
  
  def __unicode__(self):
    return self.title

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question) 
	author = models.ForeignKey(User, default=1)

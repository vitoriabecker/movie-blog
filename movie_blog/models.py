from django.db import models
from django.utils import timezone
from django.urls import reverse

class Movie(models.Model):
  user = models.CharField(max_length=200, default='anything')                  
  director = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  poster = models.ImageField(upload_to='media/posters', null=True)
  synopsis = models.TextField()
  year = models.TextField(max_length=4, blank=True, null=True)
  published_date = models.DateTimeField(default=timezone.now())

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def approve_comments(self):
    return self.comments.filter(approved_comment=True)
  
  def get_absolute_url(self):
    return reverse('movie_detail', kwargs={'pk':self.pk})

  def __str__(self):
    return self.title
  

class Comment(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
  movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
  text = models.TextField()
  create_date = models.DateTimeField(default=timezone.now())

  class Meta:
    ordering = ('create_date',)

  def __str__(self) -> str:
    return 'Comment {} by {}'.format(self.text, self.user)
  

class Rating(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, related_name='rating', on_delete=models.CASCADE)
  rate = models.IntegerField(default=0)

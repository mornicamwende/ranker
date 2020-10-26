from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    url = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class rating(models.Model):
    usability, design, content = models.IntegerField(), models.IntegerField(), models.IntegerField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT= models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE)


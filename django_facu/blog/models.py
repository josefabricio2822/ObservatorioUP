from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.TextField(verbose_name="link to the paper", default="https://docs.djangoproject.com/en/2.2/topics/db/models/")
    CATEGORIAS = (
        ('L', 'Logistica'),
        ('H', 'Hospitales'),
        ('A', 'Ambiente'),
    )
    category = models.CharField(max_length=1, choices=CATEGORIAS, default="L")

    def __str__(self):
        return self.title

class PostDetail(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    postDetail_title = models.CharField(max_length=100)
    postDetail_content = models.TextField()

    def __str__(self):
        return self.postDetail_title

class Presentation(models.Model):
    postDetail = models.ForeignKey(PostDetail, on_delete=models.CASCADE)
    presentation_title = models.CharField(max_length=100)
    presentation_content = models.TextField()

    def __str__(self):
        return self.presentation_title

class Presentation_ImageOnline(Presentation):
    ImageOnline_link = models.TextField(verbose_name="link to the image", default="https://i.pinimg.com/236x/bb/16/5c/bb165c8fcecf107962691450d7505dd3--world-cutest-dog-cutest-dogs.jpg")

    def __str__(self):
        return self.presentation_title
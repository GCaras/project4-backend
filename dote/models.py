from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
            return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')
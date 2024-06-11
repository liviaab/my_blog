from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
       return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    publication_date = models.DateTimeField("date published")
    
    def __str__(self):
       return self.title

class Interaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
       return  "User " + self.user_id + ", Post " + self.post_id + ", Rating " + self.rating 

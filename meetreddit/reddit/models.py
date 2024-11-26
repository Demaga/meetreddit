from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subreddit(models.Model):
    name = models.TextField()
    nsfw = models.BooleanField()

    def __str__(self):
        return self.name

class UserSubreddit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    to_show = models.BooleanField(default=True)
    to_highlight = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - " + self.subreddit

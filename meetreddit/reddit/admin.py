from django.contrib import admin

from .models import Subreddit, UserSubreddit

# Register your models here.
admin.site.register(Subreddit)
admin.site.register(UserSubreddit)
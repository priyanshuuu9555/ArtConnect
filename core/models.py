from django.db import models
from django.contrib.auth.models import User

# core/models.py
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField(blank=True, null=True)  # ✅ allow empty captions
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}'s post"

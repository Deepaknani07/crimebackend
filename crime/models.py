from django.db import models

class Crime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=80)
    status = models.CharField(max_length=20,default='pending')

    def __str__(self):
        return self.title
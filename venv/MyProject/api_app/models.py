from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


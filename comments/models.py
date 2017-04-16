from django.db import models


class Comment(models.Model):
    text = models.CharField(max_length=50000)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

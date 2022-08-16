from django.db import models

class Blog(models.Model):
    title=models.TextField(max_length=200)
    date=models.DateField()
    description = models.TextField(max_length=1500)
    def __str__(self):
        return self.title

from django.db import models

# Model Template View
class Article(models.Model):
    # id = Primary Key
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.title} - {self.content}'

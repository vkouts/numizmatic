from django.db import models

# Create your models here.
class CoinTags(models.Model):
    title = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

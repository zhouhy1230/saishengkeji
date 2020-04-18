from django.db import models


# Create your models here.
class ClientName(models.Model):
    ip = models.CharField(max_length=32, primary_key=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.ip}-{self.score}'

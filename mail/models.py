from django.db import models

# Create your models here.

class Mail(models.Model):
    tittle = models.CharField(max_length=200)
    text = models.TextField(blank=False)
    isSend = models.BooleanField(default=False)

    def __str__(self):
        return self.tittle

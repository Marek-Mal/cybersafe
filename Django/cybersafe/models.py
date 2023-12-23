from django.db import models

# Create your models here.

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200, blank=False, null=False)
    answer = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.question
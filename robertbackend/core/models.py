from django.db import models

# Create your models here.
class Test(models.Model):
    snake_value = models.IntegerField(null=False)
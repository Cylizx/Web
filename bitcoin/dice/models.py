from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=30)
    result = models.BooleanField()
    transaction = models.IntegerField()
    balance = models.IntegerField() 
    def __unicode__(self):
    # 在Python3中使用 def __str__(self):
        return self.name
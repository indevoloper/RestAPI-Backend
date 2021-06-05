from django.db import models

# Create your models here.
class app(models.Model):
    username = models.CharField(max_length=120)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.BooleanField(default=False)

    def _str_(self):
        return self.username
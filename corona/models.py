from django.db import models
class Country(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    

    def __str__(self):
        return self.name 
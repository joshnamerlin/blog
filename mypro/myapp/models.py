from django.db import models
class Register(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    confirm_password=models.CharField(max_length=10)
    email=models.EmailField(max_length=10)
    phone=models.IntegerField()
def __str__(self):
    return self.name

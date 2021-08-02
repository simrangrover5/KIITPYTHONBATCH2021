from django.db import models

# Create your models here.
class AddUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)  # unique_key --> True
    password = models.CharField(max_length=200)

    class Meta:
        ordering = ['fname']

    def __str__(self):
        return f"{self.email}"

    
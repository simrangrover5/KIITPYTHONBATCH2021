from django.db import models
from datetime import datetime 
from users.models import AddUser

# Create your models here.
class Addblog(models.Model):
    author = models.ForeignKey(to=AddUser, on_delete=models.CASCADE) # Parent table --> AddUser, Addblog --> child table
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())
    cat = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author}"


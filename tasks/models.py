from audioop import reverse
from tkinter import Widget
from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('Update',args=[self.id])
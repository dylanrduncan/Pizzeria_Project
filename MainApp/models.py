from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name[:50]}..."


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name="details", on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.text[:50]}..."

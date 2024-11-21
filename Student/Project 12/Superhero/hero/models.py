from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField(default="None")
    image = models.ImageField(upload_to='superhero_images/', blank=True, null=True)  # Change to ImageField
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()
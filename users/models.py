from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class User(AbstractUser):
      phone_number = models.CharField(max_length=13, null=True, blank=True)
      pro = models.ForeignKey("questions.Category", on_delete=models.SET_NULL, null=True, blank=True )
      address = models.CharField(max_length=100, null=True, blank=True)
      bio = models.CharField(max_length=100, null=True, blank=True)
      pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
      web = models.URLField(null=True, blank=True)
      github = models.URLField(null=True, blank=True)
      is_verified = models.BooleanField(default=False)

      def get_absolute_url(self):
        return reverse('home')
      
            



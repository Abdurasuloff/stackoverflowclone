from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm):
            model = User
            fields = ("username", "first_name", "last_name", "email" )


class CustomUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm):
            model = User
            fields = ("username", 'pro', "first_name", "last_name", "pic", 'github', 'web', 'phone_number', 'address','bio'   )


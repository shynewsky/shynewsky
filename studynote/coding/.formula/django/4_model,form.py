# models.py - 그대로 유지
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

#---------------------------------------------------------------------

# settings.py - 그대로 유지
AUTH_USER_MODEL = 'accounts.User'

#---------------------------------------------------------------------

# admin.py - 그대로 유지
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

#---------------------------------------------------------------------

# forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms. import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm): # create
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        
class CustomUserChangeForm(UserChangeForm): # update
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',) # 후행쉼표 필수!

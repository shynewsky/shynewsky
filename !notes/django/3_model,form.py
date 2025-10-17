# models.py - 로그인/로그아웃 용도
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

#---------------------------------------------------------------------

# settings.py
AUTH_USER_MODEL = 'accounts.User'

#---------------------------------------------------------------------

# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

#---------------------------------------------------------------------

# forms.py 수정사항 없음
# 내장폼 AuthenticationForm 사용

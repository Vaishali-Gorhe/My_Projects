from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class DIM_USER(models.Model):
    EMAIL_ID = models.EmailField(max_length=255, unique=True)
    FIRST_NAME = models.CharField(max_length=255, null=True, blank=True)
    LAST_NAME = models.CharField(max_length=255, null=True, blank=True)
    OLD_PASSWORD = models.TextField(null=True)
    PASSWORD = models.TextField(null=True)
    USER_REGISTRATION_DATE = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    IS_ACTIVE = models.BooleanField(default=True)
    LAST_LOGIN_DATE = models.DateTimeField(null=True, blank=True)

    
    class Meta:
        app_label = 'stage_weather'
        db_table = "DIM_USER"
        # managed = False

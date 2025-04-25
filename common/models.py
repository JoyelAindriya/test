from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.utils import timezone



class UserAccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required')
        user = self.model(username=username, **extra_fields)
        if not password:
            raise ValueError('Password is required')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(username, password, **extra_fields)

    

class UserAccount(AbstractBaseUser,PermissionsMixin):
    username   = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=255, unique=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    aadhar_no = models.CharField(max_length=255)
    aadhar_card = models.FileField(upload_to='addhar_card/',default=None,null=True)
    bank_pass_book  = models.FileField(upload_to='bank_pass_book/',default=None,null=True)
    is_superuser = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)  
    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
        return self.name


class Blog(models.Model):
    name    = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file            = models.FileField(upload_to='blog/',null=True,default=None)
    created_at      = models.DateTimeField(max_length=100,auto_now_add=True)


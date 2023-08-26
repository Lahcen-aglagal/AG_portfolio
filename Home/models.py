from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AdminManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Admin(AbstractBaseUser):
    STAT_CHOICES = (
        ('married', 'Married'),
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    )

    DEGREE_CHOICES = (
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    )

    email = models.EmailField('Email', max_length=100, unique=True)
    name = models.CharField('Name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    phone = models.CharField('Phone', max_length=100)
    address = models.CharField('Address', max_length=100)
    status = models.CharField('Status', max_length=20, choices=STAT_CHOICES, default='single')
    birth_date = models.DateField('Birth date', auto_now_add=False)
    city = models.CharField('City', max_length=100)
    degree = models.CharField('Degree', max_length=20, choices=DEGREE_CHOICES)

    description = models.TextField('Description', max_length=1000, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdminManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'phone', 'address', 'birth_date', 'city', 'degree']

    def __str__(self):
        return self.email
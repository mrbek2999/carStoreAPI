from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Clients(models.Model):
    passport_series = models.CharField(max_length=10)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.firstname


class Cars(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Cars"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.brand


class Orders(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Cars, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name = "Orders"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.car_id.brand} {self.car_id.model}"


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError("Users must have a username.")
        user = self.model(email=self.normalize_email(email), username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email), username=username, password=password,)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"
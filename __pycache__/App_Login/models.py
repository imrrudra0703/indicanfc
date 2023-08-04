from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, User


#To Automatically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver
from birthday import BirthdayField



# Create your models here.
class Subscriber(models.Model):
    subs = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100, blank=False)
    fullname = models.CharField(max_length=100, blank=False)
    dob = models.CharField(max_length=20, blank=False)
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'T', u'Transgender'),
    )
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, blank=False)
    contact = models.CharField(max_length=12, blank=False)
    country = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=20, blank=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "'s Profile"

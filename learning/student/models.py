from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import FileExtensionValidator, RegexValidator

class UserProfile(models.Model):

    user = models.OneToOneField(User,unique=True,db_index=True,related_name='profile',on_delete=models.CASCADE)
    name = models.CharField(blank=True,max_length=255,db_index=True)
    location = models.CharField(blank=True, max_length=255, db_index=True)
    year_of_birth = models.IntegerField(blank=True, null=True, db_index=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d*$',
        message="Phone number must start with '+' (optional) followed by digits (0-9) only.",
    )
    phone_number = models.CharField(validators=[phone_regex], blank=True, null=True, max_length=50)

    address = models.TextField(blank=True, null=True)

    @property
    def fullname(self):
        return self.name


    @property
    def age(slef):
        year_of_birth = slef.year_of_birth
        today = datetime.now().year
        if year_of_birth is not None:
            return today - year_of_birth - 1





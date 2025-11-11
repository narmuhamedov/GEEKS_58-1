from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('unknown', 'unknown')
    )

    phone_number = models.CharField(max_length=13, default="+996")
    gender = models.CharField(max_length=100, choices=GENDER, default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


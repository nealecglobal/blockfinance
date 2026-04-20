from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # ⚠️ FOR CYBERSECURITY DEMO ONLY
    demo_plain_password = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
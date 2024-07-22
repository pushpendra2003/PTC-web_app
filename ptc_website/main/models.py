from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Task(models.Model):
    TASK_TYPES = (
        ('shortlink', 'Shortlink'),
        ('offerwall', 'Offerwall'),
        ('survey', 'Survey'),
    )
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    description = models.TextField()
    reward = models.DecimalField(max_digits=10, decimal_places=2)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()

    def save(self, *args, **kwargs):
        # Check if IP address is unique
        if UserProfile.objects.exclude(id=self.id).filter(ip_address=self.ip_address).exists():
            raise ValidationError("IP address already in use.")
        super().save(*args, **kwargs)

class Click(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')

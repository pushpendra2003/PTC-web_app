from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from .models import UserProfile

@receiver(user_logged_in)
def update_user_ip(sender, request, user, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    UserProfile.objects.update_or_create(user=user, defaults={'ip_address': ip_address})

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


User = get_user_model()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class AuditModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class PostModel(AuditModel):
    image = models.ImageField(upload_to='posts/images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=1200)

    class Meta:
        verbose_name = 'Post'

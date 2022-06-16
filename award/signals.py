from django.db.models.signals import post_save 
from django.contrib.auth.models import User  #acts a the sender if signal
from django.dispatch import receiver
from award.models import Profile


#creaate user profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, created , **kwargs):
   instance.profile.save()
 

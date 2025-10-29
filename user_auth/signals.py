from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile




@receiver(post_save,sender=User)

def create_profile(sender,instance,created,**kwargs):
    if created:
       Profile.objects.create(user=instance)
    
    
    

    
    
@receiver(post_save,sender=User)

def save_profile(sender,instance,created,**kwargs):
     instance.profile.save()


    


@receiver(post_save,sender=Profile)

def sync_gmail_to_user(sender,instance,created,**kwargs):
      user=instance.user

      if instance.gmail and  user.email!=instance.gmail:
           user.email=instance.gmail
           user.save(update_fields=['email'])
        

@receiver(post_save,sender=User)

def sync_user_to_gmail(sender,instance,created,**kwargs):
     profile=instance.profile

     if instance.email and instance.email!=profile.gmail:
          profile.gmail=instance.email
          profile.save(update_fields=['gmail'])
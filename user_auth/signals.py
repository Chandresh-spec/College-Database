from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail



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
        







@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f"Sending email to: {instance.email}")
        send_mail(
            subject="Welcome!",
            message=f"Hi {instance.username}, aap gay ho",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email],
            fail_silently=False,
        )


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100,blank=True,null=True)
    phone=models.CharField(max_length=10,blank=True,null=True)
    bio=models.TextField(default="Hello! I'm new  here ",blank=True)
    profile_img=models.ImageField(upload_to='profile_pic',null=True,blank=True)
    gmail=models.EmailField(null=True,blank=True)
    city=models.CharField(max_length=10,blank=True,null=True)
    dob=models.DateTimeField(blank=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.user.username} 's Profile"


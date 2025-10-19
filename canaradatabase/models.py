from django.db import models
from Course.models import Courses

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    course_name=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True,blank=True)
    gmail=models.EmailField(null=False,blank=False)
    uucms_num=models.CharField(max_length=15,blank=False,null=False)
    rno=models.IntegerField(null=False)
    photo=models.ImageField(upload_to='studentphoto/',null=True)

    def __str__(self):
        return f"{self.name} -{self.rno}"
from django.db import models
from Course.models import Courses

class Teacher(models.Model):
    t_name = models.CharField("Teacher Name", max_length=100, null=True, blank=True)
    t_image=models.ImageField(upload_to='teacher',null=True,blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    branch = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="teachers")
    subjects = models.CharField(max_length=200, null=True, blank=True)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    about = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.t_name or "Unnamed Teacher"

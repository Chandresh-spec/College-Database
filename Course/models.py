from django.db import models

# Create your models here.
class Courses(models.Model):
    COURSE_CHOICES = [
        ('BCA', 'BCA'),
        ('BBA', 'BBA'),
    ]

    course_name = models.CharField(max_length=3, choices=COURSE_CHOICES)
    year = models.CharField(
        max_length=20,
        choices=[
            ('First Year', 'First Year'),
            ('Second Year', 'Second Year'),
            ('Final Year', 'Final Year'),
        ]
    )
    sub1 = models.CharField(max_length=50)
    sub2 = models.CharField(max_length=50)
    sub3 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name} - {self.year}"

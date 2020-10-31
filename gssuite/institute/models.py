from django.db import models
from accounts.models import User

# Create your models here.


class Institute(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    email = models.EmailField()


class InstituteManager(models.Model):
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now = True)

    
class Course(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE)


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    is_teacher = models.BooleanField(default = False)
    date_added = models.DateTimeField(auto_now = True)